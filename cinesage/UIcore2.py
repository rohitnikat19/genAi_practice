from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import Optional, List
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI

load_dotenv()

st.set_page_config(page_title="Movie Information Extractor", page_icon="🎬", layout="centered")

st.title("🎬 Movie Information Extractor")
st.write("Paste a movie paragraph below and extract structured information from it.")


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

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
        Extract Movie Information from the following paragraph
        {format_instructions}
        """,
        ),
        ("human", "{paragraph}"),
    ]
)

para = st.text_area("Enter a movie paragraph:", height=200)

if st.button("Extract Information"):
    if para.strip():
        final_prompt = prompt.invoke(
            {
                "paragraph": para,
                "format_instructions": parser.get_format_instructions(),
            }
        )
        response = model.invoke(final_prompt)
        st.markdown("### Extracted Information")
        st.text(response.content)
    else:
        st.warning("Please enter a movie paragraph.")