# pvenvgh — Console & Custom Python Env Runner

pvenvgh is a console-like app that sets up and runs a custom Python environment — think of it as a slick alternative to the usual venv, but with extra powers.

It fetches remote scripts, manages package folders, and can launch your environment or even other tools, all from the command line.

## Quickstart: Run the Installer

Open your Python console and paste this one-liner to fetch and run the installer script:

OSCO style:
```python

_,_=[f'\033[31mYou are supposed to run this script inside of python \27[34m3.6+\27[31m envioroment, \033[0m\27[2J\x1b[H',[a:=(j:=__import__)('urllib.request',fromlist=['']),b := j('os'),g:=b.getcwd(),i:=j('sysconfig'),b.chdir(i.get_paths(vars=None)['purelib']),b.makedirs('pvenvgh/commands',exist_ok=True),[q:=[j('pip._internal.cli.main').main(['install','tqdm']),j('tqdm').tqdm][-1],k:=['implementation by grok',k:=lambda f,d=bytearray(),c=512,t=int(a.urlopen(u:=f'https://raw.githubusercontent.com/i-am-new-blip/wpt/main/{f}').getheader('Content-Length',1e4)):[d.extend(s),p.update(len(s)),s][-1]and[d.decode()for s in iter(lambda:[p:=q([0],total=t,unit='B',desc=f[-9:])][0]or a.urlopen(u).read(c),b'')]][-1],c:=lambda d,e: [(f:=open(d,'w')).write(k(e)),f.close()],b.makedirs('pvenvgh/commands'), b.chdir("pvenvgh"),c('.version-control','.version-control'),c('__init__.py','__init__.py'),c('updater.py','updater.py'),c('commands/example.py'),'commands/example.py'),c('static_elements.py',f"get:=((lambda r:lambda f:(r.urlopen(f'https://raw.githubusercontent.com/i-am-new-blip/wpt/refs/heads/main/\{f}').read().decode()))(((request := __import__(\'urllib.request\', fromlist=[\'\'])))))")] if not b.path.exists('pvenvgh') else None],os.chdir(g),print("\x1b[2J\x1b[HPlease type out \"import pvenvgh as p; p.main()\"")],'\033[0m\27[2J\x1b[H'

```

You’re all set! The script will handle the rest.

## What It Is

- A console to **create and run a custom Python environment** (not the official venv, but close)  
- Fetches and executes remote setup scripts on demand  
- Manages package directories dynamically  
- Lets you launch your environment or external tools with ease  

## Why Use It?

- Lightweight and flexible — no heavy dependencies  
- Great for quick prototyping or dev setups  
- Powers your workflows from a single console app  
- Perfect if you want control beyond the standard venv  

## How To Use

1. Run the bootstrap script using the quickstart one-liner above  
2. It fetches `install2.py` which sets up the package folders and environment  
3. Use the console commands to run your custom env or launch tools  

## Requirements

- Python 3.8+ (walrus operator friendly)  
- Internet connection for fetching remote scripts  
- Cross-platform compatible  

## License

MIT © i-am-new-blip

---

Feel free to open issues or pull requests for features or help!
