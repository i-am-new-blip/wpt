import shlex

def split4lists(lst, sep):
    result = []
    current = []
    for item in lst:
        if item in sep:
            result.append(current)
            current = []
        else:
            current.append(item)
    result.append(current)
    return result

def understand_single_command(text: str):
    splitted = text.split(" ", 1)
    command = splitted[0]
    args = shlex.split(splitted[1]) if len(splitted) > 1 else []
    return command, args

def understand_line(text):
    tokenized = split4lists( shlex.split(text), ["|"] )
    JSON_tokens = []
    for token in tokenized:
      JSON_tokens.append(
        split4lists( token, list("><") )
      )
    return JSON_tokens

with open('.version-control') as f: v= f.read()

print(f'Welcome to pvenvgh v{v}')
t="\033[96m$ \033[0m"
l=3
while True:
    x=input(t)
    try:
        UL = understand_line(x)
        cmds = [understand_single_command(i) for i in UL]
        print(cmds)
    except: pass
        
    
