# pip install streamlit
# pip install langchain
# pip install -qU langchain-ollama

# 'streamlit run chatbot.py' to run
# stream lit docs for streamlit components, widgets
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate
from langchain_core.prompts import ChatPromptTemplate

st.title("Chat App with Ollama and Langchain (with Chat History)")

model = ChatOllama(model='llama3.3')

if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []




with st.form("llm-form"):
    text = st.text_area("Enter your prompt here:")
    submit = st.form_submit_button("Submit")