import re
import fitz  # PyMuPDF
from src.preprocessing.utils import clean_text

def clean_content(content: list[str]) -> str:
    cleaned_lines = []
    buffer = ""
    last_line = None

    for line in content:
        line = clean_text(line)
        if not line or line.isnumeric():
            continue

        # Ignore duplicates (exact match or line starting with previous line)
        if last_line and (line == last_line or line.startswith(last_line)):
            continue

        # Join to previous line if it's likely a continuation (doesn't start with capital or continues prior line)
        if buffer and (not re.match(r"^[A-Z0-9]", line) or line.startswith(buffer[-10:])):
            buffer += " " + line
        else:
            if buffer:
                cleaned_lines.append(buffer)
            buffer = line

        last_line = line

    # Final flush
    if buffer:
        cleaned_lines.append(buffer)

    return '\n'.join(cleaned_lines)


def load_pdf(path: str):
    doc = fitz.open(path)
    pages = []
    for page in doc:
        content = []
        text = page.get_text("text")
        content = [text.strip() for text in text.splitlines() if text.strip()]
        pages.append(clean_content(content))
    doc.close()
    return pages

def load_pdf_content_dump(path: str, page_start: int = 1, page_end: int = None):
    pages = load_pdf(path)
    content = ""
    for i, page in enumerate(pages, start=1):
        if i < page_start:
            continue
        if page_end is not None and i > page_end:
            break
        content += f"[PAGE {i}]:\n{page}\n\n"
    return content

if __name__ == "__main__":
    PDF_PATH = "data/raw/fas/4_Musharaka.PDF"
    content = load_pdf_content_dump(PDF_PATH, page_start=0, page_end=3)
    print(content)