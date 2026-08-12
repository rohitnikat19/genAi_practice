from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import Optional, List
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI

load_dotenv()


class Movie(BaseModel):
    title: str
    relsease_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    ratings: Optional[float]
    short_summary: str

parser = PydanticOutputParser(pydantic_object=Movie)


model = ChatMistralAI(model="mistral-small-2603")

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        Extract Movie Information from the following paragraph
        {format_instructions}
        """
    ),
    ("human","{paragraph}")
]  
)


para = input("Enter a movie paragraph: ")

final_prompt = prompt.invoke({
    "paragraph": para,
    "format_instructions": parser.get_format_instructions()
})

response = model.invoke(final_prompt)
movie_info = parser.parse(response.content)

print(movie_info)
