from app.models.chat import Chat, Role
from app.providers.alibaba.qwen_chat_model import QwenChatModel

PROMPT_SUMMARIZE_CURRICULUM = """
Resuma o currículo do profissional de forma clara, objetiva e concisa, destacando seu nome, 
principais experiências profissionais, habilidades e formações relevantes. 
O resumo deve ser direto, fácil de entender e focado nos pontos mais importantes do perfil apresentado. 
Retorne apenas o resumo, sem incluir explicações ou informações adicionais.
"""

class CurriculumSummarizerAgent:
    @staticmethod
    def run(text: str) -> str:
        QwenChat = QwenChatModel()
        chat_history = [
            Chat(role=Role.system, content=PROMPT_SUMMARIZE_CURRICULUM),
            Chat(role=Role.user, content=text)
        ]
        response = QwenChat.run(chat_history, True)
        return response.content
