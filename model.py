from langchain_community.chat_models import ChatLlamaCpp

def load_model():
    model_path = r"C:\Users\Nithish\Downloads\qwen2.5-3b-instruct-q5_0.gguf"
    model = ChatLlamaCpp(
        model_path=model_path,
        temperature=0.7,
        max_tokens=1000,
        top_p=0.9,
        n_gpu_layers=-1,
        streaming=True,
        n_ctx=4096,      # Context window size
        model_kwargs={
            "device": "cuda",
            "flash_attn": True,
        },
        stop=[
            "<|im_end|>",
            "Human:",
        ],
        verbose=False,
    )
    return model