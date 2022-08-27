from fileinput import filename
from sys import argv
from zoneinfo import available_timezones
import solve_path
import os
import re
import pickle
filesave_path="/root/Server/file_location.pkl"
def check_init():
    if not os.path.exists(filesave_path):
        print("Initing file_locations")
        with open(filesave_path,"wb") as f:
            init_dist={"about":"/root/Server/templates/"}
            pickle.dump(init_dist,f)
def clear(targetpath):
    tmp_con=os.getcwd()
    os.chdir(targetpath)
    for path,dir,file in os.walk(config):
        if (not file) or file[0]!="index.html":
            continue
        print("Directory {} Removed".format(path))
        os.system("rm -rf {}".format(path))
    os.chdir(tmp_con)
def determine_location(filename,dist):
    tmp_con=os.getcwd()
    os.chdir("/root/Server/templates")
    path=''
    while 1:
        print("Which directory would you wanna save?")
        available_dirs=[]
        for direc in os.listdir():
            if len(direc.split('.'))==1:
                available_dirs.append(direc)
        if not available_dirs:
            check=input("NO sub_directory| Create One?[Y/n]")
            if not check:
                pathname=input("input directory name:")
                os.mkdir(pathname)
                os.chdir(pathname)
                continue
            else:
                path=os.getcwd()
                break
        print(available_dirs)
        dir=input("Choice:[Input Create if you wanna create one]")
        if dir=="create":
            dir=input("New Directory Name:")
            if not os.path.exists(dir):
                os.mkdir(dir)
        if not os.path.exists(dir):
            print("No such directory")
            continue
        os.chdir(dir)
    os.chdir("/root/Server")
    dist[filename]=path
    with open(filesave_path,"wb") as f:#
        pickle.dump(dist,f)
    os.chdir(tmp_con)
cp_configs=['/root/Blog/public/2022','/root/Blog/public/about']
config="/root/Server/templates"
os.chdir("/root/Blog")
if len(argv)>1:
    if argv[1]=='c':
        os.system("hexo clean")
        clear(config)
    if argv[1]=='g':
        os.system("hexo g")
    if argv[1]=='s':
        os.system("hexo s")
    if len(argv)>2 and argv[1]=='n':
        filename=argv[2]
        os.system("hexo n {}".format(filename))
        check_init()
        with open(filesave_path,"rb") as f:# store a dist of {article name:absolute path}
            dist=pickle.load(f)
        if not filename in dist:
            print("New files Detected")
            determine_location(filename,dist)
        else:
            print("Already Saved Path\nSaving in {}".format(dist[filename]))
    exit(0)
if not os.path.exists("public"):
    print("Files not generated yet")
    exit(0)
check_init()
with open(filesave_path,"rb") as f:# store a dist of {article name:absolute path}
    dist=pickle.load(f)
for cp_config in cp_configs:
    for path,dir,file in os.walk(cp_config):
        if not file:
            continue
        if not file[0]=="index.html":
            continue
        print("generating {}/{}".format(path,file[0]))
        #print("cp -r {} {}".format(path,dist[path.split('/')[-1]]))
        dirname=path.split('/')[-1]
        if not dirname in dist:
            print("file {}|Path not defined".format(dirname))
            determine_location(dirname,dist)
        os.system("cp -r {} {}".format(path,dist[dirname]))
solve_path.path_solve()

