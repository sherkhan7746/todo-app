import streamlit as st
import functions
todos = functions.get_todos()

st.title("My Todo-app")
for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add new todo...")