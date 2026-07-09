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

# --- Sidebar: About + Topic + Activity + Generate ---
with st.sidebar:
    st.title("🧠 NeuroNova")
    st.caption("AI Teaching Agent")

    st.markdown(
        "NeuroNova helps you learn any topic — explains concepts simply, "
        "gives real-life examples, generates quizzes, and answers your questions."
    )

    st.divider()
    st.subheader("Actions")

    topic = st.text_input("Enter a Topic")

    option = st.selectbox(
        "Choose Activity",
        [
            "Explain Concept",
            "Real-Life Example",
            "Generate Quiz",
            "Ask Anything"
        ]
    )

    if st.button("Generate", use_container_width=True):
        if topic.strip() == "":
            st.warning("Please enter a topic.")
        else:
            if option == "Explain Concept":
                st.session_state.prompt = f"Explain {topic} in simple language for a beginner."
            elif option == "Real-Life Example":
                st.session_state.prompt = f"Give one simple real-life example of {topic}."
            elif option == "Generate Quiz":
                st.session_state.prompt = f"Create 5 MCQs on {topic} with answers."
            else:
                st.session_state.prompt = f"Tell me something interesting about {topic}."

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

# Button action (from sidebar Generate button)
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