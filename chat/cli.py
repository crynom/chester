from chat.session import ChatSession
from llm.client import ask, askStream
from voice.stt import recordAudio, transcribeAudio

def chat(session: ChatSession, model: str, think: bool = False, stream: bool = True) -> None:

    voice = False
    prompt = input(f'\n{"*" * 10} Say "Hi"! (and "/bye" to exit) {"*" * 10}\n\n[ User ] > ')
    
    while True:
        if prompt.startswith('/'):
            match prompt.split()[0].strip().lower():
                case '/bye': break
                case '/quit': break
                case '/new': return chat(session, model, think, stream)
                case '/think':
                    think = not think
                    print(f'\nThink mode [{"ON" if think else "OFF"}]')
                case '/voice':
                    voice = not voice
                    print(f'\nVoice mode [{"ON" if voice else "OFF"}]')
                case _: print('Command not recognized.')
        elif voice and (prompt.lower().startswith('voice mode off') or prompt.strip() == ''): 
            # need a better way to do this
            voice = not voice
            print(f'\nVoice mode [{"ON" if voice else "OFF"}]')


        else:
            session.addMessages({
                'role': 'user',
                'content': prompt
            })
            answer = askStream(session.getMessages(), think=think, model=model, verbose=True) if stream else ask(session.getMessages(), think=think, model=model, verbose=True)  # type: ignore
            session.addMessages(answer)

        if voice:
            prompt = transcribeAudio(recordAudio())
            if not prompt.strip() == '':
                print(f'\n[ User ] > {prompt}')
        else:
            prompt = input('\n[ User ] > ')