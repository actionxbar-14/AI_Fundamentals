






from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel , RunnablePassthrough


load_dotenv()



prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables= ['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

llm = HuggingFaceEndpoint(
    repo_id='openai/gpt-oss-20b',
    task = "text-generation"
)
model = ChatHuggingFace(llm=llm)


parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1 , model , parser)

parallel_chain = RunnableParallel({
    'joke'  : RunnablePassthrough(),
    'explanation' : RunnableSequence(prompt2 , model , parser)
})


final_chain = RunnableSequence(joke_gen_chain , parallel_chain)

result = final_chain.invoke({'topic' : 'cricket'})

print(result)

