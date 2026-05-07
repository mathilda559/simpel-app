import streamlit as st

st.title("Meine erste Streamlit Web App 🚀")

name = st.text_input("Wie heißt du?")

if name:
    st.write(f"Hallo {name}! Schön, dass du da bist 😊")
else:
    st.write("Gib deinen Namen ein 👆")
