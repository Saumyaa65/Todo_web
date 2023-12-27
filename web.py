import streamlit as st
import Functions

todos=Functions.open_read()

def add():
    todo=st.session_state["new_todo"]+"\n"
    todos.append(todo)
    Functions.open_write(todos)

st.title("My To-Do App")
st.subheader("This is for better handling of your schedule.")
st.text("Hope it helps you.")

for i,todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(i)
        Functions.open_write(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Add new To-Do", placeholder="Enter Todo...",
              on_change=add, key="new_todo")
st.session_state