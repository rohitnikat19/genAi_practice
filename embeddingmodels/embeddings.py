from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

vector = embeddings.embed_query("You are going to learn GenAi")

print(vector)
print(len(vector))