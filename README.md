# LLM-code-baseline
LLM在不同任务上的基线。也会融入Pretrain-Finetuned范式下的Bert系列任务。

## File List

- count_max_memory.py

  统计显存的最大使用大小。解决问题：LLM不同输入长度占用显存大小不同，容易在线上环境不同输入长度OOM。

  使用方法：python count_max_memory.py 将程序在后台运行，再运行自己的主程序，主程序运行完毕，cirl+C结束count_max_memory.py程序，即可输出在主程序运行过程中最大的显存占用。

- Pre-train

  预训练任务。待更新。

- Finetune

  微调任务。待更新。

  已更新QWen微调。

- RLHF-align

  强化学习对齐相关任务。待更新。

- RAG

  检索增强生成任务。待更新。
