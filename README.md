# wechat-gptbot 传令兵插件

本项目作为 `wechat-gptbot` 插件，可以将接收消息中包含关键词的消息转发给指定的群聊或者私聊。

## 安装指南

### 1. 添加插件源
在 `plugins/source.json` 文件中添加以下配置：
```
{
  "daily_news": {
    "repo": "https://github.com/lepingzhang/akfo.git",
    "desc": "负责转发群聊消息的传令兵"
  }
}
```

### 2. 插件配置
在 `config.json` 文件中添加以下配置：
```
"plugins": [
  {
    "name": "akfo",
    "keywords": ["关键词"],
    "forward_to_ids": ["wxid_1234567890", "1234567890@chatroom"]
  }
]
```
