# Resume Recruta-AI

Uma API inteligente que permite o envio de múltiplos currículos (PDF ou imagem), gera automaticamente resumos e responde perguntas personalizadas usando LLMs. Ideal para automatizar a análise de currículos em processos seletivos.

## Funcionalidades

- 📄 Upload de vários currículos (PDF, JPG, PNG)
- 🧠 Geração automática de resumos via LLM
- ❓ Consulta opcional para filtrar currículos por critérios
- 📝 Retorno com justificativas e resultados relevantes
- 📦 Dockerizado para fácil execução
- 📚 Documentação interativa via Swagger
- 🗂️ Log de uso (sem armazenar arquivos) em banco NoSQL

## Tecnologias

- **Python**
- **FastAPI**
- **Pydantic**
- **Tesseract**
- **Hugging Face Transformers**
- **MongoDB (NoSQL para logs)**
- **Docker & Docker Compose**

## Uso da API

### Corpo da Requisição (multipart/form-data)

| Campo        | Tipo              | Obrigatório | Descrição                                  |
|--------------|-------------------|-------------|--------------------------------------------|
| files        | Lista de arquivos | ✅           | Currículos em PDF ou imagem               |
| query        | String            | ❌           | Pergunta opcional para filtrar currículos |
| request_id   | UUID              | ✅           | ID único da requisição                    |
| user_id      | String            | ✅           | Identificador do solicitante              |

### Exemplo de Requisição (com query)
```json
{
  "request_id": "123e4567-e89b-12d3-a456-426614174000",
  "user_id": "fabio.techmatch",
  "query": "Quais currículos se encaixam para engenheiro de software com React e Python?"
}
```

### Exemplo de Resposta (com query)
```json
{
  "request_id": "123e4567-e89b-12d3-a456-426614174000",
  "user_id": "fabio.techmatch",
  "timestamp": "2025-05-13T01:39:38.721247",
  "query": "Quais currículos se encaixam para engenheiro de software com React e Python?",
  "result": "O currículo de João Silva corresponde à vaga por ter experiência com React e Python."
}
```

### Exemplo de Resposta (sem query)
```json
{
  "request_id": "123e4567-e89b-12d3-a456-426614174000",
  "user_id": "fabio.techmatch",
  "timestamp": "2025-05-13T01:39:38.721247",
  "result": [
    {
      "filename": "curriculo1.pdf",
      "summary": "Desenvolvedor backend experiente com Python e Django."
    },
    {
      "filename": "curriculo2.jpg",
      "summary": "Desenvolvedor frontend com experiência em React e TypeScript."
    }
  ]
}
```

### Como Executar
```bash
docker-compose up -d
```



