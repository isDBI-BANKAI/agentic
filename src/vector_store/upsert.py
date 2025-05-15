from tqdm import tqdm
from pinecone import Pinecone

from src.vector_store.embedding import get_embeddings
from src.vector_store.load import load_chunks

from src.config.keys import PINECONE_API_KEY
from src.config.config import INDEX_NAME, INDEX_NAMESPACE

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

def upsert_chunks(chunks, batch_size=96):
    for i in tqdm(range(0, len(chunks), batch_size)):
        print(f"Upserting chunks {i+1} to {i+batch_size}...")
        batch = chunks[i:i+batch_size]
        texts = [c["text"] for c in batch]
        embeddings = get_embeddings(texts)
        vectors = [
            {
                "id": batch[j]["id"],
                "values": embeddings[j],
                "metadata": batch[j]["metadata"]
            }
            for j in range(len(batch))
        ]
        index.upsert(vectors=vectors, namespace=INDEX_NAMESPACE)

if __name__ == "__main__":
    
    dir = "data/processed" 
    
    print("Loading chunks...")
    chunks = load_chunks(dir)
    print(f"Loaded {len(chunks)} chunks")

    print(f"Upserting to Pinecone index: {INDEX_NAME}")
    upsert_chunks(chunks)
    print("Upsert complete!")
