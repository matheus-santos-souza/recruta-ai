from app.models.chat import Chat, Role
from app.providers.qwen.qwen_chat_model import QwenChatModel


PROMPT_SUMMARIZE_CURRICULUM = """
Resuma o currículo abaixo de forma clara, objetiva e concisa, destacando as principais experiências profissionais, habilidades e formações relevantes. O resumo deve ser fácil de entender e focado nos pontos mais importantes do perfil apresentado.
Retorne apenas o resumo, sem incluir informações adicionais ou explicações.
"""

class CurriculumSummarizerAgent:
    @staticmethod
    def run(text: str) -> str:
        QwenChat = QwenChatModel()
        chat_history = [
            Chat(role=Role.system, content=PROMPT_SUMMARIZE_CURRICULUM),
            Chat(role=Role.user, content=text)
        ]
        response = QwenChat.run(chat_history)
        return response.content
