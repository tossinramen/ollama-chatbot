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

model = ChatOllama(model='llama3.2:1b', base_url='http://localhost:11434/')


system_message = SystemMessagePromptTemplate.from_template("You are a helpful AI Assistant. You work as a teacher for college students. You explain things in short and brief explanations.")


if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []


with st.form("llm-form"):
    text = st.text_area("Enter your prompt here:")
    submit = st.form_submit_button("Submit")



def generate_response(chat_history):
    chat_template = ChatPromptTemplate.from_messages(chat_history)
    chain = chat_template|model|StrOutputParser()
    response = chain.invoke({})
    return response

#user message in user key 
#ai message in assitant key 
def get_history():
    chat_history = [system_message]
    for chat in st.session_state['chat_history']:
        prompt = HumanMessagePromptTemplate.from_template(chat['user'])
        chat_history.append(prompt)

        ai_message = AIMessagePromptTemplate.from_template(chat['assistant'])
        chat_history.append(ai_message)

    return chat_history




if submit and text:
    with st.spinner("Generating response..."):
        prompt = HumanMessagePromptTemplate.from_template(text)
        chat_history = get_history()
        chat_history.append(prompt)
        #st.write(chat_history)
        response = generate_response(chat_history)
        st.session_state['chat_history'].append({'user': text, 'assistant': response})
        #st.write(response)
        #st.write(st.session_state['chat_history'])

st.write('## Chat History')
for chat in reversed(st.session_state['chat_history']):
    st.markdown(f"**🧑‍💻 User:** {chat['user']}", unsafe_allow_html=True)
    st.markdown(f"**🧠 Assistant:** {chat['assistant']}", unsafe_allow_html=True)
    st.write("---")
