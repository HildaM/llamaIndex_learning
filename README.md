# llamaIndex-learning
This is the repo for my llamaIndex learning notes

## Setup envrionment
I use miniconda to manage the learning envrionment, you can follow this instruction or simplely run on local python environment:
```
# conda env
conda create -n llamaindex-learning python=3.11
conda activate llamaindex-learning
```

After create the envrionment, intall the dependencies
```
pip install -r requirements.txt
```

Don't forget installing pytorch:
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

## LLM Seting
I will use OpenAI as the interface for access LLM, but that desn't mean I will use "openai".
Actually, I run LLM locally using LM Studio. LM Studio server can give 'OpenAI-Like' API interface for user.