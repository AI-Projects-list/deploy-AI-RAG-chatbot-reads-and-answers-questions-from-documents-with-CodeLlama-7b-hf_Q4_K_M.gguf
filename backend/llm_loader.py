from llama_cpp import Llama

llm = Llama(
    model_path="models/CodeLlama-7b-hf_Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=8,
    n_gpu_layers=32
)

def get_llama_response(prompt):
    output = llm(prompt, max_tokens=256)
    return output['choices'][0]['text']
