from fastapi import FastAPI
from models import TextInput
import re

app = FastAPI()

@app.post("/generate-token/")
async def generate_token():
    # Example token generation logic
    return {"token": "example_token"}

@app.post("/tokenize/")
async def tokenize_text(text_input: TextInput):
    tokens = re.findall(r'\b\w+\b', text_input.text)
    return {"tokens": tokens}


