import ollama
import streamlit as st
st.markdown("# My AI Chat Application")
with st.sidebar:
    st.header(":blue[Chat Settings]")
    if st.button("Clear Chat 🗑️"):
        st.session_state.messages = []
        st.success("Chat cleared")
    personalities = {
        "Kid" : "Answer the questions like you are explaining to a 5 year old kid. Give answer in 2 lines only.",
        "Friend" : "Answer the questions in a friendly and casual manner. Give answers in 2 lines only."
    }
    personality = st.selectbox("Select a personality", personalities.keys())
    uploaded_file = st.file_uploader("Upload a text file...")
    try:
        if uploaded_file:
            content = uploaded_file.read().decode("utf-8")
            st.success("File uploaded successfully")
            if st.button("Display"):
                st.text(content)
    except:
        st.error("File type not supported")
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question = st.chat_input("Ask a question...")
if question:
    st.session_state.messages.append(
        {"role": "user",
        "content" : question}
    )
    with st.chat_message("user"):
        st.write(question)
    with st.spinner("Wait, model is loading..."):
        response = ollama.chat(
            model="llama3.2:3b",
            messages= [
                {"role" : "system","content": personalities[personality]}]
                + st.session_state.messages)
    st.session_state.messages.append({
        "role":"assistant",
        "content":response["message"]["content"]
    })
    with st.chat_message("assistant"):
        st.write(response["message"]["content"])