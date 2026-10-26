# RAG Knowledge Assistant

A document-based question-answering application built with Python, Streamlit, LangChain, Google's Gemini models, and FAISS.

## Features

- Upload PDF and DOCX documents
- Split documents into smaller chunks
- Generate embeddings using Gemini
- Store and retrieve relevant chunks using FAISS
- Ask questions about uploaded documents using Gemini

## Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini API
- FAISS
- PyPDF and docx2txt

## Local Setup

1. Clone this repository.
2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Create a `.env` file based on `.env.example` and add your Gemini API key.

5. Start the application:

   ```bash
   python -m streamlit run app.py
   ```

## Configuration

- `GEMINI_API_KEY`: Google Gemini API key
- `EMBEDDING_MODEL`: Embedding model (default: `gemini-embedding-001`)
- `GEMINI_CHAT_MODEL`: Chat model (default: `gemini-2.5-flash`)

Never commit your API key or other secrets to GitHub.

## Notes

Uploaded documents and generated vector indexes are excluded from this repository. Upload documents and build the knowledge base in the running application.

## License

Add a license if you intend to distribute this project for reuse.
