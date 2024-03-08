# wechat-gptbot 关键词转发插件

本项目作为 `wechat-gptbot` 插件，可以将接收消息中包含关键词的消息转发给指定的群聊或者私聊。
一个使用场景：结合iOS快捷指令，将特定短信调用微信发送消息给机器人，机器人再进行转发。

## 安装指南

### 1. 添加插件源
在 `plugins/source.json` 文件中添加以下配置：
```
{
  "keyword_forward": {
    "repo": "https://github.com/lepingzhang/keyword_forward.git",
    "desc": "转发带有关键词的消息到指定群聊或私聊"
  }
}
```

### 2. 插件配置
在 `config.json` 文件中添加以下配置：
```
"plugins": [
  {
    "name": "keyword_forward",
    "forward_config": [
      {
        "id": "1234567890@chatroom",
        "keywords": ["验证码.*?(\\d{4,8})", "code"]
      },
      {
        "id": "wxid_1234567890",
        "keywords": ["其他关键词"]
      }
    ]
  }
]
```
