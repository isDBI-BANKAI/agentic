from pinecone import Pinecone

from src.vector_store.embedding import get_embeddings
from src.config.keys import PINECONE_API_KEY, PINECONE_INDEX_HOST
from src.config.config import INDEX_NAME, INDEX_NAMESPACE

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(name=INDEX_NAME)

def query_vdb(query: str, top_k: int = 5, filter: dict = None) -> list[str]:
    query_embedding = get_embeddings([query])[0]
    results = index.query(
        namespace=INDEX_NAMESPACE, 
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True,
        filter=filter,
    )
    if results and results.get("matches"):
        return [res['metadata']['content'] for res in results['matches']]
    return []

if __name__ == "__main__":
    
    q = {
        'query': "Initial Recognition at the time of commencement of Ijarah MBT using Underlying Asset Cost Method in lessee's books", 
        'filter': {'tags': {'$in': ['initial_recognition', 'ijarah_mbt_special_considerations', 'right_of_use_asset_initial_recognition']}}
    }
    query = q['query']
    filter = q['filter']
    results = query_vdb(query, filter=filter)
    print(f"Query: {query}")
    print(f"Results: {results}")
