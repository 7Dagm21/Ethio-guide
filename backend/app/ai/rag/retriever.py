from app.ai.rag.vector_store import VectorStore


class Retriever:

    def __init__(self, vector_store):

        self.vector_store = vector_store


    def retrieve(self, query, k=3):

        documents = self.vector_store.search(
            query,
            k=k
        )

        return documents