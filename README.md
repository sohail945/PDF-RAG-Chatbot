# PDF Chatbot

## Overview
**PDF Chatbot** allows users to upload PDF documents, ask questions, and get answers based on the content of the document. It uses **text embeddings** and **retrieval-based question answering** (RQA) with **FAISS indexing** to provide relevant responses. The chatbot is powered by **OpenAI's GPT-3.5** model for generating answers to user queries.

## Features
- **Upload PDF**: Upload any PDF document.
- **Question Answering**: Ask questions related to the document and get accurate answers.
- **Conversation History**: Log of past questions and answers.
- **OpenAI Integration**: Powered by OpenAI's GPT-3.5 for generating answers.

## Prerequisites
Before running the project locally, ensure you have the following:
- Python 3.7 or higher
- **OpenAI API key** (You will need to provide this in the `.env` file)

## Setup Instructions

1. **Clone the Repository**  
   To get started, clone the repository to your local machine:
   ```bash
   git clone <repository_url>
   cd pdf-chatbot

2. ```bash
   pip install -r requirements.txt

3. **Run the App**
   ```bash
   streamlit run app.py

### Example Usage
- **Upload your PDF: Click the upload button to choose your PDF document.**
- **Ask Questions: After uploading, ask questions like:**
- **"What is the summary of this document?"**
- **"Explain the main points of chapter 3."**
- **View Answer: The chatbot provides an answer based on the document's content.**

### Complete Steps:
- **Clone the repo**
- **Install dependencies**
- **Set up environment variables**
- **Run Streamlit app**

Each step in this version is grouped under one heading, with all the relevant code for execution.

Replace `<repository_url>` with your actual repository URL, and it should be ready for you!

Let me know if you need anything else!