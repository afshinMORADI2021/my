import streamlit as st
import script_sec_1


todos = script_sec_1.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    script_sec_1.write_todos(todos)



st.title("My Todo APP")
st.subheader("this is mine")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)

    if checkbox:
        todos.pop(index)
        script_sec_1.write_todos(todos)
        del st.session_state[index
        ]
        st.experimental_rerun()

st.text_input(label="Enter your fucking name",
              placeholder="Enter your fucking todos",
              on_change=add_todo, key='new_todo')

st.write("training")
st.checkbox("hello")



