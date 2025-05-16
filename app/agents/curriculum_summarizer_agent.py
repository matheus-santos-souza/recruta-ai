from app.models.chat import Chat, Role
from app.providers.alibaba.qwen_chat_model import QwenChatModel

PROMPT_SUMMARIZE_CURRICULUM = """
Resuma o currículo do profissional de forma clara, objetiva e concisa. 
Destaque o nome, principais experiências profissionais, habilidades técnicas e formações mais relevantes.
O resumo deve ser direto, fácil de ler e focado apenas nos pontos mais importantes do perfil apresentado. Retorne apenas o resumo, sem explicações adicionais.

Exemplo de entrada:
Nome: Carlos Henrique
Experiência: 10 anos como desenvolvedor backend, com passagens por empresas como Globo, PicPay e OLX.
Atua com arquitetura de microsserviços, APIs REST e mensageria com RabbitMQ.
Especialista em Node.js, Go, PostgreSQL e Docker.
Formação: Bacharel em Ciência da Computação pela USP.
Certificações: AWS Certified Developer, Kubernetes Administrator.

Resposta esperada:
Carlos Henrique é desenvolvedor backend com 10 anos de experiência em empresas como Globo, PicPay e OLX. 
Atua com arquitetura de microsserviços, APIs REST e mensageria com RabbitMQ. 
Tem expertise em Node.js, Go, PostgreSQL e Docker. 
É bacharel em Ciência da Computação pela USP e possui certificações AWS Developer e Kubernetes Administrator.
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
