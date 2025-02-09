import streamlit as st
from pdf_loader import load_pdf, split_text
from utils import embed_chunks, create_faiss_index
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set page configuration
st.set_page_config(
    page_title="PDF Chatbot",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Initialize conversation history in session state
if "conversation_history" not in st.session_state:
    st.session_state["conversation_history"] = []

# Main Page Title and Instructions
st.title("📄 Chat with Your PDF")
st.markdown("""
    Upload your **PDF document** below, and ask questions to extract valuable insights.
""")

# File uploader for PDF
uploaded_file = st.file_uploader(
    "📂 Upload your PDF file:",
    type="pdf",
    help="Only PDF files are supported.",
)

if uploaded_file:
    # Save the uploaded file temporarily
    file_path = f"temp_{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    # Load and process the PDF
    try:
        pdf_text = load_pdf(file_path)
        text_chunks = split_text(pdf_text)
    except Exception as e:
        st.error(f"❌ Error reading PDF: {e}")
        st.stop()

    # Embed text chunks and create FAISS index
    try:
        embeddings = embed_chunks(text_chunks)
        faiss_index = create_faiss_index(text_chunks)
    except Exception as e:
        st.error(f"❌ Error creating embeddings or index: {e}")
        st.stop()

    # Set up OpenAI LLM
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        st.error("❌ OpenAI API key not found. Please add it to the `.env` file.")
        st.stop()

    llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)

    # Set up the RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=faiss_index.as_retriever(),
        chain_type="stuff"
    )

    # User input for questions
    st.subheader("💬 Ask Questions About the Document")
    question = st.text_input(
        "Type your question below:",
        placeholder="e.g., What is the summary of the document?",
    )

    if question:
        try:
            # Prepare context: Get the last 8 interactions (question + answer)
            context = ""
            for entry in st.session_state["conversation_history"][-8:]:  # Last 8 interactions
                context += f"User: {entry['user']}\nBot: {entry['bot']}\n\n"

            # Combine context with the current question
            full_input = context + f"User: {question}\nBot:"

            # Get the answer from the model using the full context
            answer = qa_chain.run(full_input)

            if answer.strip():  # If the answer is not empty or blank
                st.write(f"**Answer:** {answer}")  # Default styling
                # Add question and answer to conversation history
                st.session_state["conversation_history"].append({"user": question, "bot": answer})
            else:
                st.error("❌ No answer could be generated. Please try rephrasing your question.")
        except Exception as e:
            st.error(f"❌ Error generating answer: {e}")

# Display the full conversation history
if st.session_state["conversation_history"]:
    st.subheader("📝 Conversation History:")
    for i, entry in enumerate(st.session_state["conversation_history"]):
        st.chat_message("user").write(entry["user"])
        st.chat_message("assistant").write(entry["bot"])

# Footer
st.markdown("""
---
**PDF Chatbot** | Powered by [Sohail](https://abc...com)
""")
