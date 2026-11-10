from session import ChatSession

def chat(session: ChatSession, model: str, think: bool = False, stream: bool = True) -> None:

    prompt = input(f'\n{"*" * 10} Say "Hi"! (and "/bye" to exit) {"*" * 10}\n\n[ User ] > ')
    
    while True:
        if prompt.startswith('/'):
            match prompt.split()[0].strip().lower():
                case '/bye': break
                case '/quit': break
                case '/new': return chat(session, model, think stream)
                case '/think':
                    think = not think
                    print(f'Think mode [{"on" if think else "off"}]')
                case _: print('Command not recognized.')


        else:
            session.addMessages({
                'role': 'user',
                'content': prompt
            })
            answer = askStream(session.getMessages, think=think, model=model, verbose=True) if stream else ask(session.getMessages, think=think, model=model, verbose=True)['message']  # type: ignore
            session.addMessages(answer)
        prompt = input('\n[ User ] > ')