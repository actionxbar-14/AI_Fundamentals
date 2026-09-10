


from langchain_community.document_loaders import CSVLoader 

loader = CSVLoader(file_path=r'C:\Users\ANUBHAV\Program_Folders\AI\GenAI\RAG\Document_Loaders\Datasets\Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))
print(docs[0])