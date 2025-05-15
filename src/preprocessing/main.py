from src.preprocessing.prompt import pdf_content_prompt

from src.preprocessing.load import load_pdf_content_dump

from src.llm.llm import GeminiLLM

from src.preprocessing.utils import load_json, save_json, parse_json, load_txt, save_txt

base_dir = "data/raw"

fas_files = [
    {
        "filename": f"{base_dir}/fas/4_Musharaka.PDF",
        "name": "musharaka",
        "parts": [
            [1, 10],
            [11, 14],
            [15, 24],
            [25, 30]
        ]
    },
    {
        "filename": f"{base_dir}/fas/7_Salam.PDF",
        "name": "salam",
        "parts": [
            [1, 9],
            [10, 12],
            [13, 20],
            [21, 26]
        ]
    },
    {
        "filename": f"{base_dir}/fas/10_Istisnaa.PDF",
        "name": "istisnaa",
        "parts": [
            [1, 14],
            [15, 23],
            [24, 33],
            [34, 42]
        ]
    },
    {
        "filename": f"{base_dir}/fas/28_Murabaha.PDF",
        "name": "murabaha",
        "parts": [
            [1, 6],
            [7, 16],
            [17, 21],
        ]
    },
    {
        "filename": f"{base_dir}/fas/32_Ijarah.PDF",
        "name": "ijarah",
        "parts": [
            [1, 8],
            [9, 13],
            [13, 15],
            [15, 20],
            [21, 23],
            [23, 25],
            [26, 31],
            [32, 39],
            [40, 41]
        ]
    }
]

ss_files = [
    {
        "filename": f"{base_dir}/ss/12_Musharakah.PDF",
        "name": "musharaka",
        "parts": [
            [1, 5],
            [6, 16],
            [17, 26],
            [26, 31],
            [32, 42],
            [43, 44],
            [45, 59],
            [60, 61],
            [62, 70]
        ]
    },
    {
        "filename": f"{base_dir}/ss/10_Salam.PDF",
        "name": "salam",
        "parts": [
            [1, 14],
            [15, 17],
            [18, 24],
        ]
    },
    {
        "filename": f"{base_dir}/ss/8_Murabahah.PDF",
        "name": "murabaha",
        "parts": [
            [1, 5],
            [6, 12],
            [12, 20],
            [21, 26],
            [27, 35],
            [36, 38]
        ]
    },
    {
        "filename": f"{base_dir}/ss/9_Ijarah.PDF",
        "name": "ijarah",
        "parts": [
            [1, 5],
            [6, 12],
            [12, 19],
            [20, 23],
            [24, 34],
        ]
    }
]

llm = GeminiLLM()

def get_outline(doc_content: dict) -> dict:
    def recurse(node):
        outline_node = {
            "title": node.get("title"),
            "tag": node.get("tag")
        }
        if "sections" in node:
            outline_node["sections"] = [recurse(child) for child in node["sections"]]
        return outline_node
    return recurse(doc_content)

def build_outline(outline: dict, indent=0):
    lines = []
    indent_str = "  " * indent
    title = outline.get("title")
    tag = outline.get("tag", None)
    
    if title:
        if tag:
            lines.append(f"{indent_str}- {title} — [{tag}]")
        else:
            lines.append(f"{indent_str}- {title}")
    
    for section in outline.get("sections", []):
        lines.extend(build_outline(section, indent + 1))
    
    return lines

def create_chunks(doc_content: dict, parent_path=None, parent_tags=None):
    if parent_path is None:
        parent_path = []
    if parent_tags is None:
        parent_tags = []

    chunks = []

    title = doc_content.get("title")
    tag = doc_content.get("tag")
    content = doc_content.get("content")

    current_path = parent_path + [title] if title else parent_path
    current_tags = parent_tags + [tag] if tag else parent_tags

    if content:
        heading = " > ".join(current_path)
        chunks.append({
            "tags": current_tags,  # Changed to plural for clarity
            "content": f"{heading}\n\n{content}"
        })

    for section in doc_content.get("sections", []):
        chunks.extend(create_chunks(section, current_path, current_tags))

    return chunks

if __name__ == "__main__":
    type = "fas" # fas, ss
    if type == "fas":
        files = fas_files
    elif type == "ss":
        files = ss_files
    for file in files:
        filename = file["filename"]
        name = file["name"]
        doc_content = {}
        outline = {}
        print("Loading PDF...", filename)
        for i, part in enumerate(file["parts"]):
            print("Processing part...", part)
            start, end = part
            content = load_pdf_content_dump(filename, page_start=start, page_end=end)
            prompt = pdf_content_prompt(content)
            response = llm.generate(prompt)
            response = parse_json(response)
            if i==0:
                doc_content = response
            else:
                doc_content["sections"].extend(response["sections"])
                
        save_json(doc_content, f"data/processed/{type}/{name}/content.json")
        
        outline = get_outline(doc_content)
        outline = build_outline(outline)
        save_txt('\n'.join(outline), f"data/processed/{type}/{name}/outline.txt")
        
        chunks = create_chunks(doc_content)
        save_json(chunks, f"data/processed/{type}/{name}/chunks.json")
