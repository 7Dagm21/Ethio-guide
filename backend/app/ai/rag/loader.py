from pathlib import Path
from langchain_core.documents import Document


class DocumentLoader:
    def __init__(self):
        project_root = Path(__file__).resolve().parents[4]

        self.docs_path = (
            project_root
            / "knowledge_base"
            / "passport"
            / "markdown"
        )

    def load_documents(self):
        documents = []

        for file in self.docs_path.glob("*.md"):
            with open(file, "r", encoding="utf-8") as f:
                documents.append(
                    Document(
                        page_content=f.read(),
                        metadata={
                            "source": file.name,
                            "category": "passport"
                        }
                    )
                )

        return documents