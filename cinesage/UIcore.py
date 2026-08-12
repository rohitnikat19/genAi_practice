from dotenv import load_dotenv
import streamlit as st
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

st.set_page_config(page_title="Movie Information Extractor", page_icon="🎬", layout="centered")

st.title("🎬 Movie Information Extractor")
st.write("Paste a movie paragraph below and extract structured information from it.")

model = ChatMistralAI(model="mistral-small-2603")

prompt = ChatPromptTemplate.from_messages(
    [
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
""",
        ),
        (
            "human",
            """
     Extract information from the following movie paragraph:

     {paragraph}
    """,
        ),
    ]
)

para = st.text_area("Enter a movie paragraph:", height=200)

if st.button("Extract Information"):
    if para.strip():
        final_prompt = prompt.invoke({"paragraph": para})
        response = model.invoke(final_prompt)
        st.markdown("### Extracted Information")
        st.text(response.content)
    else:
        st.warning("Please enter a movie paragraph.")