"""Chat with Qwen2.5-3B-Instruct running locally on your CPU.

Run:  python chat.py
Type 'exit' to quit, 'clear' to start a new conversation.
"""

import os
from pathlib import Path

from llama_cpp import Llama

MODEL_PATH = Path(__file__).parent / "models" / "qwen2.5-3b-instruct-q4_k_m.gguf"
SYSTEM_PROMPT = "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."

print("Loading model... (takes a few seconds)")
llm = Llama(
    model_path=str(MODEL_PATH),
    n_ctx=4096,                    # how much conversation the model remembers
    n_threads=os.cpu_count() // 2,  # use the physical CPU cores
    verbose=False,
)

messages = [{"role": "system", "content": SYSTEM_PROMPT}]
print("Ready! Type 'exit' to quit, 'clear' to reset.\n")

while True:
    try:
        user_input = input("You: ").strip()
    except (EOFError, KeyboardInterrupt):
        break
    if not user_input:
        continue
    if user_input.lower() == "exit":
        break
    if user_input.lower() == "clear":
        messages = messages[:1]
        print("(conversation cleared)\n")
        continue

    messages.append({"role": "user", "content": user_input})
    print("AI: ", end="", flush=True)

    reply = ""
    for chunk in llm.create_chat_completion(messages=messages, stream=True, max_tokens=1024):
        text = chunk["choices"][0]["delta"].get("content", "")
        print(text, end="", flush=True)
        reply += text
    print("\n")

    messages.append({"role": "assistant", "content": reply})

print("Bye!")
