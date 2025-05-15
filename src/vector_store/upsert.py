import os
import json
from tqdm import tqdm
from pinecone import Pinecone

from src.vector_store.embedding import get_embeddings

from src.config.keys import PINECONE_API_KEY
from src.config.config import INDEX_NAME, INDEX_NAMESPACE

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

def load_chunks_from_dir(base_dir: str):
    all_chunks = []
    for doc_type in ["fas", "ss"]:
        dir_path = os.path.join(base_dir, doc_type)
        for operation in os.listdir(dir_path):
            file_path = os.path.join(dir_path, operation, 'chunks.json')
            with open(file_path, "r") as f:
                chunks = json.load(f)
                for i, chunk in enumerate(chunks, start=1):
                    chunk_id = f"{doc_type} {operation} {i}"
                    all_chunks.append({
                        "id": chunk_id,
                        "text": chunk["content"],
                        "metadata": {
                            "doc_type": doc_type,
                            "operation": operation,
                            "tag": chunk["tag"]
                        }
                    })
    return all_chunks

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
    
    DATA_DIR = "data/processed" 
    
    print("Loading chunks...")
    chunks = load_chunks_from_dir(DATA_DIR)
    print(f"Loaded {len(chunks)} chunks")

    print(f"Upserting to Pinecone index: {INDEX_NAME}")
    upsert_chunks(chunks)
    print("Upsert complete!")
