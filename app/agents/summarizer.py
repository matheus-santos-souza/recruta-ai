class Summarizer:
    @staticmethod
    def summarize(text: str) -> str:
        # Placeholder simples — depois trocamos por um modelo LLM local ou da HuggingFace
        lines = text.strip().split("\n")
        return " ".join(lines[:5]) + "..."
