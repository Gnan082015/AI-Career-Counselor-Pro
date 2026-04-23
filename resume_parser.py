
import pdfplumber

def extract_text(file):
    if file is None:
        return ""

    text = ""

    try:
        with pdfplumber.open(file.name) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

    except Exception as e:
        return f"Error reading file: {str(e)}"

    return text