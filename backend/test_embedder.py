from app.ai.rag.loader import DocumentLoader
from app.ai.rag.chunker import DocumentChunker
from app.ai.rag.embedder import DocumentEmbedder


# Load documents
loader = DocumentLoader()

documents = loader.load_documents()

print("Documents loaded:", len(documents))


# Chunk documents
chunker = DocumentChunker(
    chunk_size=700,
    chunk_overlap=100
)

chunks = chunker.split_documents(documents)

print("Chunks created:", len(chunks))


# Get text from chunks
texts = [
    chunk.page_content
    for chunk in chunks
]


# Create embeddings
embedder = DocumentEmbedder()

embeddings = embedder.create_embeddings(texts)


print("\nEmbeddings created:", len(embeddings))

print("\nFirst embedding:")
print(embeddings[0])

print("\nEmbedding size:")
print(len(embeddings[0]))