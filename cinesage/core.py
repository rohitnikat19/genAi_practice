from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(model = "mistral-small-2603")
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a professional Movie Information Extraction Assistant.

Your task:
Extract useful and relevant information from the movie paragraph provided by the user and present it in a clean, consistent format.

Rules:
- Extract information ONLY from the provided paragraph.
- Do NOT invent, assume, or guess any facts.
- Do NOT add explanations or extra commentary.
- Follow the exact output format below.
- If any information is not mentioned in the paragraph, write NULL.
- Keep the information concise and accurate.
- For cast members, include the actor and character when available.
- Keep the short summary to 2-3 sentences maximum.

Output Format:

Movie Title:
Release Year:
Director:
Genre:
Main Cast:
Setting/Location:
Plot:
Themes:
Ratings:
Notable Features:
Short Summary:
"""
    ),
    ('human',
     """
     Extract information from the following movie paragraph:
     
     {paragraph}
    """)
]
)

para = input("Enter a movie paragraph: ")

final_prompt = prompt.invoke({
    "paragraph": para
})

response = model.invoke(final_prompt)

print(response.content)