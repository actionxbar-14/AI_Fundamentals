


from sklearn.metrices.pairwise import cosine_similarity 
import numpy as np 

load_dotenv()

embedding = OpenAIEmbeddings(model='BAAI/bge-small-en-v1.5' ,dimensions=300)

documents = [
    'Delhi is the capital of India.',
    'Machine learning helps computers learn from data.',
    'The sun rises in the east.',
    'Python is widely used for artificial intelligence.'
]



query = 'tell me about virat kohli'

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)


scores = cosine_similarity([query_embedding] ,doc_embeddings)[0]

index , score = sorted(list(enumerate(scores))) ,key = lambda x: x[1][-1]



print(query)
print(documents[index])
print("similarity score is :" ,score)





