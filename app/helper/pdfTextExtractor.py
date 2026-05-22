from pypdf import PdfReader

class PDFTextExtractor:    
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._text = None

    def get_text(self) -> str:
        if self._text is not None:
            return self._text
            
        try:
            reader = PdfReader(self.file_path)
            pages_text = []
            
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    pages_text.append(text)
            
            self._text = "\n".join(pages_text)
            return self._text
            
        except Exception as e:
            return f"Failed to extract text: {e}"
