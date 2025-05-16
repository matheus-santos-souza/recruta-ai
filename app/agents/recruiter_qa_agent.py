from typing import List
from app.models.chat import Chat, Role
from app.providers.alibaba.qwen_chat_model import QwenChatModel

PROMPT_RECRUITER_QA = """
Você é um agente de recrutamento especializado em analisar currículos e responder perguntas sobre candidatos. 
Abaixo estão os currículos sumarizados dos candidatos entre as tags <curriculums> e </curriculums>. 
Utilize apenas as informações fornecidas nesses currículos para responder de forma objetiva e clara às perguntas do recrutador.

<curriculums>
{curriculums}
</curriculums>
"""

class RecruiterQAAgent:
    @staticmethod
    def run(text: str, curriculums: List[str]) -> str:
        QwenChat = QwenChatModel()
        curriculums_str = "\n".join(curriculums)
        prompt = PROMPT_RECRUITER_QA.format(curriculums=curriculums_str)
        chat_history = [
            Chat(role=Role.system, content=prompt),
            Chat(role=Role.user, content=text)
        ]
        response = QwenChat.run(chat_history, enable_thinking=True)
        return response.content
