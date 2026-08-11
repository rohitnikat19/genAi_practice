from dotenv import load_dotenv

load_dotenv()


#from langchain.chat_models import init_chat_model

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


model = ChatMistralAI(model = "mistral-small-2603", temperature=0.7, max_tokens=100)



print("Choose your AI model:")

print("Press 1 for Sad Mode")
print("Press 2 for Funny Mode")
print("Press 3 for angry Mode")

choice = int(input("Enter your choice (1, 2, or 3): "))

if choice == 1:
    mode = "You are a Sad AI Agent"
elif choice == 2:
    mode = "You are a Funny AI Agent"
elif choice == 3:
    mode = "You are an Angry AI Agent" 
else :
    mode = "This is a default AI Agent"


messages = [
    SystemMessage(content=mode)
]

print("Welcome to the GenAi Chatbot! Type 0 to quit.")
while True:
    
    prompt = input("You: ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot: ",response.content)
    
print(messages)