from app.ai.rag.vector_store import VectorStore


store = VectorStore()


query = "What documents are required for a passport application?"

results = store.search(query, k=3)


print(f"Found {len(results)} results\n")


for result in results:
    print("=" * 50)
    print(result.metadata)
    print(result.page_content[:300])
    print()