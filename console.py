from passgen import passgen
from os import system
from shutil import rmtree
from json import loads

with open("config.json") as jso:
    data = jso.read()
    jsodct = loads(data)
    jso.close()

os = jsodct["os"]

if os == "win":clear = "cls"
elif os == "unix":clear = "clear"
else:clear = "clear"

length = jsodct["length"]
charset = jsodct["charset"]

while True:
    rmtree("__pycache__")
    i = input("passgen>")
    if i == "gen":print(passgen(length, charset))
    elif i == clear:system(clear)
    else:continue
