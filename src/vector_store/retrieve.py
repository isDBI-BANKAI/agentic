from pinecone import Pinecone

from src.vector_store.embedding import get_embeddings
from src.config.keys import PINECONE_API_KEY, PINECONE_INDEX_HOST
from src.config.config import INDEX_NAME, INDEX_NAMESPACE

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(host=PINECONE_INDEX_HOST, name=INDEX_NAME)

def query_vdb(query: str, top_k: int = 2, filter: dict = None):
    results = index.query(
        namespace=INDEX_NAMESPACE, 
        vector=get_embeddings([query])[0],
        top_k=top_k,
        include_metadata=True,
        filter=filter,
    )
    return results

if __name__ == "__main__":
    query = "What is Islamic finance?"
    results = query_vdb(query, filter={"tag": "measurement"})
    print(f"Query: {query}")
    print(f"Results: {results}")
