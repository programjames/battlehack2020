# get a bot playable in the regular engine from weights.

import shutil, json
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
shutil.copytree(r.bot_directory, name)
