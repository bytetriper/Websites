from fileinput import filename
import os
import pickle
filename="/root/Server/file_location.pkl"
with open(filename,"rb") as f:
    file=pickle.load(f)
    print(file)