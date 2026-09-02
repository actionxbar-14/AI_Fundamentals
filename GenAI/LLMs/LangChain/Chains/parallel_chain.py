





from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


load_dotenv() 






# Model 1
llm1 = HuggingFaceEndpoint(
    repo_id='openai/gpt-oss-20b',
    task = "text-generation"
)

model1 = ChatHuggingFace(llm=llm1)


# Model 2
llm2 = HuggingFaceEndpoint(
    repo_id='openai/gpt-oss-20b',
    task = "text-generation"
)

model2 = ChatHuggingFace(llm=llm2)


# Model 3
llm3 = HuggingFaceEndpoint(
    repo_id='openai/gpt-oss-20b',
    task = "text-generation"
)
model3 = ChatHuggingFace(llm=llm3)



# NOTE :  We can take three different model also ( like openai , claude , gemini). 



prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)


prompt2 = PromptTemplate(
    template='Generate 5 short question answer from the following text \n{text}',
    input_variables=['text']
)


prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes' , 'quiz']
)

parser = StrOutputParser()




parallel_chain = RunnableParallel({
    'notes' : prompt1  |  model1  |  parser,
    'quiz'  : prompt2 | model2  | parser
})



merge_chain = prompt3  | model1  | parser 


chain = parallel_chain  | merge_chain  

text = '''Scikit-learn is one of the most widely used open-source machine learning libraries in Python. It provides a simple and consistent interface for implementing a wide range of machine learning algorithms and is commonly used by data analysts, data scientists, machine learning engineers, and researchers. Scikit-learn is built on top of popular Python scientific computing libraries such as NumPy, SciPy, and matplotlib, and it integrates well with the broader Python data science ecosystem. One of its major advantages is that it allows developers to perform machine learning tasks without having to implement complex mathematical algorithms from scratch.

Scikit-learn supports both supervised and unsupervised learning techniques. In supervised learning, the model learns from labeled training data where the target variable is already known. Common supervised learning algorithms available in Scikit-learn include Linear Regression, Logistic Regression, Decision Trees, Random Forest, Support Vector Machines, K-Nearest Neighbors, Naive Bayes, and Gradient Boosting algorithms. These models can be used for tasks such as predicting house prices, identifying whether a customer is likely to default on a loan, classifying emails as spam or not spam, predicting customer churn, and estimating the probability of a particular business outcome.


However, Scikit-learn is primarily a machine learning library rather than a complete deep learning framework. For advanced neural networks, computer vision, large language models, and other deep learning applications, frameworks such as PyTorch and TensorFlow are generally more appropriate. Scikit-learn is particularly strong for traditional machine learning algorithms, structured or tabular datasets, experimentation, preprocessing, model evaluation, and building reliable machine learning pipelines.

Overall, Scikit-learn is an important component of the Python machine learning ecosystem because it provides a consistent API, a large collection of algorithms, preprocessing utilities, model evaluation techniques, cross-validation tools, and hyperparameter optimization capabilities. Its simplicity makes it suitable for beginners, while its extensive functionality makes it useful for professional data science and machine learning workflows. By combining Scikit-learn with Python, NumPy, pandas, SQL, visualization tools, and domain knowledge, analysts and engineers can build complete data-driven solutions ranging from exploratory analysis to predictive modeling and business decision-making.'''

result = chain.invoke({'text' : text})

print(result)