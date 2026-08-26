
# :: downloading the open source model and then running it inside the RAM.

# from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline
# import os

# llm = HuggingFacePipeline.from_model_id(
#     model_id= 'openai/gpt-oss-20b',
#     task= 'text-generation',
#     pipeline_kwargs=dict(
#         temprature=0.5,
#         max_new_tokens=50
#     )
# )

# model = ChatHuggingFace(llm=llm)


# result = model.invoke("what is the capital of india")

# print(result.content)