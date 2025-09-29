import streamlit as st

st.set_page_config(page_title="Two-Person Chat", layout="centered")

# Initialize session state for storing chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("💬 Simple Two-Person Chat")

# Input box
user_input = st.chat_input("Type a message...")

if user_input:
    # Always store as string
    st.session_state.messages.append(str(user_input))
    # Keep only last 50
    st.session_state.messages = st.session_state.messages[-50:]

# Display messages
for msg in st.session_state.messages:
    msg = str(msg)  # make sure it's a string
    if msg.lower().startswith("bb1"):
        with st.chat_message("user"):
            st.write(msg[3:].strip())  # strip "b:"
    else:
        with st.chat_message("assistant"):
            st.write(msg.strip())
