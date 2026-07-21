from app.ai.rag.vector_store import VectorStore
from app.ai.rag.retriever import Retriever
from app.ai.rag.generator import Generator


class RAGService:

    def __init__(self):

        print("Initializing RAG service...")

        self.vector_store = VectorStore()

        self.retriever = Retriever(
            self.vector_store
        )

        self.generator = Generator()


    def answer(self, question):

        documents = self.retriever.retrieve(
            question,
            k=3
        )

        context = "\n\n".join(
            [
                doc.page_content
                for doc in documents
            ]
        )

        response = self.generator.generate(
            question,
            context
        )

        return {
            "answer": response,
            "sources": [
                {
                    "source": doc.metadata.get("source"),
                    "category": doc.metadata.get("category")
                }
                for doc in documents
            ]
        }