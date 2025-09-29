import streamlit as st
import os

st.set_page_config(page_title="Two-Person Chat", layout="centered")

chat_file = "chat_history.txt"

# Load previous chat history if file exists
if "messages" not in st.session_state:
    if os.path.exists(chat_file):
        with open(chat_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # Strip newlines and keep last 50
        st.session_state.messages = [line.strip() for line in lines][-50:]
    else:
        st.session_state.messages = []

st.title("💬")

# Display messages from session state as chat messages
for msg in st.session_state.messages:
    msg = str(msg)
    if msg.lower().startswith("bb1"):
        with st.chat_message("user"):
            st.write(msg[3:].strip())
    else:
        with st.chat_message("assistant"):
            st.write(msg.strip())

# Input box for new message
user_input = st.chat_input("Type a message...")

if user_input:
    # Append new message, keep last 50
    st.session_state.messages.append(str(user_input))
    st.session_state.messages = st.session_state.messages[-50:]

    # Write updated messages back to file (overwrite)
    with open(chat_file, "w", encoding="utf-8") as f:
        for msg in st.session_state.messages:
            f.write(msg + "\n")

    # Rerun to update interface instantly with new message
    st.experimental_rerun()
