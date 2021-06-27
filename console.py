from passgen import passgen
from os import system
import json

with open("config.json") as jso:
    data = jso.read()
    jsodct = json.loads(data)
    jso.close()

os = jsodct["os"]

if os == "win":clear = "cls"
elif os == "unix":clear = "clear"
else:clear = "clear"

length = jsodct["length"]
charset = jsodct["charset"]

while True:
    with open("config.json", "w") as jso:
        jso.write(json.dumps(jsodct))
        jso.close()
    
    i = input("passgen>")
    if i == "gen":print(passgen(length, charset))
    elif i == clear:system(clear)
    elif i == "win":
        jsodct["os"] = "win"
    elif i == "unix":
        jsodct["os"] = "unix"
    elif i == "else":
        jsodct["os"] = "else"
    else:continue
