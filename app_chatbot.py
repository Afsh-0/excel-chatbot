import streamlit as st
import pandas as pd

from chatbot import ask_chatbot


st.set_page_config(
    page_title="Excelot",
    layout="wide"
)

st.title("Excelot")

st.write(
    "Ask questions about the humanitarian Excel dataset."
)

@st.cache_data
def load_data():

    file_path = "data/Humanitarian_Data.xlsx"

    return pd.read_excel(
        file_path,
        sheet_name="Population"
    )


data = load_data()

if "messages" not in st.session_state:

    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


question = st.chat_input(
    "Ask a question about the humanitarian data..."
)


if question:


    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)


    with st.chat_message("assistant"):

        with st.spinner("Analyzing..."):

            try:

                answer = ask_chatbot(
                    question,
                    data
                )

                st.markdown(answer)

            except Exception as e:

                answer = (
                    "Sorry, I couldn't process that question.\n\n"
                    f"Error: `{e}`"
                )

                st.error(answer)


    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )