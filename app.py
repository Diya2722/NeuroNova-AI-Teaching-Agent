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

# --- Session state setup ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! I'm NeuroNova😊. How can I help you?"}]

if "last_topic" not in st.session_state:
    st.session_state.last_topic = ""

# --- Sidebar: About + Action Buttons only (matches your image) ---
with st.sidebar:
    st.title("🧠 NeuroNova")
    st.caption("AI Teaching Agent")
    st.markdown(
        "NeuroNova helps you learn any topic — explains concepts simply, "
        "gives real-life examples, generates quizzes, and answers your questions."
    )
    st.divider()
    st.subheader("Actions")

    explain_clicked = st.button("📘 Explain Concept", use_container_width=True)
    example_clicked = st.button("🌍 Real-Life Example", use_container_width=True)
    quiz_clicked = st.button("❓ Generate Quiz", use_container_width=True)
    ask_clicked = st.button("💬 Ask Anything", use_container_width=True)

# --- Main chat area ---
st.title("🧠 NeuroNova")
st.subheader("AI Teaching Agent")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# --- Helper to run a prompt through Gemini and display it ---
def run_prompt(prompt_text, display_text=None):
    st.session_state.messages.append({"role": "user", "content": display_text or prompt_text})
    with st.chat_message("user"):
        st.write(display_text or prompt_text)
    with st.chat_message("assistant"):
        with st.spinner("NeuroNova is thinking..."):
            try:
                response = model.generate_content(prompt_text)
                reply_text = response.text
            except Exception as e:
                error_str = str(e)
                if "429" in error_str or "ResourceExhausted" in error_str or "quota" in error_str.lower():
                    reply_text = (
                        "⚠️ I've hit today's free usage limit for the AI model "
                        "(Gemini's free tier allows a limited number of requests per day). "
                        "Please try again later!"
                    )
                else:
                    reply_text = f"⚠️ Something went wrong while generating a response: {error_str}"
            st.write(reply_text)
            st.session_state.messages.append({"role": "assistant", "content": reply_text})

# --- Chat input: user types a topic/question here ---
if prompt := st.chat_input("Type your message..."):
    st.session_state.last_topic = prompt  # remember it for sidebar buttons
    run_prompt(prompt)

# --- Sidebar button actions: use the last topic typed in chat ---
if explain_clicked:
    if st.session_state.last_topic.strip() == "":
        st.sidebar.warning("Please type a topic in the chat box first.")
    else:
        run_prompt(f"Explain {st.session_state.last_topic} in simple language for a beginner.")

if example_clicked:
    if st.session_state.last_topic.strip() == "":
        st.sidebar.warning("Please type a topic in the chat box first.")
    else:
        run_prompt(f"Give one simple real-life example of {st.session_state.last_topic}.")

if quiz_clicked:
    if st.session_state.last_topic.strip() == "":
        st.sidebar.warning("Please type a topic in the chat box first.")
    else:
        run_prompt(f"Create 5 MCQs on {st.session_state.last_topic} with answers.")

if ask_clicked:
    if st.session_state.last_topic.strip() == "":
        st.sidebar.warning("Please type a topic in the chat box first.")
    else:
        run_prompt(f"Tell me something interesting about {st.session_state.last_topic}.")