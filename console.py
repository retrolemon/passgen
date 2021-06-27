from passgen import passgen
from os import system
import json
import sys

while True:
    with open("config.json") as jso:
        data = jso.read()
        jsodct = json.loads(data)
        jso.close()
    
    clear = jsodct["clear"]
    length = jsodct["length"]
    charset = jsodct["charset"]
    
    i = input("passgen>")
    if i == "gen":print(passgen(length, charset))
    elif i == clear:system(clear)
    elif i == "exit":sys.exit()
    else:continue
