import os
import json
os.chdir("/root/Server/templates")
objs={}
def walk(path):
    sons=[]
    for direc in os.listdir('./'):
        if len(direc.split('.'))>1:
            continue
        sons.append(direc)
    if not sons:
        return
    objs[path]=sons
    for son in sons:
        os.chdir(son)
        walk(son)
        os.chdir('../')
if __name__=="__main__":
    walk('.')
    print(objs)
    with open("/root/Server/templates/tree.json","w") as f:
        json.dump(objs,f)
