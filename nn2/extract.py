# get a bot playable in the regular engine from weights.

import shutil, os, json
from robot import Robot

epoch = input("Epoch? ")
bot = 0

if "/" in epoch:
    epoch, bot = epoch1.split("/")
    bot = int(bot)


with open(f"saved_weights/epoch{epoch}.json") as f:
    weights = json.load(f)[bot]

name = input("Name? ")
r = Robot(name, weights)
if os.path.exists(name):
    shutil.rmtree(name)
shutil.copytree(r.bot_directory, name)

path = name + "/bot.py"
with open(path, "r") as f:
    code = f.read()
new_code = ""
for line in code.split("\n"):
    if len(line) > 300:
        s = ""
        lis = line.split(",")
        for x in lis:
            s += x + ",\n"
        s = s[:-2]
        line = s
    new_code += line + "\n"
with open(path, "w") as f:
    f.write(new_code)
