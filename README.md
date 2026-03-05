# Automated Finance Report Analyzer

This project is an AI-powered financial report analysis system that allows users to upload company financial reports and interact with them through natural language questions. The system extracts insights such as financial ratios, risk indicators, revenue trends, and an AI-generated executive summary from the uploaded reports. It uses a Retrieval-Augmented Generation (RAG) pipeline to analyze financial documents and answer user queries based on the report content.

Currently the system uses **Ollama (local LLM)** for generating responses and summaries. I am working on improving the project further and plan to integrate **OpenAI API or other advanced LLMs** in future versions.

---

## How to Run the Project

1. Install Python (3.9 or later recommended)

2. Install the required Python modules

pip install flask
pip install langchain
pip install langchain-community
pip install chromadb
pip install pypdf
pip install python-docx
pip install matplotlib

3. Install and run **Ollama**

Download from:
https://ollama.com

After installation run a model:

ollama run mistral

4. Run the Flask application

python app.py

5. Open the application in your browser

http://127.0.0.1:5000

Make sure both ollama and app.py runs in two different terminals

Upload a financial report (**PDF recommended**) and start asking questions about the report.

---

## Features

• AI-generated executive summary of the report
• Financial ratio analysis
• Risk indicator detection from management discussion
• Revenue trend visualization
• Chat-based financial Q&A using RAG
• Local LLM inference using Ollama

---

## Current Limitation

At the moment, the system analyzes **one financial report at a time**. I am currently working on improving the system so that it can **process and analyze multiple financial documents simultaneously**.It's slower to give analysis of the report.

---

## Future Improvements

This project is still under development and I am continuously working to improve it. Planned improvements include:

• Supporting analysis of **multiple reports at once**
• Integrating **OpenAI API or other advanced LLMs**
• Improving financial ratio extraction and calculations
• Adding peer company comparison
• Enhancing visual dashboards and financial insights
• Converting the project into a **complete web application**
• Make it faster.
