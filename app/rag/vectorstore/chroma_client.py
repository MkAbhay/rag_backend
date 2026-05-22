import chromadb

from chromadb.config import Settings

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from app.config.setting import (
    OPENAI_API_KEY,
    CHROMA_COLLECTION,
    CHROMA_DB_PATH
)

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=OPENAI_API_KEY
)

client = chromadb.PersistentClient(
    path=CHROMA_DB_PATH,
    settings=Settings(anonymized_telemetry=False)
)

vector_store = Chroma(
    client=client,
    collection_name=CHROMA_COLLECTION,
    embedding_function=embeddings
)