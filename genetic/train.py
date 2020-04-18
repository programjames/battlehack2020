import random
import json
import os

from robot import Robot
from run import run_game

def cross(weights1, weights2):
    return {key: (weights1[key] + weights2[key])/2 for key in weights1}

def mutate(weights, amount=1):
    return {key: weight + random.random() * 2 * amount - amount for key, weight in weights.items()}

def random_weights(keys, amount=10):
    return {key: random.random() * 2 * amount - amount for key in keys}

LOAD_FROM_FILE = True
if  LOAD_FROM_FILE:
    epoch = 0
    while os.path.isfile(f"saved_weights/epoch{epoch}.json"):
        epoch += 1
    with open(f"saved_weights/epoch{epoch-1}.json") as f:
        weightss = json.load(f)
else:
    keys = ["advanced", "chains", "count", "horizontal", "threats", "vertical", "wedges"]
    weightss = [random_weights(keys) for i in range(5)]
    epoch = 0

while epoch < 100:
    robots = [Robot(epoch, i, weights) for i, weights in enumerate(weightss)]
    wins = [0 for i in range(len(weightss))]
    for i, robot1 in enumerate(robots):
        for j, robot2 in enumerate(robots[:i]):
            winner = run_game(robot1.bot_directory, robot2.bot_directory)
            if winner == 0:
                wins[i] += 1
            else:
                wins[j] += 1
            print(".", end="", flush=True)
    print()
    wins, weightss = zip(*sorted(zip(wins, weightss), key=lambda x:x[0], reverse=True))

    with open(f"saved_weights/epoch{epoch}.json", "w") as f:
        f.write(json.dumps(weightss))

    new_weightss = [weightss[0]]
    for i in range(4):
        new_weightss.append(mutate(cross(random.choice(weightss[:3]), random.choice(weightss[:3]))))
    weightss = new_weightss

    with open(f"saved_weights/epoch{epoch}.json", "w") as f:
        json.dump(weightss, f)
     
    print(f"Epoch {epoch} completed!")
    epoch += 1
