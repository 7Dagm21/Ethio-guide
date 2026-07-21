from app.ai.rag.generator import Generator
from app.ai.rag.vector_store import VectorStore
from app.ai.rag.retriever import Retriever


print("Starting generator test...")

# Initialize components
store = VectorStore()
retriever = Retriever(store)
generator = Generator()

# User question
question = "How can I apply for an Ethiopian passport?"

print(f"\nQuestion:\n{question}")

# Retrieve relevant documents
documents = retriever.retrieve(question)

# Build context
context = "\n\n".join(
    doc.page_content
    for doc in documents
)

# Show retrieved context
print("\n" + "=" * 60)
print("CONTEXT RETRIEVED FROM CHROMADB")
print("=" * 60)
print(context)

# Generate answer
print("\nGenerating answer...")

answer = generator.generate(
    question=question,
    context=context
)

print("\n" + "=" * 60)
print("AI RESPONSE")
print("=" * 60)
print(answer)