
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])   
model = genai.GenerativeModel('gemini-2.5-flash')

st.set_page_config(page_title="NeuroNova", layout="wide")

# --- CSS ---
st.markdown("""
<style>
html {
    scroll-behavior: smooth;
}
[data-testid="stSidebar"] {
    background-color: #0e1117;
    border-right: 1px solid rgba(255,255,255,0.15);
}
</style>
""", unsafe_allow_html=True)

# --- Sidebar: About + Buttons ---
with st.sidebar:
    st.title("🧠 NeuroNova")
    st.caption("AI Teaching Agent")

    st.markdown(
        "NeuroNova helps you learn any topic — explains concepts simply, "
        "gives real-life examples, generates quizzes, and answers your questions."
    )

    st.divider()
    st.subheader("Actions")

    if st.button("📘 Explain Concept", use_container_width=True):
        st.session_state.prompt = "Explain in simple way"
    if st.button("🌍 Real-Life Example", use_container_width=True):
        st.session_state.prompt = "Give real life examples"
    if st.button("❓ Generate Quiz", use_container_width=True):
        st.session_state.prompt = "Create 5 MCQs on this and at last after giving my answer provide correct answers also"
    if st.button("💬 Ask Anything", use_container_width=True):
        st.session_state.prompt = "Tell me something interesting about it"

# --- Main chat area ---
st.title("🧠 NeuroNova")
st.subheader("AI Teaching Agent")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! I'm NeuroNova😊. How can I help you?"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        with st.spinner("NeuroNova is thinking..."):
            response = model.generate_content(prompt)
            st.write(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})

# Button action
if "prompt" in st.session_state:
    prompt = st.session_state.prompt
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        with st.spinner("NeuroNova is thinking..."):
            response = model.generate_content(prompt)
            st.write(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
    del st.session_state.prompt

