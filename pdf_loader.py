# pdf_loader.py
import PyPDF2

def load_pdf(file_path):
    """
    Load and read a PDF file.
    Args:
        file_path (str): The path to the PDF file.
    Returns:
        str: The extracted text from the PDF.
    """
    
    try:
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                # Use a fallback if text extraction fails
                text += page.extract_text() or ""
    except Exception as e:
        raise ValueError(f"Error reading the PDF file: {e}")
    
    return text

def split_text(text, chunk_size=1000, overlap=100):
    """
    Split text into chunks of a specified size with optional overlap.
    Args:
        text (str): The text to split.
        chunk_size (int): The size of each chunk.
        overlap (int): The overlap between consecutive chunks.
    Returns:
        list: A list of text chunks.
    """
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunk = text[i:i+chunk_size]
        chunks.append(chunk)
    
    return chunks