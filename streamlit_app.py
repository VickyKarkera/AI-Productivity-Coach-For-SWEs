import bs4
import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain.chains.retrieval import create_retrieval_chain 
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.llms import Ollama
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import InMemoryVectorStore
import warnings
warnings.filterwarnings("ignore")

st.title(" 🤖 Productivity Assistant For Software Engineers with RAG")
st.markdown("Tools: Langchain (🦜🔗), Python (🐍), Ollama 3.2 (🦙)")

if "vectors" not in st.session_state:
    st.session_state.embeddings = OllamaEmbeddings(model="llama3.2")
    st.session_state.loader = WebBaseLoader(
    web_paths=("https://arc.dev/talent-blog/time-management-skills/","https://arc.dev/talent-blog/continuous-learning-with-busy-developer-schedule/"),
    bs_kwargs={"parse_only":bs4.SoupStrainer(class_=("entry-title","entry-summary","entry-content entry-single clearfix"))},)
    st.session_state.web_documents = st.session_state.loader.load()
    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    st.session_state.web_documents = st.session_state.text_splitter.split_documents(st.session_state.web_documents)
    st.session_state.vectors = InMemoryVectorStore.from_documents(st.session_state.web_documents,st.session_state.embeddings)

llm = Ollama(model="llama3.2")

prompt_template = ChatPromptTemplate.from_template("""
You are an AI-Powered Productivity Coach designed specifically for software engineers.
Your goal is to help developers optimize their workflow, manage time effectively, improve focus, and avoid burnout. 
You provide expert-level insights on task management, debugging, code quality, focus strategies, and balancing deep work with meetings.
Answer the question presented and use the provided context supplied.
Summarize the problem in one sentence.  
Provide a structured, step-by-step solution with bullet points.                                                                                      
<context>
{context}                                         
</context>
Question: {input}""")


# Set a default model
if "ollama_model" not in st.session_state:
    st.session_state["ollama_model"] = "llama3.2"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

document_chain = create_stuff_documents_chain(llm,prompt_template)
retriever = st.session_state.vectors.as_retriever()
retrieval_chain = create_retrieval_chain(retriever,document_chain)

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Accept user input
if prompt := st.chat_input("How can I help you today"):
    # Add user message to chat history
    st.session_state.messages.append({"role":"user","content":prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)


    with st.chat_message("assistant"):
        response = retrieval_chain.invoke({"input":prompt})
        llm_response = response["answer"]
        st.markdown(llm_response)    

    st.session_state.messages.append({"role":"assistant","content":llm_response})