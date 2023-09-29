# Llama Index Experiment

The following notebook implements a RAG system using LlamaIndex. It is using LlamaCPP as the main LLM API.

## Setup

1. Configure LlamaCPP. Refer to the following [link](https://github.com/abetlen/llama-cpp-python) for the installation steps. This will depend on the hardware configuration that you have.
2. Install the other python dependencies in the requirements.txt.
3. Create a model folder and download the following [model](https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_0.gguf) and store it to the created model folder. The model that will be downloaded is the llama-2-7b-chat.Q4_0.gguf

## Implementations

The implementations folder contain the different POCs for Llama Index and LLMs in general. The notebooks can be run using vscode or jupyter server.

## DBS

The dbs folder contains the docker-compose file for various db setups used in the notebook. It requires that you install Docker and docker-compose. _If you can configure these databases locally you can bypass this folder._

## Hardware and Data

- CPU: 4500u
- RAM: 16GB
- GPU: Integrated in 4500u

## Data

The data folder contains a PDF document which is the QGIS 3.22 user manual. It contains about 1393 pages and is a mixture of texts and images.

## Notes

- We are using a quantized model to reduce the hardware requirements of running a full blown LLM. Refer to the following [Reddit post](https://www.reddit.com/r/LocalLLaMA/comments/14gjz8h/i_have_multiple_doubts_about_kquant_models_and/) for guidance regarding quantized models
- Performance will be better if you are running using a GPU and better CPU and Memory.
