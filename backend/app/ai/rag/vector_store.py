from pathlib import Path
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


class VectorStore:

    def __init__(self):

        BASE_DIR = Path(__file__).resolve().parents[4]

        VECTOR_DB = BASE_DIR / "vector_db" / "chroma"

        VECTOR_DB.mkdir(
            parents=True,
            exist_ok=True
        )

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.vector_store = Chroma(
            persist_directory=str(VECTOR_DB),
            embedding_function=self.embeddings
        )


    def add_documents(self, documents):

        self.vector_store.add_documents(
            documents
        )


    def search(self, query, k=3):

        return self.vector_store.similarity_search(
            query,
            k=k
        )