import pandas as pd
from langchain_core.prompts import PromptTemplate
# from langchain.chains import LLMChain
from langchain_ollama import OllamaLLM

df = pd.read_csv("./data/sales_data.csv", encoding="latin1")

summary_text = df.describe().to_string()

template = """
    You are an experienced data analyst. Analyze the following statistics and generate for me a smart summary that explains the changes and notes: {text}.
"""

prompt = PromptTemplate.from_template(template)
llm = OllamaLLM(model="llama3")

# chain = LLMChain(llm=llm, prompt=prompt)
chain = prompt | llm

# result = chain.run({"text": "The latest quarter sales has been droped down by 12%"})
# result = chain.invoke({"text": "The latest quarter sales has been droped down by 12%"})
result = chain.invoke({"text": summary_text})
print("=== Analyzing Sales ===")
print(result)