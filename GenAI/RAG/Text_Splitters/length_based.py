

# from langchain_text_splitters import CharacterTextSplitter

# text = """

# Artificial Intelligence is one of the most important technologies of the modern world. It allows computers and machines to perform tasks that normally require human intelligence, such as understanding language, recognizing images, making decisions, and solving problems. AI is being used in many industries, including banking, healthcare, education, transportation, retail, and manufacturing.

# In the banking and financial services industry, Artificial Intelligence has become especially useful. Banks can use AI to detect fraudulent transactions, analyze customer behavior, assess credit risk, and provide personalized financial recommendations. Machine learning models can study thousands of transactions and identify unusual patterns that may indicate fraud. AI-powered chatbots can also answer customer questions and provide support at any time.

# Data plays a major role in the development of AI systems. Organizations collect data from customers, transactions, websites, applications, and various business processes. This data must be cleaned, transformed, and analyzed before it can be used effectively. Data analysts and data engineers help organizations prepare reliable data for reporting, analytics, and machine learning.

# Python is one of the most popular programming languages for working with data and AI. Libraries such as NumPy, pandas, Matplotlib, and scikit-learn provide powerful tools for data analysis and machine learning. SQL is also essential because most business data is stored in relational databases.

# As AI continues to develop, professionals who understand data, programming, business processes, and machine learning will have many opportunities to build useful and intelligent applications.

# """

# splitter = CharacterTextSplitter(
#     chunk_size = 100,
#     chunk_overlap = 0,
#     separator=''
# )


# result = splitter.split_text(text)

# print(result)





#-----------------------------------------------------------------------------------------------------------------------------------------------



# :: with document :  




from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r'C:\Users\ANUBHAV\Program_Folders\AI\GenAI\RAG\Text_Splitters\Datasets\dl-curriculum.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=''
)


result = splitter.split_documents(docs)

# print(result)


print(result[1].page_content)
