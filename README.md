📚🤖 Multi-PDF Chatbot – Streamlit + LangChain + OpenAI








Multi-PDF Chatbot allows users to chat with multiple PDF documents in real-time. Using embeddings, retrieval, and LLM responses, it transforms static PDFs into an interactive knowledge base. Ideal for research, contracts, manuals, or any document-heavy workflow.

🚀 Features

📄 Upload & Chat with Multiple PDFs
Extracts text from every page of each file and allows real-time conversation.

🧠 Advanced RAG (Retrieval-Augmented Generation)

CharacterTextSplitter for text chunking

FAISS vector database for fast similarity search

OpenAI embeddings for semantic understanding

💬 Streaming Chat UI (ChatGPT-Like)

Fully scrollable chat window

Sticky bottom input bar

User & bot chat bubbles

🗃️ Conversation Memory

StreamlitChatMessageHistory & RunnableWithMessageHistory

Maintains chat context for multi-turn conversations



Local environments

🛠 Tech Stack
<p> <a href="https://www.python.org/" target="_blank"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="40" height="40" alt="Python"/></a> <a href="https://streamlit.io/" target="_blank"><img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" width="40" height="40" alt="Streamlit"/></a> <a href="https://www.langchain.com/" target="_blank"><img src="https://raw.githubusercontent.com/langchain-ai/brand/main/langchain-icon.svg" width="40" height="40" alt="LangChain"/></a> <a href="https://openai.com/" target="_blank"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/openai/openai-original.svg" width="40" height="40" alt="OpenAI"/></a> <a href="https://faiss.ai/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/7/7d/FAISS_logo.png" width="40" height="40" alt="FAISS"/></a> </p>
📦 Project Structure
project/
│-- app.py
│-- requirements.txt
│-- htmlTemplates.py
│-- .env
│-- README.md

🔧 Setup Instructions

1️⃣ Install Dependencies

# Create virtual environment
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows

# Install packages
pip install -r requirements.txt


2️⃣ Add Your OpenAI API Key

Create .env file:

OPENAI_API_KEY=your_api_key_here


Or set directly in app.py:

api_key = "your_api_key_here"


3️⃣ Run the Application

streamlit run app.py


Streamlit will launch automatically in your browser.

🖥️ How It Works

PDF → Text Extraction: PdfReader extracts text from all PDFs

Text Chunking: CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

Embedding + VectorStore:

OpenAIEmbeddings()

Stored in FAISS: FAISS.from_texts(chunks, embeddings)

Retrieval + LLM Chat:

GPT-3.5-Turbo with RAG context

Custom system prompt

Conversation history maintained

Conversation Flow:

User query → Relevant PDF chunks retrieved → Context injected → Model answers only from PDFs → Chat history displayed

🎨 UI Features

ChatGPT-like clean interface

Custom CSS templates in htmlTemplates.py

Auto-scrolling chat window

Sticky input bar at bottom

Separate user & bot chat bubbles

📁 Supported PDF Types

Research papers

Contracts & reports

Invoices & manuals

Books

Any document you want to query

The bot answers only based on uploaded PDFs.

📷 Screenshots
![Home Page](/images/UploadPDF.png)
![Chat Window](/images/ChatWithPDF.png)


(Replace paths with your actual images folder)
