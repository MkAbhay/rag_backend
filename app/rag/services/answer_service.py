import tiktoken
from app.rag.llm.openai import gpt_4_1_mini as llm
from app.rag.prompt.ask import prompt
from app.rag.retrievers.vector_retriever import retriever

class AnswerService:

    @staticmethod
    def ask(question: str):

        docs = retriever.invoke(question)
        context = "\n\n".join([
            doc.page_content for doc in docs
        ])

        input_data = {
            "context": context,
            "question": question
        }

        chain = prompt | llm

        response = chain.invoke(input_data)

        formatted_prompt = prompt.format(**input_data)

        encoding = tiktoken.get_encoding("cl100k_base")
        prompt_tokens = len(encoding.encode(formatted_prompt))

        return {
            "answer": response.content,
            "prompt": formatted_prompt,
            "tokens": prompt_tokens,
            "sources": [
                {
                    "document_id": doc.metadata.get("document_id"),
                    "chunk_id": doc.metadata.get("chunk_id")
                }
                for doc in docs
            ]
        }
