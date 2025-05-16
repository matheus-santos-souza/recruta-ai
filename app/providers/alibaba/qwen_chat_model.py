from typing import List
from transformers import AutoModelForCausalLM, AutoTokenizer

from app.models.chat import Chat, ChatThinkingOutput

model_name = "Qwen/Qwen3-0.6B"
print(f"Modelo {model_name} carregando...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
  model_name,
  torch_dtype="auto",
  device_map="auto"
)
print(f"Modelo {model_name} carregado com sucesso!")
device = next(model.parameters()).device
device_name = "GPU" if str(device).startswith("cuda") else "CPU"
print(f"Modelo {model_name} está rodando em: {device_name}")

class QwenChatModel:
  def run(self, chat_history: List[Chat], enable_thinking: bool = False) -> ChatThinkingOutput:
    messages = [{"role": m.role.value, "content": m.content} for m in chat_history]
    text = tokenizer.apply_chat_template(
      messages,
      tokenize=False,
      add_generation_prompt=True,
      enable_thinking=enable_thinking
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
    generated_ids = model.generate(
      **model_inputs,
      max_new_tokens=2000
    )
    output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist()

    try:
      index = len(output_ids) - output_ids[::-1].index(151668)
    except ValueError:
      index = 0
    
    thinking_content = ""
    if enable_thinking:
      thinking_content = tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
    content = tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")
    return ChatThinkingOutput(thinking_content=thinking_content, content=content)
