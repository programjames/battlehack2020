name = input("Name? ")
path = name + "/bot.py"
with open(path, "r") as f:
    code = f.read()
code = code.replace("IN_TRAINING = True", "IN_TRAINING = False")
import os
os.mkdir(name+"_ready")
with open(name+"_ready/bot.py", "w") as f:
    f.write(code)
