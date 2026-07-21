from app.ai.rag.loader import DocumentLoader
from app.ai.rag.chunker import DocumentChunker


loader = DocumentLoader()

documents = loader.load_documents()


print("Documents loaded:", len(documents))


chunker = DocumentChunker()

chunks = chunker.split_documents(documents)


print("Chunks created:", len(chunks))


for i, chunk in enumerate(chunks[:5]):
    print("\n====================")
    print("Chunk:", i+1)
    print(chunk.page_content[:300])
    print("Metadata:")
    print(chunk.metadata)