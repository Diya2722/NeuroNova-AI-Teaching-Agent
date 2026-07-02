# 🧠 NeuroNova — AI Teaching Agent

NeuroNova is an interactive AI-powered teaching assistant built with **Streamlit** and **Google Gemini**. It helps learners understand any topic through simple explanations, real-life examples, auto-generated quizzes, and open-ended Q&A — all inside a clean chat interface.

Built as part of the **Infosys Springboard AI Empower(Her)** program.

---

## ✨ Features

- **📘 Explain Concept** — Get a simple, beginner-friendly explanation of any topic
- **🌍 Real-Life Example** — See how the concept applies in everyday situations
- **❓ Generate Quiz** — Auto-generate 5 MCQs to test your understanding, with correct answers provided
- **💬 Ask Anything** — Free-form chat to ask follow-up questions
- Clean sidebar navigation with persistent chat history

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) — frontend & app framework
- [Google Generative AI (Gemini 2.5 Flash)](https://ai.google.dev/) — language model powering responses
- Python 3.13

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Diya2722/NeuroNova-AI-Teaching-Agent.git
cd NeuroNova-AI-Teaching-Agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your Gemini API key

Create a `.streamlit/secrets.toml` file in the project root:

```toml
GEMINI_API_KEY = "your_api_key_here"
```

> Get a free API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 4. Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## 📂 Project Structure

```
NeuroNova-AI-Teaching-Agent/
├── .streamlit/
│   └── secrets.toml       # API key (not committed to git)
├── app.py                 # Main Streamlit app
├── requirements.txt       # Python dependencies
└── README.md
```

---

## 🌐 Live Demo

🔗 [Add your deployed Streamlit Cloud link here]

---

## 📌 Note

Never commit your `secrets.toml` file or expose your API key publicly. This repo's `.gitignore` excludes it by default.

---

## 🙋‍♀️ Author

**Diya Prajapati**

- GitHub: [@Diya2722](https://github.com/Diya2722)
- LinkedIn: [Diya Prajapati](https://linkedin.com/in/diya-prajapati-258a27275)

---

## 📄 License

This project is open source and available for educational use.
# NeuroNova-AI-Teaching-Agent
