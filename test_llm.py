import os
from llama_cpp import Llama

llm = Llama(model_path=os.getenv("MODEL"))
output = llm("Q: What is the smallest mammal? A: ", max_tokens=32, stop=["Q:", "\n"], echo=True)
print(output)
