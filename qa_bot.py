from langchain.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import gradio as gr
import os 

# load documents
loader = TextLoader('business_knowledge.txt')
docs = loader.load()

# create vector store
embeddings = HuggingFaceEmbeddings()
vector_store = FAISS.from_documents(docs, embeddings)

# create a retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# connect to orca mini
llm = Ollama(model="phi")

# create a prompt template
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a helpful business consultant. Use the following context to answer the question.

Context:
{context}

Question:
{question}

Answer clearly and professionally:
"""
)

# create a RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt_template}

)

# define the Gradio interface
def chatbot(query):
    if not query:
        return "Please enter a business-related question."
    result = qa_chain({"query": query})
    return result["result"] if "result" in result else str(result)

iface = gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(lines=2, placeholder="Ask a business question..."),
    outputs="text",
    title="Business Q&A Chatbot",
    description="Powered by Llama2 7B Chat and LangChain. Ask business-related questions based on a local knowledge base."
)

# launch the Gradio app
iface.launch(share=True)