# from langchain_core.documents import Document

# file_path = r"C:\Users\ANUBHAV\Program_Folders\AI\GenAI\RAG\Document_Loaders\Datasets\cricket.txt"

# with open(file_path, "r", encoding="utf-8") as file:
#     text = file.read()

# docs = [Document(page_content=text)]

# print(docs)



# ______________________________________________________________________________________________________



# :: using with LLm :  





from langchain_core.documents import Document

from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser


load_dotenv() 


llm = HuggingFaceEndpoint(
    repo_id='openai/gpt-oss-20b',
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)



prompt = PromptTemplate(
    template = 'Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

file_path = r"C:\Users\ANUBHAV\Program_Folders\AI\GenAI\RAG\Document_Loaders\Datasets\cricket.txt"

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()



docs = [Document(page_content=text)]

print(docs)



chain = prompt | model | parser 


result = chain.invoke({'poem' : docs[0].page_content})

print(result)
