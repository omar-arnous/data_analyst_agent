import pandas as pd
import streamlit as st
from langchain.agents import initialize_agent
from langchain_core.prompts import PromptTemplate
# from langchain.chains import LLMChain
from langchain_ollama import OllamaLLM
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_experimental.tools import PythonREPLTool

st.title("🤖 Data Analyst Bot using LangChain and Ollama")

uploaded_file = st.file_uploader("📁 Choose a CSV file to analyze", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("📊 Data")
    st.dataframe(df.head())

    summary_text = df.describe().to_string()

    template = """
        You are an experienced data analyst. Analyze the following statistics and generate for me a smart summary that explains the changes and notes: {text}.
    """

    prompt = PromptTemplate.from_template(template)
    llm = OllamaLLM(model="llama3")
    chain = prompt | llm
    result = chain.invoke({"text": summary_text})

    st.write("🔍 Analyzing results...")
    st.write(result)

df = pd.read_csv("./data/sales_data.csv", encoding="latin1")

template = """
    You are an experienced data analyst. Analyze the following statistics and generate for me a smart summary that explains the changes and notes: {text}.
"""

prompt = PromptTemplate.from_template(template)

tools = [PythonREPLTool()]
llm = OllamaLLM(model="llama3")

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type="zero-shot-react-description",
    verbose=True
)

result = agent.run("read the sales_data.csv file and print the statistics summary between last 2 quarters")

# chain = LLMChain(llm=llm, prompt=prompt)
chain = prompt | llm

# result = chain.run({"text": "The latest quarter sales has been droped down by 12%"})
# result = chain.invoke({"text": "The latest quarter sales has been droped down by 12%"})
# result = chain.invoke({"text": summary_text})
print("=== Analyzing Sales ===")
print(result)


