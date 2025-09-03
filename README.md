# 📄 Ollama PDF Q&A + Summarizer  

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit)](https://streamlit.io/)  
[![Docker](https://img.shields.io/badge/Container-Docker-blue?logo=docker)](https://www.docker.com/)  
[![Ollama](https://img.shields.io/badge/LLM-Ollama-black?logo=ai)](https://ollama.ai/)  
[![TinyLlama](https://img.shields.io/badge/Model-TinyLlama-green)](https://huggingface.co/TinyLlama)  

> ⚡ An **AI-powered PDF Question-Answering and Summarization app** built with **Streamlit** and **Ollama (TinyLlama)**.  
> Upload a PDF, ask questions, and get instant AI-generated answers + summaries.  

---

## 🚀 Features  
✅ Upload any PDF document  
✅ Ask **questions** about the document  
✅ Get **summaries** powered by TinyLlama  
✅ Modern **Streamlit web UI**  
✅ Dockerized for easy deployment  

---

## 🛠️ Tech Stack  
- **Backend (LLM)** → [Ollama](https://ollama.ai/) (TinyLlama model)  
- **Frontend** → [Streamlit](https://streamlit.io/)  
- **Containerization** → [Docker](https://www.docker.com/)  
- **Language** → Python 3.10+  

---

## 📂 Project Structure  
```bash
├── pdfSummary.py       # Main Streamlit app
├── requirements.txt    # Python dependencies
├── start.sh            # Startup script (Ollama + Streamlit)
├── Dockerfile          # Container setup
├── notes.txt           # Dev notes
└── README.md           # Project docs

🔹 Run Locally
# 1. Install Ollama
curl https://ollama.ai/install.sh | sh

# 2. Pull TinyLlama model
ollama pull tinyllama

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the app
streamlit run pdfSummary.py --server.port 8501 --server.address 0.0.0.0

🔹 Run with Docker
# 1. Build Docker image
docker build -t ollama_pdf_app .

# 2. Run the container
docker run -p 8501:8501 ollama_pdf_app

🎯 Use Cases

Showcasing LLM integration skills in portfolio

Building AI-powered PDF assistants

Demonstrating document Q&A systems

📸 Demo

👉 Add screenshots of your app here
👉 Optional: embed a demo video/GIF

💡 Future Improvements

Support for larger models (Mistral, Llama 3)

Free lightweight demo via Render / Railway / Hugging Face Spaces

Enhanced UI/UX with chat-like interface

👨‍💻 Author

Vikas Gautam
