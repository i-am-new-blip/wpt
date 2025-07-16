import os, sysconfig
ocwd = os.getcwd() # For readers | THIS EXISTS
#region setup
os.chdir(sysconfig.get_paths()['purelib']) #great!
if os.path.exists("pvenvgh"): exit()
os.makedirs(os.path.join('pvenvgh','commands')); os.chdir("pvenvgh")
with open('.version-control','w') as f: f.write(get('.version-control'))
with open('updater.py','w') as f: f.write(get('updater.py'))
with open(os.path.join('commands','example.py'),'w') as f: f.write(get("commands/example.py"))
with open('__init__.py','w') as f: f.write(get("__init__.py"))
#endregion
#region launch
del sysconfig,get,request
os.chdir(ocwd)
del os,ocwd
print("\x1b[2J\x1b[HPlease type out \"import pvenvgh as p; p.main()\"")
#endregion
