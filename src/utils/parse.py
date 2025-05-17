import json

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
