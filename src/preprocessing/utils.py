import re
import json

def clean_text(text: str):
    # Remove lines that are mostly repeated punctuation characters
    text = re.sub(r'^[\s\.\-_]{5,}$', '', text, flags=re.MULTILINE)
    # Remove long chains of dots, dashes, underscores even inside lines
    text = re.sub(r'[\.\-_]{5,}', '', text)
    # Remove weird spacing artifacts
    text = re.sub(r'\s{2,}', ' ', text)
    # Optional: remove multiple blank lines
    text = re.sub(r'\n\s*\n+', '\n\n', text)
    return text.strip()

def load_txt(path: str):
    with open(path, 'r') as f:
        data = f.read()
        return data

def save_txt(data, path: str):
    with open(path, 'w') as f:
        f.write(data)
        
def load_json(path: str):
    with open(path, "r") as f:
        data = json.load(f)
    return data

def save_json(data, path: str):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        
def parse_json(json_str: str):
    start = json_str.find("```json")
    if start == -1:
        raise ValueError("No ```json found in the string")
    end = json_str.rfind("```")
    if end == -1:
        raise ValueError("No ``` found in the string")
    json_str = json_str[start + len("```json"):end]
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse \n {json_str} \n JSON: {e}")