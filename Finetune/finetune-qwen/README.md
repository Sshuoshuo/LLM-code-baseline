## 数据格式

所有样本放到一个列表中并存入json文件中， 每个样本对应一个字典，包含id和conversation，其中后者为一个列表。

```python
[
  {
    "id": "identity_0",
    "conversations": [
      {
        "from": "user",
        "value": "你好"
      },
      {
        "from": "assistant",
        "value": "我是一个语言模型，我叫通义千问。"
      }
    ]
  }
]
```

```python
# code example
import json

# 创建样本列表
samples = [
    {
        "id": "identity_0",
        "conversations": [
            {
                "from": "user",
                "value": "你好"
            },
            {
                "from": "assistant",
                "value": "我是一个语言模型，我叫通义千问。"
            }
        ]
    }
]

# 将样本列表存入JSON文件
with open('samples.json', 'w') as outfile:
    json.dump(samples, outfile, ensure_ascii=False)
```

