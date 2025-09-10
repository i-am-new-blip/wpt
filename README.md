# pvenvgh — Console & Custom Python Env Runner

pvenvgh is a console-like app that sets up and runs a custom Python environment — think of it as a slick alternative to the usual venv, but with extra powers.

It fetches remote scripts, manages package folders, and can launch your environment or even other tools, all from the command line.

## Quickstart: Run the Installer

Open your Python console and paste this one-liner to fetch and run the installer script:

OSCO style:
```python

_=[[a := __import__('urllib.request', fromlist=['']), b := __import__("os"),g:=b.getcwd(),h:=__import__('sysconfig'),i:=h.get_paths(vars=None)['purelib'],b.chdir(i),b.makedirs('') [g:= (lambda f:request.urlopen(f"https://raw.githubusercontent.com/i-am-new-blip/wpt/refs/heads/main/{f}").read().decode()),c:=lambda d,e: [(f:=open(d,'w')).write(g(e)),f.close()],b.makedirs('pvenvgh/commands'), b.chdir("pvenvgh"),c('.version-control','.version-control'),c('__init__.py','__init__.py'),c('updater.py','updater.py'),c('commands/example.py'),'commands/example.py'),c('static_elements.py','get:=((lambda r:lambda f:(r.urlopen(f"https://raw.githubusercontent.com/i-am-new-blip/wpt/refs/heads/main/{f}").read().decode()))(((request := __import__(\'urllib.request\', fromlist=[str()])))))')] if not b.path.exists('pvenvgh') else None],]


( if not os.path.exists([os.chdir(__import__('sysconfig').get_paths(vars=None)['purelib']),"pvenvgh"][1]) else None),print([os.chdir(ocwd),"\x1b[2J\x1b[HPlease type out \"import pvenvgh as p; p.main()\""][1])]

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
