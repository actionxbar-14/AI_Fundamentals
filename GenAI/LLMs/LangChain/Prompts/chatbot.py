




# :: Simple Chatbot :  

# from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
# from dotenv import load_dotenv 


# load_dotenv() 

# llm = HuggingFaceEndpoint(
#     repo_id='openai/gpt-oss-20b',
#     task = "text-generation"
# )

# model = ChatHuggingFace(llm=llm)


# while True:
#     user_input = input('You : ')
#     if user_input == 'exit':
#         break 

#     result = model.invoke(user_input)
#     print("HF-Ai :" , result.content)



# -------------------------------------------------------------------------------------------------------------------






# :: Adding the chat history functionality :  



# from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
# from dotenv import load_dotenv 


# load_dotenv() 

# llm = HuggingFaceEndpoint(
#     repo_id='openai/gpt-oss-20b',
#     task = "text-generation"
# )

# model = ChatHuggingFace(llm=llm)

# chat_history = []


# while True:
#     user_input = input('You : ')
#     chat_history.append(user_input)
#     if user_input == 'exit':
#         break 

#     result = model.invoke(chat_history)
#     chat_history.append(result.content)
#     print("HF-Ai :" , result.content)




# print(chat_history)



# NOTE :  We added the chat history but it look like this : 

# ['hii', 'Hey there! 👋 How can I help you today?', '', 'Hey! 👋 What can I help you with today?', 'which one is greater than 2 or 0', '2 is greater than 0.', 'now multiply the bigger number with 10', '2 multiplied by 10 is **20**.', 'exit']

# Here we can't figure out that who write which line so we have to implement dictionary to contain this external information using langchain message :







# -------------------------------------------------------------------------------------------------------------------




# :: Adding the messages feature  : 




from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv 


from langchain_core.messages import SystemMessage , HumanMessage , AIMessage

load_dotenv() 

llm = HuggingFaceEndpoint(
    repo_id='openai/gpt-oss-20b',
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

chat_history = [
    SystemMessage(content= 'You are a Helpful AI assistent')
]


while True:
    user_input = input('You : ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break 

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("HF-Ai :" , result.content)




print(chat_history)
