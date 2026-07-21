from transformers import pipeline
import torch


class Generator:

    def __init__(self):

        print("Loading Qwen 2.5 0.5B local model...")

        self.generator = pipeline(
            task="text-generation",
            model="Qwen/Qwen2.5-0.5B-Instruct",
            device_map="auto",
            dtype=torch.float32,
        )

        print("Qwen model loaded successfully")

    def generate(self, question, context):

        print("Generating answer...")

        messages = [
            {
                "role": "system",
                "content": (
                    "You are an AI assistant for Ethiopian Passport Services.\n\n"
                    "Your job is to answer questions ONLY using the supplied context.\n\n"
                    "Rules:\n"
                    "- Never use outside knowledge.\n"
                    "- Never invent information.\n"
                    "- If the answer is not contained in the context, reply exactly:\n"
                    "\"I do not have enough information to answer this question.\"\n"
                    "- Answer clearly and professionally.\n"
                    "- Use bullet points whenever appropriate."
                ),
            },
            {
                "role": "user",
                "content": f"""
Context:

{context}

----------------------------------------

Question:

{question}
""",
            },
        ]

        response = self.generator(
            messages,
            max_new_tokens=250,
            do_sample=False,
            repetition_penalty=1.1,
            return_full_text=False,
        )

        answer = response[0]["generated_text"]

        # Some pipeline versions return a list of messages.
        if isinstance(answer, list):
            answer = answer[-1]["content"]

        return answer.strip()