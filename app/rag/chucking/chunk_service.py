import tiktoken
from langchain_text_splitters  import RecursiveCharacterTextSplitter

encoding = tiktoken.get_encoding("cl100k_base")

def tiktoken_len(text):
    tokens = encoding.encode(text)
    return len(tokens)

splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=tiktoken_len,
        is_separator_regex=['\n\n', '\n', ' ', ''],
    )


def chunk_documents(documents):
    return splitter.split_documents(documents)