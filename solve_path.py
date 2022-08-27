from distutils.command.config import config
import os
import re

def path_solve(config="templates/"):
    os.chdir("/root/Server")
    for path,dir,file in os.walk(config):
        if (not file) or file[0]!="index.html":
            continue
        with open(path+"/"+file[0],"r") as f:
            f.seek(0)
            s=f.read()
        s=re.sub("/css/main.css","/static/css/main.css",s)
        s=re.sub("/css/noscript.css","/static/css/noscript.css",s)
        s=re.sub("/js/","/static/js/",s)
        print(path,dir,file)
        with open(path+"/"+file[0],"w") as f:    
            f.write(s)
if __name__=="__main__":
    path_solve()