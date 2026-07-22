from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm():

    token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

    llm = HuggingFaceEndpoint(
        repo_id="Qwen/Qwen2.5-7B-Instruct",
        task="text-generation"
    )

    return ChatHuggingFace(llm=llm)