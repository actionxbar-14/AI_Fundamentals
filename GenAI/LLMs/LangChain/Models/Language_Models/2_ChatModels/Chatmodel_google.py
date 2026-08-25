
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 





load_dotenv()





model = ChatGoogleGenerativeAI(model = 'gemini-3.6-flash')

result = model.invoke("What is the capital of India")

print(result.content)












# -------------------------------------------------------------------------------------------------- 






# from pathlib import Path
# from dotenv import load_dotenv, dotenv_values
# import os

# # Current file:
# print("FILE:", Path(__file__).resolve())

# # 2_ChatModels folder
# current_folder = Path(__file__).resolve().parent
# print("CURRENT FOLDER:", current_folder)

# # Language_Models folder
# project_root = current_folder.parent
# print("PROJECT ROOT:", project_root)

# # .env path
# env_path = project_root / ".env"
# print("ENV PATH:", env_path)

# # Check whether .env actually exists
# print("ENV EXISTS:", env_path.exists())

# # Read .env directly
# config = dotenv_values(env_path)

# print("ENV VARIABLES FOUND:", list(config.keys()))

# # Load environment variables
# load_dotenv(env_path)

# print("GOOGLE_API_KEY EXISTS:", os.getenv("GOOGLE_API_KEY") is not None)
# print("GEMINI_API_KEY EXISTS:", os.getenv("GEMINI_API_KEY") is not None)