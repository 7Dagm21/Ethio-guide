from app.ai.rag.loader import DocumentLoader
from app.ai.rag.vector_store import VectorStore


loader = DocumentLoader()

documents = loader.load_documents()

print(f"Loaded {len(documents)} documents\n")


for doc in documents:
    print("=" * 50)
    print(doc.metadata["source"])
    print(doc.metadata["category"])
    print(doc.page_content[:200])
    print()


print("\nCreating vector store...")

store = VectorStore()

print("Adding documents to Chroma...")

store.add_documents(documents)

print("Vector database created successfully!")