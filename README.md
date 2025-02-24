# **🤖 AI Productivity Assistant for Software Engineers with RAG**  
🚀 **Built using LangChain, Ollama (Llama 3.2), and Streamlit**  

This AI-powered chatbot helps software engineers **optimize workflow, manage tasks, improve focus, and prevent burnout** using **RAG (Retrieval-Augmented Generation)**. It leverages **LLMs (Llama 3.2 via Ollama), NLP, and document retrieval** to provide **structured, actionable advice** based on real-world best practices.  

---

## **📌 Features**
✅ **Retrieval-Augmented Generation (RAG):** Retrieves **productivity tips** from trusted online sources and enhances responses with AI.  
✅ **Task & Time Management:** Helps engineers **break down tasks, set goals, and use focus techniques (Pomodoro, Deep Work, Flow State)**.  
✅ **Code Review & Debugging Tips:** Provides **best practices for clean, optimized code** and debugging strategies.  
✅ **Distraction & Burnout Management:** Identifies **work patterns, suggests breaks, and optimizes deep work vs. meetings**.  
✅ **Chat History & Context Awareness:** Remembers previous messages for **personalized, continuous assistance**.  

---

## **🛠️ Tech Stack**
- **🦜 LangChain** – For AI pipeline & retrieval  
- **🦙 Ollama (Llama 3.2)** – Local LLM processing  
- **🐍 Python** – Core backend logic  
- **📜 Streamlit** – Frontend UI for interactive chatbot  
- **🔍 WebBaseLoader** – Loads articles for RAG-based knowledge  
- **🛠 RecursiveCharacterTextSplitter** – Prepares text for efficient embeddings  

---

## **🚀 Installation & Setup**
### **1️⃣ Install Dependencies**
Ensure you have **Python 3.8+** installed, then run:  
```bash
pip install streamlit langchain langchain_community ollama bs4
```

### **2️⃣ Install & Set Up Ollama**
Ollama is required to run the **Llama 3.2 model locally**. Install it:  
```bash
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull llama3.2
```

### **3️⃣ Run the Streamlit App**
```bash
streamlit run streamlit_app.py
```
The app will open in your browser at: **http://localhost:8501**  

---

## **📜 How It Works**
1. **Loads Productivity Data**  
   - Uses `WebBaseLoader` to scrape content from blogs like **Arc.dev**.  
   - Processes data using `RecursiveCharacterTextSplitter`.  
   - Stores **vector embeddings in InMemoryVectorStore** for efficient retrieval.  

2. **Retrieval-Augmented Generation (RAG) Workflow**  
   - **User asks a question** (e.g., *"How do I improve focus while coding?"*).  
   - **Retriever searches knowledge base** for relevant productivity tips.  
   - **LLM generates a response** based on retrieved context.  
   - **User gets structured, step-by-step recommendations.**  

3. **Chat History & Context Retention**  
   - Messages are stored in **`st.session_state.messages`**.  
   - Ensures a **smooth, personalized conversation flow**.  

---

## **🎯 Example Prompts & Responses**
### **User:** *"How can I stay focused while coding?"*  
### **AI Response:**  
📌 **Problem Summary:** You’re struggling with distractions while coding.  
✅ **Step-by-Step Solution:**  
- Use the **Pomodoro Technique** (25 min focus, 5 min break).  
- Block distractions using **Cold Turkey, RescueTime, or Freedom App**.  
- Enable **Do Not Disturb mode** on Slack & phone.  
- Schedule **Deep Work blocks** in your calendar.  
💡 **Extra Tip:** If you like background noise, try **brown noise playlists** for focus.  

---

## **📌 Credits & Acknowledgments**
- **LangChain & Ollama** for the **LLM-powered AI processing**.  
- **Arc.dev blog sources** for **productivity best practices**.  
- **Streamlit Community** for **UI & deployment guidance**.  

---

This README provides a **clear project overview, installation guide, features, and next steps**—let me know if you'd like to refine any section! 🚀
