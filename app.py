




# import os
# import streamlit as st
# from dotenv import load_dotenv
# from pypdf import PdfReader

# from langchain_text_splitters import CharacterTextSplitter
# from langchain_openai import ChatOpenAI, OpenAIEmbeddings
# from langchain_community.vectorstores import FAISS
# from langchain_community.chat_message_histories import StreamlitChatMessageHistory
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.runnables.history import RunnableWithMessageHistory
# from langchain_core.messages import HumanMessage, AIMessage
# from io import BytesIO
# from htmlTemplates import css, bot_template, user_template
# from langchain_openai import ChatOpenAI
# # ---------------------------------------------------------
# # Load OpenAI API key from .env
# # ---------------------------------------------------------
# load_dotenv()

# # api_key = "ssk-proj-gR-t0Vzx8keN9qj_ZgH3RDqNCK_x3KUxI3HI7m5_8nugYiNa1DQZA1GtZ2ubuh174h4c-qGI38T3BlbkFJdlw-GEP4Gko-oDh_RR65NssFt3p5OgVuM_HWSSap-bcWnOHwT52pfd7yLUCKYS-HpwQuV0GygA"
api_key="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"

# #OPENAI_API_KEY ="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"
# if not api_key:
#     st.error("❌ Please set your OPENAI_API_KEY in a .env file")
#     st.stop()

# # ---------------------------------------------------------
# # Extract PDF Text
# # ---------------------------------------------------------
# def get_pdf_text(pdf_docs):
#     text = ""
#     for pdf in pdf_docs:
#        # reader = PdfReader(pdf)
#               # Use the stream from the uploaded file
#        # reader = PdfReader(pdf.stream)
#         reader = PdfReader(BytesIO(pdf.read()))
#         print(reader)
#         for page in reader.pages:
#             page_text = page.extract_text() or ""
#             text += page_text
#     return text

# # ---------------------------------------------------------
# # Split text into chunks
# # ---------------------------------------------------------
# def get_text_chunks(text):
#     splitter = CharacterTextSplitter(
#         separator="\n",
#         chunk_size=1000,
#         chunk_overlap=200
#     )
#     return splitter.split_text(text)

# # ---------------------------------------------------------
# # Build FAISS vectorstore
# # ---------------------------------------------------------
# def get_vectorstore(text_chunks):
#     embeddings = OpenAIEmbeddings(openai_api_key=api_key)
#     vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
#     return vectorstore






# def get_conversation_chain(vectorstore):
#     llm = ChatOpenAI(
#     model_name="gpt-3.5-turbo",  # cheaper than GPT-4
#     temperature=0,
#     openai_api_key=api_key
# )
#     retriever = vectorstore.as_retriever()

#     prompt = ChatPromptTemplate.from_messages([
#         (
#             "system",
#             "You are a helpful assistant. Use the provided context to answer the user's question.\n"
#             "If the answer is not contained in the documents, say so."
#         ),
#         ("human", "Question: {question}\n\nRelevant context:\n{context}")
#     ])

#     # FINAL FIX: retriever.invoke returns a dict, so extract "documents"
#     chain = (
#         {
#             "context": lambda x: retriever.invoke(x["question"]),
#             "question": lambda x: x["question"],
#         }
#         | prompt
#         | llm
#     )

#     def get_history(session_id):
#         if "history" not in st.session_state:
#             st.session_state["history"] = StreamlitChatMessageHistory(key="history")
#         return st.session_state["history"]

#     conversation = RunnableWithMessageHistory(
#         chain,
#         get_history,
#         input_messages_key="question",
#         history_messages_key="history"
#     )

#     return conversation




# # ---------------------------------------------------------
# # Handle user messages
# # ---------------------------------------------------------
# def handle_userinput(user_question):
#     response = st.session_state.conversation.invoke(
#         {"question": user_question},
#         config={"configurable": {"session_id": "user"}}
#     )

#     # history = st.session_state["history"].messages
#     # print(history)
#     # for msg in history:
#     #     if isinstance(msg, HumanMessage):
#     #         st.write(
#     #             user_template.replace("{{MSG}}", msg.content),
#     #             unsafe_allow_html=True
#     #         )
#     #     elif isinstance(msg, AIMessage):
#     #         st.write(
#     #             bot_template.replace("{{MSG}}", msg.content),
#     #             unsafe_allow_html=True
#     #         )

# # ---------------------------------------------------------
# # Streamlit App UI
# # ---------------------------------------------------------
# def main():
#     st.set_page_config(page_title="Chat with multiple PDFs", page_icon="📚")
#     st.write(css, unsafe_allow_html=True)

#     if "conversation" not in st.session_state:
#         st.session_state.conversation = None

#     st.header("Chat with multiple PDFs 📚")
    
    
#     user_question = st.text_input("Ask a question about your documents:")

#     if user_question and st.session_state.conversation:
#         handle_userinput(user_question)

#     chat_container=st.container()


#     with chat_container:
#         if "history" in st.session_state:
#             messages = st.session_state["history"].messages

#             for msg in reversed(messages): #ewest closest to input box
#                 if isinstance(msg, HumanMessage):
#                     st.write(user_template.replace("{{MSG}}", msg.content), unsafe_allow_html=True)
#                 elif isinstance(msg, AIMessage):
#                     st.write(bot_template.replace("{{MSG}}", msg.content), unsafe_allow_html=True)

    
    
   

#     # Sidebar
#     with st.sidebar:
#         st.subheader("Your documents")
#         pdf_docs = st.file_uploader(
#             "Upload your PDFs here",
#             accept_multiple_files=True
#         )

#         if st.button("Process"):
#             if not pdf_docs:
#                 st.warning("Please upload at least one PDF.")
#                 return

#             with st.spinner("Processing your documents..."):
#                 # Read PDFs
#                 raw_text = get_pdf_text(pdf_docs)
#                 print("raw_text",raw_text)
#                 # Split text
#                 chunks = get_text_chunks(raw_text)
#                 print("Chunks",chunks)

#                 # Create vectorstore
#                 vectorstore = get_vectorstore(chunks)
#                 print(vectorstore)
#                 # Create conversational chain
#                 st.session_state.conversation = get_conversation_chain(vectorstore)

#             st.success("Processing complete! You can now ask questions.")

# if __name__ == "__main__":
#     main()





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
