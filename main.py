from tempfile import template
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_ollama import OllamaLLM

template = """
    You are an experienced data analyst. Analyze the following text {text}.
"""

prompt = PromptTemplate.from_template(template)
llm = OllamaLLM(model="llama3")

# chain = LLMChain(llm=llm, prompt=prompt)
chain = prompt | llm

# result = chain.run({"text": "The latest quarter sales has been droped down by 12%"})
result = chain.invoke({"text": "The latest quarter sales has been droped down by 12%"})
print(result)