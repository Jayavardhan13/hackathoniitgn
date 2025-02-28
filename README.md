# hackathoniitgn

# 🚀 AI-Powered Document Search for MoSPI  

## 📌 Problem Statement  
Manual search within documents **impacts the overall efficiency** of operations at MoSPI. Our solution automates and optimizes document retrieval using **AI-driven techniques**.  

---

## ✅ Our Approach  
We have developed a **scalable AI-powered system** that enhances document search. Here’s how it works:  

### 1️⃣ Extracting Text from Documents  
- Extracts text from **PDFs and DOCs** and stores it in a structured **vector database (ChromaDB)**.  
- For **scanned images or handwritten text**, we use **OCR (Tesseract)** to extract meaningful text.  

### 2️⃣ Identifying the Best Document  
- Uses **ChromaDB** to intelligently **retrieve the most relevant document** based on the search query.  

### 3️⃣ Integrating Web Search  
- Fetches additional relevant information using **Tavily web search** to supplement the database results.  

### 4️⃣ Leveraging LLM for Enhanced Search  
- **Combines** the best-matching document from **ChromaDB** and **Tavily web search results** as input to a **Large Language Model (LLM)**.  
- Processes the **user query** and generates **accurate, contextual responses**.  

### 5️⃣ Seamless Integration with LangChain  
- The entire pipeline is **built within LangChain**, ensuring **efficient orchestration** of retrieval, processing, and AI-driven responses.  

---

## 🎯 Why Our Solution?  
✅ **Speeds up search operations** 🔍🚀  
✅ **Reduces manual effort** by automating document retrieval  
✅ **Enhances accuracy** with AI-powered search  
✅ **Integrates ChromaDB, Tavily, Tesseract, and LLM seamlessly with LangChain**  

---


## 🛠️ Tech Stack  
| Technology | Purpose |
|------------|---------|
| **Python** | Core programming language |
| **LangChain** | AI workflow orchestration |
| **ChromaDB** | Vector database for storing and retrieving documents |
| **Tavily API** | Web search integration |
| **llama-3.1-8b-instant LLM** | Processing user queries and generating responses |
| **Streamlit** | Simple UI for interacting with the system |
| **Tesseract OCR** | Extracting text from scanned images and handwritten text | ( to be added )
| **Docker** | Containerization for easy deployment | ( to be added )
