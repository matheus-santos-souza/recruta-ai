from typing import List
from transformers import AutoModelForCausalLM, AutoTokenizer

from app.models.chat import Chat, ChatThinkingOutput

class QwenChatModel:
  def __init__(self, model_name="Qwen/Qwen3-0.6B"):
    self.tokenizer = AutoTokenizer.from_pretrained(model_name)
    self.model = AutoModelForCausalLM.from_pretrained(
      model_name,
      torch_dtype="auto",
      device_map="auto"
    )

  def run(self, chat_history: List[Chat]) -> ChatThinkingOutput:
    messages = [{"role": m.role.value, "content": m.content} for m in chat_history]
    text = self.tokenizer.apply_chat_template(
      messages,
      tokenize=False,
      add_generation_prompt=True,
      enable_thinking=True
    )
    model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)
    generated_ids = self.model.generate(
      **model_inputs,
      max_new_tokens=32768
    )
    output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist()

    try:
      index = len(output_ids) - output_ids[::-1].index(151668)
    except ValueError:
      index = 0

    thinking_content = self.tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
    content = self.tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")
    return ChatThinkingOutput(thinking_content=thinking_content, content=content)
