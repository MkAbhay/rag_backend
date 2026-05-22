from langchain_openai import ChatOpenAI
from app.config.setting import OPENAI_API_KEY

gpt_4_1_mini = ChatOpenAI(
    model="gpt-4.1-mini",
    api_key=OPENAI_API_KEY,
    temperature=0
)