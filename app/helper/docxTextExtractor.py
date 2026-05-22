import docx2txt
# from docx import Document

class DOCXTextExtractor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._text = None

    def get_text(self) -> str:
        if self._text is not None:
            return self._text
        
        try:
            self._text = docx2txt.process(self.file_path)
            return self._text
        # try:
        #     document = Document(self.file_path)
        #     pages_text = []

        #     for paragraph in document.paragraphs:
        #         text = paragraph.text
        #         if text:
        #             pages_text.append(text)

        #     self._text = "\n".join(pages_text)
        #     return self._text
        
        except Exception as e:
            return f"Failed to extract text: {e}"