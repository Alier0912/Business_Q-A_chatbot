# Business Q&A Chatbot

A local, privacy-preserving business question-answering chatbot powered by [LangChain](https://github.com/langchain-ai/langchain), [Ollama](https://ollama.com/), and [Gradio](https://gradio.app/). This chatbot leverages a custom business knowledge base and advanced language models to provide clear, professional answers to business-related questions.

---

## Features

- **Private & Local**: All data and models run locally—no data leaves your machine.
- **Custom Knowledge Base**: Answers are grounded in your own business knowledge, loaded from `business_knowledge.txt`.
- **Modern LLM Integration**: Uses Ollama to run the `phi` model (or other supported models).
- **Semantic Search**: Employs vector search (FAISS + HuggingFace embeddings) for relevant context retrieval.
- **Conversational UI**: Clean, user-friendly web interface via Gradio.

---

## Project Structure

```
business_knowledge.txt         # Your business knowledge base (plain text)
qa_bot.py                     # Main application script
.gradio/
    certificate.pem           # SSL certificate for Gradio (if needed)
```

---

## Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running locally
- Required Python packages (see below)

---

## Installation

1. **Clone the repository**  
   ```sh
   git clone <your-repo-url>
   cd Business_Q&A_chatbot
   ```

2. **Install dependencies**  
   It is recommended to use a virtual environment.
   ```sh
   pip install langchain gradio faiss-cpu sentence-transformers
   ```

3. **Install and run Ollama**  
   - [Download and install Ollama](https://ollama.com/download)
   - Pull the required model (e.g., `phi`):
     ```sh
     ollama pull phi
     ```
   - Start the Ollama server (usually runs automatically).

4. **Prepare your knowledge base**  
   - Edit `business_knowledge.txt` and add your business information, FAQs, policies, etc.

---

## Usage

Run the chatbot with:

```sh
python qa_bot.py
```

- The Gradio web interface will launch (by default at `http://localhost:7860`).
- If `share=True` is set in the script, a public link will also be generated.

---

## How It Works

1. **Document Loading**: Loads your business knowledge from `business_knowledge.txt`.
2. **Embedding & Indexing**: Converts documents to embeddings using HuggingFace models and indexes them with FAISS.
3. **Retrieval**: For each user question, retrieves the top relevant context chunks.
4. **Prompting**: Constructs a prompt with the retrieved context and user question.
5. **LLM Response**: Sends the prompt to the local Ollama LLM for a professional, context-aware answer.
6. **UI**: Presents the answer in a simple Gradio web app.

---

## Customization

- **Change the LLM**:  
  Modify the `Ollama(model="phi")` line in [`qa_bot.py`](qa_bot.py) to use another supported model (e.g., `"llama2"`, `"mistral"`, etc.).
- **Tune Retrieval**:  
  Adjust `search_kwargs={"k": 3}` to retrieve more or fewer context chunks.
- **Prompt Engineering**:  
  Edit the `PromptTemplate` in [`qa_bot.py`](qa_bot.py) to change the assistant's tone or instructions.

---

## Security & Privacy

- All processing is local.
- No data is sent to external servers.
- SSL certificate (`.gradio/certificate.pem`) can be used for HTTPS if desired.

---

## Troubleshooting

- **Ollama not running**:  
  Ensure the Ollama server is running and the required model is pulled.
- **Missing dependencies**:  
  Double-check that all Python packages are installed.
- **Gradio not launching**:  
  Check for port conflicts or firewall issues.

---

## License

This project is for educational and internal business use. See [LICENSE](LICENSE) for details.

---

## Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [Ollama](https://ollama.com/)
- [Gradio](https://gradio.app/)
- [FAISS](https://github.com/facebookresearch/faiss)
