import streamlit as st
import function
from datetime import datetime

todos = function.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    function.write_todos(todos)
    st.session_state["new_todo"] = ""
    

st.title("My Todo App")
st.subheader("Your personal todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
st.text_input(label="", placeholder="Add new todo...", key="new_todo", on_change=add_todo)

st.session_state