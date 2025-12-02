



api_key="your_openai_api_key_here"








import os
import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader

from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
from io import BytesIO

from htmlTemplates import css, bot_template, user_template, chat_container_css, scroll_script

# ---------------------------------------------------------
# Load API key
# ---------------------------------------------------------
load_dotenv()


if not api_key:
    st.error("❌ Please set your OPENAI_API_KEY in a .env file")
    st.stop()


# ---------------------------------------------------------
# Extract text from PDFs
# ---------------------------------------------------------
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        reader = PdfReader(BytesIO(pdf.read()))
        for page in reader.pages:
            text += page.extract_text() or ""
    return text


# ---------------------------------------------------------
# Split into chunks
# ---------------------------------------------------------
def get_text_chunks(text):
    splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=200
    )
    return splitter.split_text(text)


# ---------------------------------------------------------
# Build vectorstore
# ---------------------------------------------------------
def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    return FAISS.from_texts(text_chunks, embeddings)


# ---------------------------------------------------------
# Conversation chain
# ---------------------------------------------------------
def get_conversation_chain(vectorstore):
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=api_key
    )

    retriever = vectorstore.as_retriever()

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Use only the provided documents."),
        ("human", "Question: {question}\n\nRelevant context:\n{context}")
    ])

    chain = (
        {
            "context": lambda x: retriever.invoke(x["question"]),
            "question": lambda x: x["question"]
        }
        | prompt
        | llm
    )

    def get_history(_):
        if "history" not in st.session_state:
            st.session_state["history"] = StreamlitChatMessageHistory(key="history")
        return st.session_state["history"]

    return RunnableWithMessageHistory(
        chain,
        get_history,
        input_messages_key="question",
        history_messages_key="history"
    )


# ---------------------------------------------------------
# Handle user input
# ---------------------------------------------------------
def handle_userinput(q):
    st.session_state.conversation.invoke(
        {"question": q},
        config={"configurable": {"session_id": "session"}}
    )


# ---------------------------------------------------------
# Streamlit UI
# ---------------------------------------------------------
def main():
    st.set_page_config(page_title="Chat with PDFs", page_icon="📚", layout="wide")

    st.write(css, unsafe_allow_html=True)
    st.write(chat_container_css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    st.title("📚 Chat with Multiple PDFs")

    # -----------------------------------------------
    # CHAT WINDOW (scrollable)
    # -----------------------------------------------
    chat_placeholder = st.container()
    with chat_placeholder:
        st.markdown('<div id="chat-box" class="chat-box">', unsafe_allow_html=True)

        if "history" in st.session_state:
            for msg in st.session_state["history"].messages:
                if isinstance(msg, HumanMessage):
                    st.write(user_template.replace("{{MSG}}", msg.content), unsafe_allow_html=True)
                else:
                    st.write(bot_template.replace("{{MSG}}", msg.content), unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    # -----------------------------------------------
    # FLOATING INPUT BAR (fixed bottom)
    # -----------------------------------------------
    st.markdown(
        """
        <div class="input-bar">
            <div class="input-inner">
        """,
        unsafe_allow_html=True
    )

    user_input = st.chat_input("Type your message…")

    if user_input and st.session_state.conversation:
        handle_userinput(user_input)
        st.rerun()


    st.markdown("</div></div>", unsafe_allow_html=True)

    # Auto-scroll JS
    st.markdown(scroll_script, unsafe_allow_html=True)

    # -----------------------------------------------
    # Sidebar
    # -----------------------------------------------
    with st.sidebar:
        st.subheader("📄 Upload Your PDFs")
        docs = st.file_uploader("Upload PDF files", accept_multiple_files=True)

        if st.button("Process PDFs"):
            if not docs:
                st.warning("Upload at least one PDF!")
                return

            with st.spinner("Processing PDFs…"):
                text = get_pdf_text(docs)
                chunks = get_text_chunks(text)
                vectorstore = get_vectorstore(chunks)

                st.session_state.conversation = get_conversation_chain(vectorstore)
                st.session_state["history"] = StreamlitChatMessageHistory(key="history")

            st.success("Done! Start chatting.")


if __name__ == "__main__":
    main()
