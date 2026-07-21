from app.ai.rag.loader import DocumentLoader
from app.ai.rag.chunker import DocumentChunker
from app.ai.rag.vector_store import VectorStore


loader = DocumentLoader()

documents = loader.load_documents()

print(
    "Documents:",
    len(documents)
)


chunker = DocumentChunker(
    chunk_size=700,
    chunk_overlap=100
)

chunks = chunker.split_documents(documents)


print(
    "Chunks:",
    len(chunks)
)


store = VectorStore()


store.add_documents(
    chunks
)


print(
    "Documents stored in ChromaDB"
)


results = store.search(
    "How can I renew my passport?"
)


print("\nSearch Results:\n")


for result in results:
    print("----------------")
    print(result.page_content[:300])
    print(result.metadata)