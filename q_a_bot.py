import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

def get_response(question):
    response_stream = chat.send_message(question, stream=True)
    return response_stream

st.set_page_config(page_title="Gemini Q&A Bot")
st.title("Gemini Q&A Chatbot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

user_input = st.text_input("Ask something...", key="input")

if st.button("Send") and user_input:
    st.session_state['chat_history'].append(("You", user_input))
    response_stream = get_response(user_input)

    full_response = ""
    st.subheader("The Response is")
    for chunk in response_stream:
        st.write(chunk.text)
        full_response += chunk.text

    st.session_state['chat_history'].append(("Gemini", full_response))

st.subheader("Chat History")
for role, message in st.session_state['chat_history']:
    st.markdown(f"**{role}:** {message}")
