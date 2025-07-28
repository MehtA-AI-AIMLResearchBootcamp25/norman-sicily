import streamlit as st
from chatbot import get_chatbot_response
import time

st.set_page_config(page_title="Norman Sicily Chatbot", layout="centered")
st.title("Norman Sicily Historical Chatbot")
st.markdown("Ask questions about people, places, and their historical connections.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Ask something..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    assistant_message = st.chat_message("assistant")
    message_placeholder = assistant_message.container()
    placeholder_text = message_placeholder.markdown("...")

    # Build history from last 10 user/assistant pairs
    messages = st.session_state.messages[:-1]  # exclude the most recent user message just added
    history_pairs = []
    i = 0
    while i < len(messages) - 1:
        if messages[i]["role"] == "user" and messages[i+1]["role"] == "assistant":
            history_pairs.append((messages[i]["content"], messages[i+1]["content"]))
            i += 2
        else:
            i += 1

    # Keep only the last 10 conversation pairs
    history_pairs = history_pairs[-10:]

    # Rebuild prompt history
    history = ""
    for user_msg, assistant_msg in history_pairs:
        history += f"User: {user_msg}\nAssistant: {assistant_msg}\n"

    # Add the current user message
    history += f"User: {user_input}\n"

    full_response = get_chatbot_response(history)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

    response_stream = ""
    for char in full_response:
        response_stream += char
        placeholder_text.markdown(response_stream + "▌")
        time.sleep(0.015)
    placeholder_text.markdown(response_stream)