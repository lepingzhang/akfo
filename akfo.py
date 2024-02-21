from plugins import register, Plugin, Event
from utils.api import send_txt

@register
class AKFO(Plugin):
    name = "akfo"
    
    def __init__(self, config):
        super().__init__(config)
        self.keywords = self.config.get("keywords", [])
        self.forward_to_ids = self.config.get("forward_to_ids", [])
        
    def did_receive_message(self, event: Event):
        # 检查消息是否包含任何关键词
        if any(keyword in event.message.content for keyword in self.keywords):
            msg_content = event.message.content
            # 对每个配置的id进行消息转发
            for forward_to_id in self.forward_to_ids:
                send_txt(msg_content, forward_to_id)
            event.bypass()  # 防止消息被其他插件处理

    def will_generate_reply(self, event: Event):
        pass

    def will_decorate_reply(self, event: Event):
        pass

    def will_send_reply(self, event: Event):
        pass

    def help(self, **kwargs) -> str:
        return "转发带有关键词的消息到指定群聊或私聊'。"
