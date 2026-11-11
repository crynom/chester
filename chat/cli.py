from chat.session import ChatSession
from llm.client import ask, askStream
from voice.stt import recordAudio, transcribeAudio

def chat(session: ChatSession, model: str, think: bool = False, stream: bool = True) -> None:

    voice = False
    prompt = input(f'\n{"*" * 10} Say "Hi"! (and "/bye" to exit) {"*" * 10}\n\n[ User ] > ')
    
    while True:
        if prompt.startswith('/'):
            match prompt.strip().lower():
                case '/bye': break
                case '/quit': break
                case '/new': return chat(session, model, think, stream)
                case '/think':
                    think = not think
                    print(f'\nThink mode [{"ON" if think else "OFF"}]')
                case '/voice':
                    voice = not voice
                    print(f'\nVoice mode [{"ON" if voice else "OFF"}]')
                case '/lock in':
                    session.addMessage({'role': 'system', 'content': 'Respond to the next query, and only the next query unless the user asks you to continue remaining "locked in" (another term for serious), with the utmost care, dignity, rigor, and intellectual depth. Ensure that you challenge your own results until you are certain that you are correct. If you are not highly certain, give your certainty level as part of your response or decline to answer on the grounds of uncertainty. Use any tools at your disposal. Begin your response with "*locked in.* ".'})
                case _: print('Command not recognized.')
        elif voice and (prompt.lower().startswith('voice mode off') or prompt.strip() == ''): 
            # need a better way to do this
            voice = not voice
            print(f'\nVoice mode [{"ON" if voice else "OFF"}]')


        else:
            session.addMessage({
                'role': 'user',
                'content': prompt
            })
            answer = askStream(session.getMessages(), think=think, model=model, verbose=True) if stream else ask(session.getMessages(), think=think, model=model, verbose=True)  # type: ignore
            session.addMessage(answer)

        if voice:
            prompt = transcribeAudio(recordAudio())
            if not prompt.strip() == '' and not prompt.startswith('/'): print(f'\n[ User ] > {prompt}')
        else:
            prompt = input('\n[ User ] > ')

            # fix the user prompt being printed after repsonse