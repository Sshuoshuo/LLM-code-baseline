# 微调任务

包括分类与生成，待更新。

## 指令微调

finetune-qwen：微调qwen脚本，修改自[QwenLM/Qwen: The official repo of Qwen (通义千问) chat & pretrained large language model proposed by Alibaba Cloud. (github.com)](https://github.com/QwenLM/Qwen)

说明：qwen架构修改自LLaMA，主要修改了embedding和output projection层，位置编码采用RoPE，对于Bias只保留了QKV注意力层，采用Pre-Norm&RMSNorm，激活函数为SwiGLU，基本为LLM中最优架构。