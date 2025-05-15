import os
import json

def load_chunks(base_dir: str):
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
                            "content": chunk["content"],
                            "doc_type": doc_type,
                            "operation": operation,
                            "tags": chunk["tags"]
                        }
                    })
    return all_chunks
