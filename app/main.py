import os

import langchain
import openai
from fastapi import FastAPI
from langchain.indexes import VectorstoreIndexCreator

API_KEY = os.environ.get("OPENAI_API_KEY")

loader = langchain.document_loaders.TextLoader("app/data.txt")

index = VectorstoreIndexCreator().from_loaders([loader])

app = FastAPI()


@app.get("/api/query")
def query(q: str):
    return {"data": index.query(q)}
