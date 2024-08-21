import google.generativeai as genai
import streamlit as st

st.title("welcome to gemini chat")

genai.configure(api_key="AIzaSyDhVPI34_4W1ADCuPX0GAvSLaNP14YetX0")  
text = st.text_input("enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)
