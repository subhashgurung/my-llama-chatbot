import streamlit as st
import subprocess

st.title("🦙 LLaMA 3 Chatbot (Local + Free)")

if "history" not in st.session_state:
    st.session_state.history = []

# Display previous messages
for role, message in st.session_state.history:
    with st.chat_message(role):
        st.markdown(message)

# User input
if prompt := st.chat_input("Say something..."):
    # Show user's message
    st.chat_message("user").markdown(prompt)
    st.session_state.history.append(("user", prompt))

    # Build prompt with memory
    full_prompt = ""
    for role, message in st.session_state.history:
        if role == "user":
            full_prompt += f"User: {message}\n"
        else:
            full_prompt += f"Assistant: {message}\n"
    full_prompt += "Assistant:"

    # Run LLaMA 3 via Ollama
    result = subprocess.run(["ollama", "run", "llama3"], input=full_prompt.encode(), capture_output=True)
    response = result.stdout.decode().strip()

    # Show response
    st.chat_message("assistant").markdown(response)
    st.session_state.history.append(("assistant", response))
