# chatbot using streamlit 
import langchain 
import os 
import openai
from langchain_community.llms import HuggingFaceHub
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage,SystemMessage,AIMessage
import streamlit as st 

#response generation: 
def response(question):
    llm = OpenAI(model ="gpt-3.5-turbo-instruct", api_key = os.environ['openai_api_key'],temperature = 0.7 )
    response = llm.invoke(question)
    return response

# streamlit 
st.set_page_config(page_title="Cookbook")
st.header('Chatbot')

input = st.text_input("input: ", key ="input")
output = response(input)

submit =st.button("Generate response")

if submit:
    st.subheader("The response is")
    st.write(output)
