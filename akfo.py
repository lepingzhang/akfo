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
        if any(keyword in event.message.content for keyword in self.keywords):
            msg_content = event.message.content
            for forward_to_id in self.forward_to_ids:
                send_txt(msg_content, forward_to_id)
            event.bypass()

    def will_generate_reply(self, event: Event):
        pass

    def will_decorate_reply(self, event: Event):
        pass

    def will_send_reply(self, event: Event):
        pass

    def help(self, **kwargs) -> str:
        return "转发带有关键词的消息到指定群聊或私聊"
