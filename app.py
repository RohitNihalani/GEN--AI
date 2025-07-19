import streamlit as st
import google.generativeai as ai

ai.configure(api_key="AIzaSyCo7EDZa1_4kAgjPbHvi7EAir3qmi1nV1I")

model = ai.GenerativeModel("gemini-1.5-flash")

st.title("WELCOME TO BOTIMUS PRIME")

user_query = st.text_input("ASK ME ANYTHING")

if st.button("GENERATE RESPONSE"):
    response = model.generate_content(user_query)
    st.write(response.text)
