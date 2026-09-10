



from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r'C:\Users\ANUBHAV\Program_Folders\AI\GenAI\RAG\Document_Loaders\Datasets\dl-curriculum.pdf')


docs = loader.load()


print(docs)


print(docs[0].page_content)
print(docs[1].metadata)