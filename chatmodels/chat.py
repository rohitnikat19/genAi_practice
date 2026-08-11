from dotenv import load_dotenv

load_dotenv()


#from langchain.chat_models import init_chat_model

from langchain_mistralai import ChatMistralAI
#from langchain_openai import ChatOpenAI
#from langchain_groq import ChatGroqAI
#from langchain_google_genai import ChatGoogleGenAI


#model = init_chat_model("gpt-3.5 Turbo")
#model = init_chat_model("google_genai:gemini-3.1-flash-lite")
#model = init_chat_model("groq:openai/gpt-oss-120b")
model = ChatMistralAI(model = "mistral-small-2603", temperature=0.7, max_tokens=100)



response = model.invoke("Who is virat kohli?")

print(response.content)