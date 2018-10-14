import requests

with open("simple.py","r") as f:
    r = requests.post("http://localhost:8888/post/", files={"files_index":f})
