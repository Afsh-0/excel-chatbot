#It connects the pieces
import pandas as pd
import ollama

from llm_query import generate_query
from query_engine import execute_query


MODEL = "llama3.2"


def generate_answer(question, result):

    prompt = f"""
You are a humanitarian data assistant.

The user asked:

{question}

The calculation was performed directly on the complete Excel dataset.

Here is the exact result produced by the data analysis engine:

{result}

Answer the user's question using ONLY this result.

Rules:
- Never invent numbers.
- Never calculate a different number yourself.
- Do not use outside knowledge.
- Clearly explain the result.
- If the result is a table, present it clearly.
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def ask_chatbot(question, data):
    query = generate_query(
        question,
        data
    )
    result = execute_query(
        data,
        query
    )

    answer = generate_answer(
        question,
        result
    )

    return answer