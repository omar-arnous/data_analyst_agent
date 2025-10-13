# Data Analyst Bot with LangChain + Ollama + Gradio

The bot will understand your data, clean it, analyze it, and generate reports for you

## Project Phases

### **Phase - 1: Project Idea**

Build an AI data analyst agent
His job is to:

- Read CSV Files (EX: Sales data)
- Analyze data and figure out the changes and directions
- Generate smart summary or report that explains results
- View results and upload files area using **Gradio**

### **Phase - 2: activate virtual environment and install main packages**

Install ollama locally from [Ollama Download Website](https://ollama.com/download)

1. Create a virtual environment

```bash
python -m venv myenv
source myenv/bin/activate  # Mac/Linux
myenv\Scripts\activate     # Windows
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

Key dependencies:

- `langchain`
- `langchain-community`
- `pandas`
- `gradio`

3. Run Llama3 locally

```bash
ollama run llama3
```

### **Phase - 3: Make first chain for text analysis**
