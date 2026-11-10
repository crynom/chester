import requests, json

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

    return resp['message']

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
    THINKING = True
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

    endThoughts = False
    for line in response.iter_lines():
        if not line:
            continue

        chunk = json.loads(line)

        if "message" in chunk:
            piece = chunk["message"]["content"]
            if verbose and (not THINKING or think): print(f'{piece}', end="", flush=True)
            content.append(piece)
            if endThoughts: THINKING = False # dumb way to skip the token after thoughts (new line)
            if '/think' in piece: endThoughts = True

        if chunk.get("done", False):
            break

    if verbose: print()

    return {
        "role": "assistant",
        "content": "".join(content)
    }