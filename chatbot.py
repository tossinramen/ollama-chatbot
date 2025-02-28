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

model = ChatOllama(model='llama3.3', base_url='http://localhost:11434/')

system_message = SystemMessagePromptTemplate.from_template("You are a helpful AI Assistant.")


if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []


def generate_repsonse(chat_history):
    chat_template = ChatPromptTemplate.from_messages(chat_history)
    chain = chat_template|model|StrOutputParser()
    response = chain.invoke({})
    return response




with st.form("llm-form"):
    text = st.text_area("Enter your prompt here:")
    submit = st.form_submit_button("Submit")

if submit and text:
    with st.spinner("Generating response..."):
        prompt = HumanMessagePromptTemplate.from_template(text)
