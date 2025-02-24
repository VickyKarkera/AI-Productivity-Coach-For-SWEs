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


if "vectors" not in st.session_state:
    st.session_state.embeddings = OllamaEmbeddings(model="llama3.2")
    st.session_state.loader = WebBaseLoader(
    web_paths=("https://arc.dev/talent-blog/time-management-skills/","https://arc.dev/talent-blog/continuous-learning-with-busy-developer-schedule/"),
    bs_kwargs={"parse_only":bs4.SoupStrainer(class_=("entry-title","entry-summary","entry-content entry-single clearfix"))},)
    st.session_state.web_documents = st.session_state.loader.load()
    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    st.session_state.web_documents = st.session_state.text_splitter.split_documents(st.session_state.web_documents)
    st.session_state.vectors = InMemoryVectorStore.from_documents(st.session_state.web_documents,st.session_state.embeddings)

st.title("AI Productivity Assistant For Software Engineers")
llm = Ollama(model="llama3.2")

prompt = ChatPromptTemplate.from_template("""
You are an AI Productivity Assistant for Software Engineers.
Answer the question presented based only on the provided context.
Please provide the most accurate response based on the question.                                                                                    
<context>
{context}                                         
</context>
Question: {input}""")

document_chain = create_stuff_documents_chain(llm,prompt)
retriever = st.session_state.vectors.as_retriever()
retrieval_chain = create_retrieval_chain(retriever,document_chain)

prompt = st.text_input("How can I help you today?")

if prompt:
    response = retrieval_chain.invoke({"input":prompt})
    st.write(response["answer"])
