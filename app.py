from flask import Flask, render_template, request
import os

from src.data_loader import load_documents
from src.rag_pipeline import create_rag
from src.ratio_calculator import calculate_ratios
from src.red_flag_detector import detect_red_flags
from src.trend_visualizer import generate_trend_chart

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

qa_system = None
analysis = ""
summary_lines = []
selected_files = ""
chat_history = []
file_status = "No file chosen"


@app.route("/", methods=["GET", "POST"])
def home():

    global qa_system, analysis, summary_lines, selected_files, chat_history, file_status

    message = ""

    if request.method == "POST":

        files = request.files.getlist("files")

        paths = []
        names = []

        for file in files:

            if file.filename == "":
                continue

            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)

            paths.append(path)
            names.append(file.filename)

        selected_files = ", ".join(names)
        file_status = "File uploaded"

        # LOAD DOCUMENTS
        chunks = load_documents(paths)

        retriever, llm = create_rag(chunks)
        qa_system = {"retriever": retriever, "llm": llm}

        # MERGE TEXT
        text = " ".join([c.page_content for c in chunks])

        # EXTRACT RATIOS
        ratios = calculate_ratios(text)

        # DETECT RISKS
        flags = detect_red_flags(text)

        # GENERATE TREND CHART
        generate_trend_chart(text)

        # FORMAT RATIOS FOR DISPLAY
        ratio_text = ""

        if ratios:
            for key, value in ratios.items():
                ratio_text += f"{key}: {value}%\n"
        else:
            ratio_text = "No financial ratios detected in the document.\n"

        # FORMAT RISK INDICATORS
        risk_text = ""

        if flags:
            for r in flags:
                risk_text += f"- {r}\n"
        else:
            risk_text = "No major risk indicators detected.\n"

        # FINAL ANALYSIS TEXT
        analysis = f"""
📊 Financial Ratio Analysis

The following financial ratios were identified from the report:

{ratio_text}

⚠ Risk Indicators

The system detected potential risk signals in management discussion:

{risk_text}

📈 Revenue Trend

A revenue trend chart has been generated based on extracted financial data.
"""

        # AI EXECUTIVE SUMMARY
        summary_prompt = f"""
Summarize the company performance in 5 clear bullet insights.

Context:
{text}
"""

        try:
            summary_response = llm.invoke(summary_prompt)
            raw_summary = summary_response.content

            summary_lines = [
                line.strip() for line in raw_summary.split("\n") if line.strip()
            ]

        except:
            summary_lines = ["AI summary could not be generated."]

        message = "Reports uploaded successfully."
        chat_history = []

    return render_template(
        "index.html",
        message=message,
        analysis=analysis,
        summary_lines=summary_lines,
        selected_files=selected_files,
        chat_history=chat_history,
        file_status=file_status
    )


@app.route("/chat", methods=["POST"])
def chat():

    global qa_system, chat_history, analysis, selected_files, file_status, summary_lines

    question = request.form["question"]

    if qa_system is None:

        answer = "Please upload financial reports first."

    else:

        docs = qa_system["retriever"].invoke(question)

        context = "\n".join([d.page_content for d in docs])

        prompt = f"""
Answer the question using the financial report context.

Context:
{context}

Question:
{question}
"""

        response = qa_system["llm"].invoke(prompt)

        try:
            answer = response.content
        except:
            answer = str(response)

    chat_history.append({
        "question": question,
        "answer": answer
    })

    return render_template(
        "index.html",
        analysis=analysis,
        summary_lines=summary_lines,
        chat_history=chat_history,
        selected_files=selected_files,
        file_status=file_status
    )


if __name__ == "__main__":
    app.run(debug=True)