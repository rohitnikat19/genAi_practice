from langchain_huggingface import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

texts = [
    "You are going to learn GenAi",
    "This is another example text."
]

vectors = embedding.embed_documents(texts)
print(vectors)