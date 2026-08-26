


from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv 


load_dotenv() 

llm = HuggingFaceEndpoint(
    repo_id='openai/gpt-oss-20b',
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital on India")

print(result.content)








# ------------------------------------------------------------------------------------------------------------------------------


# import os
# from pathlib import Path
# from dotenv import load_dotenv
# from huggingface_hub import InferenceClient

# env_path = Path(__file__).resolve().parents[1] / ".env"

# load_dotenv(env_path, override=True)

# token = os.getenv("HF_TOKEN")

# print("Token loaded:", token is not None)

# client = InferenceClient(
#     api_key=token
# )

# response = client.chat.completions.create(
#     model="openai/gpt-oss-20b",
#     messages=[
#         {
#             "role": "user",
#             "content": "What is the capital of India?"
#         }
#     ]
# )

# print(response.choices[0].message.content)