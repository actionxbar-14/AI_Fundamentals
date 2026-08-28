


from langchain_core.messages import SystemMessage , HumanMessage , AIMessage 


# :--> HumanMessage :  the chat which user write and sent to the AI. 
# :--> AIMessage :  the result which AI generate for the user. 
# :--> SystemMessage :  the initial or TOP level message/prompt send by the user to the AI.

from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv 


load_dotenv() 

llm = HuggingFaceEndpoint(
    repo_id='openai/gpt-oss-20b',
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)


messages = [
    SystemMessage(content= 'You are a helpful assistent'),
    HumanMessage(content='Tell me about LangChain')
]


result = model.invoke(messages)

messages.append(AIMessage(content=result.content))


print(messages)
