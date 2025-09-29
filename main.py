import streamlit as st
import os

st.set_page_config(page_title="Two-Person Chat", layout="centered")

chat_file = "chat_history.txt"

# Callback to add new message
def laod_chat():
    if "messages" not in st.session_state:
        if os.path.exists(chat_file):
            with open(chat_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
            st.session_state.messages = [line.strip() for line in lines][-50:]
        else:
            st.session_state.messages = []

def add_message():
    msg = st.session_state.user_input
    if msg:
        st.session_state.messages.append(msg)
        st.session_state.messages = st.session_state.messages[-50:]
        # Save latest 50 messages
        with open(chat_file, "w", encoding="utf-8") as f:
            for m in st.session_state.messages:
                f.write(m + "\n")
        st.session_state.user_input = ""  # Clear input field after submit
        load_chat()



st.title("💬 Two-Person Chat")

load_chat()
# Display chat messages
for msg in st.session_state.messages:
    if msg.lower().startswith("bb1"):
        with st.chat_message("user"):
            st.write(msg[3:].strip())
    else:
        with st.chat_message("assistant"):
            st.write(msg.strip())

# Input to type new messages with callback on change
st.text_input("Type a message...", key="user_input", on_change=add_message)
