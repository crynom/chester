from chat.session import ChatSession
from chat.cli import chat

from utils.config import MODEL, SYSPROMPT

if __name__ == 'main':
    session = ChatSession(SYSPROMPT['default'])
    chat(
        session = session,
        model = MODEL,
        think = True, # why not
        stream = True
    )