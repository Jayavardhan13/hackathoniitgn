import streamlit as st

st.title("Basic Streamlit App")


input_text = st.text_input("Enter something:")

if st.button("Submit"):
    st.write("You entered:", input_text)





from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings  


pdf_path = "signals.pdf"
loader_1 = PyPDFLoader(pdf_path)
documents_1 = loader_1.load()
texts_1 = [doc.page_content for doc in documents_1]
texts_1=str(texts_1)


pdf_path = "EML_report.pdf"
loader_2 = PyPDFLoader(pdf_path)
documents_2 = loader_2.load()
texts_2 = [doc.page_content for doc in documents_2]
texts_2=str(texts_2)


import chromadb
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="collection")
collection.add(
    documents=[texts_1,texts_2],  
    ids=["id1", "id2"]
)




results = collection.query(
    query_texts=[input_text],
    n_results=1
)
final_DB_content=results["documents"]



from langchain_community.tools import TavilySearchResults
import os

os.environ["TAVILY_API_KEY"] = "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"

tavily_tool = TavilySearchResults()
full_web_content=tavily_tool.run(input_text)

final_web_content=full_web_content[0]["content"]



from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature=0,
    groq_api_key="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",  
    model_name="llama-3.1-8b-instant"  
)



llm_input_text = f"Generate the best content for the question: '{input_text}',also consider the following sources: {final_web_content} and {final_DB_content} "



result= llm.invoke(llm_input_text)

st.subheader("Result of your query...")
st.write(result.content)