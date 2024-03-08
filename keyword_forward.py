from plugins import register, Plugin, Event
from utils.api import send_txt
import re

@register
class KeywordForward(Plugin):
    name = "keyword_forward"
    
    def __init__(self, config):
        super().__init__(config)
        self.forward_config = [{
            'id': fc['id'],
            'patterns': [re.compile(keyword) for keyword in fc.get("keywords", [])]
        } for fc in self.config.get("forward_config", [])]
        
    def did_receive_message(self, event: Event):
        msg_content = event.message.content
        for fc in self.forward_config:
            if any(pattern.search(msg_content) for pattern in fc['patterns']):
                send_txt(msg_content, fc['id'])
                event.bypass()

    def will_generate_reply(self, event: Event):
        pass

    def will_decorate_reply(self, event: Event):
        pass

    def will_send_reply(self, event: Event):
        pass

    def help(self, **kwargs) -> str:
        return "转发带有关键词的消息到指定群聊或私聊"
