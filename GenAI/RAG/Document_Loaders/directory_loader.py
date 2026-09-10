



from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader 

loader = DirectoryLoader(
    path = r'C:\Users\ANUBHAV\Program_Folders\AI\GenAI\RAG\Document_Loaders\Datasets',
    glob = '*.pdf',
    loader_cls = PyPDFLoader 
)


docs = loader.load()


for document in docs:
    print(document.metadata)



#---------------------------------------------------------------------------------------------------------------




# :: lazy load : 




from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader 

loader = DirectoryLoader(
    path = r'C:\Users\ANUBHAV\Program_Folders\AI\GenAI\RAG\Document_Loaders\Datasets',
    glob = '*.pdf',
    loader_cls = PyPDFLoader 
)


docs = loader.lazy_load()


for document in docs:
    print(document.metadata)
