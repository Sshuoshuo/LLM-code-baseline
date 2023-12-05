
import json
from datasets import load_dataset
# demo dataset is Evol-Instruct-Code-80k-v1, you can download it from hf or load is by load_dataset("nickrosh/Evol-Instruct-Code-80k-v1")
# this file is to construct dataset formatted as qwen instruct tuning
evol_instruct_code = load_dataset("Evol-Instruct-Code-80k-v1")
samples = []
for i in range(300): # len(evol_instruct_code['train'])
    samples.append(
        {
            "id": str(i),
            "conversations": [
                {
                    "from": "user",
                    "value": evol_instruct_code['train']['instruction'][i]
                },
                {
                    "from": "assistant",
                    "value": evol_instruct_code['train']['output'][i]
                }
            ]
        }
    )
# 将样本列表存入JSON文件
with open('evol_instruct_code.json', 'w') as outfile:
    json.dump(samples, outfile, ensure_ascii=False)
