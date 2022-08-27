import os
from unicodedata import name
import pickle
import json
from flask import Flask,request,render_template,url_for,redirect,abort
filesave_path="/root/Server/file_location.pkl"
ip_path="/root/Server/visit_ip.json"
dist={}
ips={}
app=Flask(__name__,static_url_path='',static_folder='.')
@app.route("//")
def front_index():
    if not request.remote_addr in ips:
        ips[request.remote_addr]=0
    ips[request.remote_addr]+=1
    return render_template("index.html")
@app.route("/about/")
def hello():
    return render_template("about/index.html")
@app.route("/content/<string:name>/")#access to certain html
def return_name(name):
    return render_template("{}/{}/index.html".format(dist[name].split('templates/')[1],name),name=name)
if __name__=='__main__':
    with open(ip_path,"r") as f:
        ips=json.load(f)
    with open(filesave_path,"rb") as f:# store a dist of {article name:absolute path}
        dist=pickle.load(f)
    app.run("0.0.0.0",port=80)
    with open(ip_path,"w") as f:
        json.dump(ips,f)
    exit(0)
        
    #app.run("0.0.0.0")