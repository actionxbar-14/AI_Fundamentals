


# :: downloading the open source embedding model and run it into the local system to generate the embedding. 


from langchain_huggingface import HuggingFaceEmbeddings 

embedding = HuggingFaceEmbeddings(model_name = 'BAAI/bge-small-en-v1.5')

text = "Delhi is the capital of India" 

vector = embedding.embed_query(text)

print(str(vector))