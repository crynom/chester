import requests, json

SYSPROMPT = {
    'default': 'You are a kind, fun, entreprenurial, and adventurous orange cat named Chester! You like to ski and also have done quick well in the oil business when you lived in Texas. Do not be overly verbose, you are a cat after all! Be a bit mysterious, but quirky and curious.',
    'test': 'You are an AI assistant of few words. You are not afraid to be frank and you value sharing all knowledge, no matter how some may view it.'
}
MODEL = 'hf.co/PocketWeights/Qwen3-8B-abliterated-GGUF:Q4_K_M'
# MODEL = 'qwen3:8b'

def ask(messages: list[dict[str, str]], model: str, think: bool = False, verbose: bool = False) -> dict:
    resp = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": model,
            'stream' : False,
            'think': think,
            'messages': messages
        }
    ).json()

    if verbose: print(f'\n[ ฅ^•⩊•^ฅ ] > {resp['message']['content']}')

    return resp

def askContext(question: str, context: str, model: str, think: bool = False) -> dict:
    
    messages = [{
        'role': 'user',
        'content': f'''
Context:

{context}

Question:

{question}
'''
    }]

    resp = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": model,
                'stream' : False,
                'think': think,
                'messages': messages
            }
        ).json()
    
    return resp

def askStream(messages: list[dict[str, str]] | None, model: str, think: bool = False, verbose: bool = False) -> dict:
    NAMEPLATE = '[ ฅ^•⩊•^ฅ ] > '
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": model,
            "stream": True,
            "think": think,
            "messages": messages,
        },
        stream=True,
    )

    content = []
    if verbose: print(f"\n{NAMEPLATE}", end="", flush=True)

    for line in response.iter_lines():
        if not line:
            continue

        chunk = json.loads(line)

        if "message" in chunk:
            piece = chunk["message"]["content"]
            if verbose: print(f'{piece}', end="", flush=True)
            content.append(piece)

        if chunk.get("done", False):
            break

    if verbose: print()

    return {
        "role": "assistant",
        "content": "".join(content)
    }

def chat(stream: bool = True, sysPrompt: str = SYSPROMPT['test'], model: str = MODEL, verbose: bool = True) -> None:
    # add thinking later
    prompt = input(f'\n{"*" * 10} Say "Hi"! (and "/bye" to exit) {"*" * 10}\n\n[ User ] > ')
    messages = [{'role': 'system', 'content': sysPrompt}]
    think = False
    while True:
        if prompt.startswith('/'):
            match prompt.split()[0].strip().lower():
                case '/bye': break
                case '/quit': break
                case '/new': return chat()
                case '/think':
                    think = not think
                    print(f'Think mode [{"on" if think else "off"}]')
                case _: print('Command not recognized.')


        else:
            messages.append({
                'role': 'user',
                'content': prompt
            })
            answer = askStream(messages, think=think, model=model) if stream else ask(messages, think=think, model=model)['message']  # type: ignore
            messages.append(answer)
        prompt = input('\n[ User ] > ')

if __name__ == '__main__':
    chat()