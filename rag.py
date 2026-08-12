import chromadb
import ollama


EMBEDDING_MODEL = "nomic-embed-text"

def get_collection():

    client = chromadb.PersistentClient(
        path="chroma_db"
    )

    collection = client.get_or_create_collection(
        name="humanitarian_knowledge"
    )

    return collection


def create_knowledge(file_path):

    import pandas as pd

    excel_file = pd.ExcelFile(file_path)

    collection = get_collection()

    for sheet in excel_file.sheet_names:

        data = pd.read_excel(
            file_path,
            sheet_name=sheet
        )

        document = f"""
Humanitarian Dataset

Sheet name:
{sheet}

Number of rows:
{len(data)}

Columns:
{', '.join(data.columns.astype(str))}

This sheet contains humanitarian data.
"""

        embedding_response = ollama.embeddings(
            model=EMBEDDING_MODEL,
            prompt=document
        )

        collection.upsert(
            ids=[f"sheet_{sheet}"],
            documents=[document],
            embeddings=[embedding_response["embedding"]]
        )

    return "Knowledge base created successfully."

def search_knowledge(question, n_results=3):

    collection = get_collection()

    embedding_response = ollama.embeddings(
        model=EMBEDDING_MODEL,
        prompt=question
    )

    results = collection.query(
        query_embeddings=[
            embedding_response["embedding"]
        ],
        n_results=n_results
    )

    return results["documents"][0]

def get_context(question):

    documents = search_knowledge(question)

    return "\n\n".join(documents)