from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import CSVLoader
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_documents(paths):

    documents = []

    for path in paths:

        if path.endswith(".pdf"):
            loader = PyPDFLoader(path)

        elif path.endswith(".csv"):
            loader = CSVLoader(file_path=path)

        elif path.endswith(".docx"):
            loader = UnstructuredWordDocumentLoader(path)

        else:
            continue

        docs = loader.load()
        documents.extend(docs)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    return chunks
