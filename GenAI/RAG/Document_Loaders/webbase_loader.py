


from langchain_community.document_loaders import WebBaseLoader 


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
    template = 'Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question' , 'text']
)

parser = StrOutputParser()


url = 'https://www.geeksforgeeks.org/html/static-websites/'

loader  = WebBaseLoader(url)

docs = loader.load()



chain = prompt | model | parser 

result = chain.invoke({'question' : 'what is the main idea of this content' , 'text' : docs[0].page_content})

print(result)