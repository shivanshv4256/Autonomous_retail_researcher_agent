import chromadb
from chromadb.utils import embedding_functions
from datetime import datetime


client = chromadb.PersistentClient(path="./chroma_storage")

embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = client.get_or_create_collection(
    name="retail_reports",
    embedding_function=embedding_function
)

def store_report(report_text):
    report_id = f"report_{datetime.now().timestamp()}"
    collection.add(
        documents=[str(report_text)],
        ids=[report_id]
    )

def search_similar_reports(query, n_results=2):
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results["documents"]