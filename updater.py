from static_elements import request, get 
import json, os, hashlib

def is_outdated():
  with open('.version-control') as f:
    return f.read().strip() != get('.version-control').strip()

def list_github_files():
    req = request.Request("https://api.github.com/repos/i-am-new-blip/wpt/contents/", headers={'User-Agent': 'Mozilla/5.0'})
    with request.urlopen(req) as response:
        data = json.loads(response.read().decode())
    return [item['name'] for item in data if item['type'] == 'file']

def attempt_to_update():
  if not is_outdated(): return
  files = list_github_files()
  for name in files:
    try:
      with open(name,'w',encoding='utf-8') as f:
        f.write(get(name))
    except Exception as e:
      print(f"Failed to update {name}: {e}")

