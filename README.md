Multi-PDF Chatbot – Streamlit + LangChain + OpenAI

Chat with multiple PDFs in real-time using embeddings + retrieval + LLM responses.

This app allows users to upload multiple PDF documents, convert them into text, chunk the text, embed it, store embeddings in FAISS, and then chat with the content using GPT-3.5-Turbo (or newer models).

🚀 Features
✅ Upload and chat with multiple PDFs

Extracts text from every page in every file.

✅ Advanced RAG (Retrieval-Augmented Generation)

Uses:

CharacterTextSplitter

FAISS vector database

OpenAIEmbeddings

✅ Streaming Chat UI (Like ChatGPT)

Custom HTML + CSS
Fully scrollable chat window
Sticky bottom input bar

✅ Conversation Memory

Powered by:

StreamlitChatMessageHistory

RunnableWithMessageHistory

✅ Easy deployment

Can be deployed on:

Streamlit Cloud

Docker

EC2

Local environment

📦 Project Structure
📁 project/
│-- app.py
│-- requirements.txt
│-- htmlTemplates.py
│-- .env
│-- README.md

🔧 Setup Instructions
1️⃣ Install Dependencies

Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows


Install packages:

pip install -r requirements.txt

2️⃣ Add Your OpenAI API Key

Create a .env file:

OPENAI_API_KEY=your_api_key_here


Or set directly inside the script:

api_key="your_api_key_here"

3️⃣ Run the Application
streamlit run app.py


Streamlit will launch in your browser automatically.

🖥️ How It Works Internally
1. PDF → Text Extraction

Uses PdfReader to extract raw text from all uploaded PDFs.

2. Text Chunking

Splits text into overlapping chunks using:

CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

3. Embedding + VectorStore

Creates embeddings using:

OpenAIEmbeddings()


Stores vectors in FAISS:

FAISS.from_texts(chunks, embeddings)

4. Retrieval + Chat LLM

Builds a custom chain with:

GPT-3.5-Turbo

RAG context injection

Custom system prompt

Conversation history

🧠 Conversation Flow

User sends a query

App retrieves relevant text chunks

Injects into custom prompt

Model answers using ONLY document context

Chat history saved & displayed nicely

🎨 UI Features

Clean ChatGPT-like interface

Custom CSS templates in htmlTemplates.py

Auto-scrolling JS script

Sticky input bar at bottom

Separate chat bubbles for user & bot

📁 Uploading PDFs

You can upload:

Research papers

Contracts

Reports

Invoices

Books

Manuals

The bot only answers from what’s inside the PDFs.
