import pickle, os

class ChatSession:
    def __init__(self, sysPrompt: str = '') -> None:
        self.messages = [
            {
                'role': 'system',
                'content': sysPrompt
            }
        ]

    def getMessages(self) -> list[dict[str, str]]:
        return self.messages

    def addMessages(self, messages: dict[str, str]) -> None:
        self.messages.append(messages)

    def save(self) -> None:
        pass # for sqlite