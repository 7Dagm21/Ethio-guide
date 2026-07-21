from sentence_transformers import SentenceTransformer


class DocumentEmbedder:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        """
        Initialize embedding model
        """

        self.model = SentenceTransformer(model_name)


    def create_embeddings(self, texts):
        """
        Convert text into vector embeddings
        """

        embeddings = self.model.encode(
            texts,
            show_progress_bar=True
        )

        return embeddings