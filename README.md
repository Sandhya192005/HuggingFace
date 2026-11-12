# Local Qwen2.5 Chat

A simple terminal chatbot that runs [Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF) entirely on your CPU using [llama-cpp-python](https://github.com/abetlen/llama-cpp-python). No GPU or API key is needed.

## Setup

1. **Create a virtual environment and install the dependencies**

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate

   pip install -r requirements.txt
   ```

2. **Download the model** (about 2 GB) into the `models/` folder

   ```bash
   hf download Qwen/Qwen2.5-3B-Instruct-GGUF qwen2.5-3b-instruct-q4_k_m.gguf --local-dir models
   ```

   On older versions of `huggingface_hub`, use `huggingface-cli download` with the same arguments.

   The model isn't stored in this repo because it is too large for GitHub.

## Usage

```bash
python chat.py
```

- Type a message and press Enter to chat.
- Type `clear` to start a new conversation.
- Type `exit` (or press Ctrl+C) to quit.

## Configuration

You can change these settings in `chat.py`:

| Setting | Default | Description |
|---|---|---|
| `n_ctx` | `4096` | How many tokens of conversation the model remembers |
| `n_threads` | half of your CPU cores | How many CPU threads to use |
| `max_tokens` | `1024` | The maximum length of each reply |
| `SYSTEM_PROMPT` | Qwen's default | The model's persona and instructions |
