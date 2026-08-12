# Spreadsheet Reader

An AI-powered chatbot that can read Excel files, analyze the data, and answer questions in normal language.

## About the Project

The main purpose of this project is to make it easier to ask questions about an Excel dataset.
Instead of manually opening Excel and doing calculations, the user can simply ask a question such as:

E.g. What is the total number of refugees?

The chatbot understands the question, performs the required calculation using the Excel data, and gives the answer.


## Dataset

The project currently uses **UNHCR humanitarian population data for 2024**.

The main Excel file is inside data folder and thsi workbook contains humanitarian population information across different sheets.


## How the Chatbot Works?

The project has two main ways of answering questions.

### 1. Excel Data Questions

For questions that require numbers or calculations, the chatbot uses the actual Excel data.

E.g. What is the total number of refugees?

The flow is:

```text
User Question
     ↓
Ollama
     ↓
Understand the question
     ↓
Create a structured query
     ↓
Query Engine
     ↓
Pandas
     ↓
Excel Data
     ↓
Exact Result
     ↓
Final Answer
```

The numerical answer is calculated from the Excel data rather than being guessed by the AI for better accuracy. 


### 2. RAG Questions

RAG is used for questions that require information or explanations from documents.

E.g. What does Country of Asylum mean?

The RAG system searches the available knowledge and gives the relevant information to Ollama, which then explains it to the user.

The flow is:

```text
User Question
     ↓
RAG
     ↓
Find Relevant Information
     ↓
Ollama
     ↓
Answer
```


## 💬 Example Questions

The chatbot can answer questions such as:

```text
What is the total number of refugees?

What is the average number of refugees?

What is the maximum number of refugees?

What is the minimum number of refugees?

What are the top 5 countries by total refugees?

What is the average number of refugees in India?

What is the total number of refugees in India and Nepal?

What does Country of Asylum mean?
```


## Project Structure

```text
SPREADSHEET_READER/
│
├── data/
│   └── Humanitarian_Data.xlsx
│
├── app.py
├── app_chatbot.py
├── chatbot.py
├── llm.py
├── llm_query.py
├── query_engine.py
├── rag.py
├── build_rag.py
│
├── chroma_db/
│
├── README.md
└── requirements.txt
```

## How to Run the Project

### 1. Create and activate the virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 2. Install the required packages

```bash
pip install -r requirements.txt
```

### 3. Make sure Ollama is installed

The project uses Ollama to run the AI model locally.

The required model is:

```text
llama3.2
```

### 4. Run the chatbot

```bash
streamlit run app_chatbot.py
```

The chatbot will open in the browser.


## Goal

The main goal of this project is to create an AI assistant that makes Excel data easier to understand.

The user should be able to ask a question in normal language instead of manually searching through rows, applying filters, and performing calculations in Excel.


