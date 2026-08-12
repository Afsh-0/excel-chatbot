#translator

import json
import pandas as pd
import ollama

from query_engine import execute_query


MODEL = "llama3.2"


def generate_query(question, data):

    columns = data.columns.tolist()

    prompt = f"""
You are a data analysis assistant.

The user will ask questions about an Excel dataset.

Available columns:
{columns}

Your job is to convert the user's question into a JSON query.

The JSON must follow this structure:

{{
    "operation": "sum | mean | max | min | count | ranking",
    "column": "column name",
    "filters": {{}},
    "group_by": "column name",
    "aggregation": "sum | mean | max | min | count",
    "sort": "ascending | descending",
    "limit": number
}}

Rules:

1. Use only columns from the available columns.
2. For totals use "sum".
3. For averages use "mean".
4. For highest values use "max".
5. For lowest values use "min".
6. For rankings use "ranking".
7. If the question asks for top countries, use ranking.
8. Return ONLY valid JSON.
9. Do not explain the JSON.

User question:
{question}
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

    content = response["message"]["content"]

    # Remove possible markdown code fences
    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    return json.loads(content)


def answer_question(question, data):

    query = generate_query(question, data)

    result = execute_query(data, query)

    return result