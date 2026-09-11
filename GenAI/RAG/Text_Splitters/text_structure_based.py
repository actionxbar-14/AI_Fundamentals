



from langchain_text_splitters import RecursiveCharacterTextSplitter
text = """

Artificial Intelligence is one of the most important technologies of the modern world. It allows computers and machines to perform tasks that normally require human intelligence, such as understanding language, recognizing images, making decisions, and solving problems. AI is being used in many industries, including banking, healthcare, education, transportation, retail, and manufacturing.

In the banking and financial services industry, Artificial Intelligence has become especially useful. Banks can use AI to detect fraudulent transactions, analyze customer behavior, assess credit risk, and provide personalized financial recommendations. Machine learning models can study thousands of transactions and identify unusual patterns that may indicate fraud. AI-powered chatbots can also answer customer questions and provide support at any time.


"""


# Initialize the splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,

)



# Perform the split
chunks = splitter.split_text(text)

print(len(chunks))

print(chunks)

