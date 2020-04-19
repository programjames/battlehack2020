import random
import json
import os
import time

from robot import Robot
from run import run_game

def cross(weights1, weights2):
    return {key: (weights1[key] + weights2[key])/2 for key in weights1}

def mutate(weights, amount=1):
    return {key: weight + random.random() * 2 * amount - amount for key, weight in weights.items()}

def random_weights(keys, amount=10):
    return {key: random.random() * 2 * amount - amount for key in keys}

keys = ["advanced", "back", "captured", "chains", "column", "count", "horizontal", "offense",
        "promoted", "threats", "vertical", "wedges"]

LOAD_FROM_FILE = False
if  LOAD_FROM_FILE:
    epoch = 0
    while os.path.isfile(f"saved_weights/epoch{epoch}.json"):
        epoch += 1
    with open(f"saved_weights/epoch{epoch-1}.json") as f:
        weightss = json.load(f)
else:
    weightss = [random_weights(keys) for i in range(32)]
    epoch = 0

while epoch < 1000:
    start = time.time()
    robots = [Robot(epoch, i, weights) for i, weights in enumerate(weightss)]
    wins = [0 for i in range(len(weightss))]
    for i, robot1 in enumerate(robots):
        for c in range(5):
            j = i ^ (1 << c)
            robot2 = robots[j]
            winner = run_game(
                robot1.bot_directory,
                robot2.bot_directory,
                board_size=10,
                max_rounds=200,
                debug=False
                )
            if winner == 0:
                wins[i] += 1
            else:
                wins[j] += 1
            print(".", end="", flush=True)
            
    print()
    wins, weightss = zip(*sorted(zip(wins, weightss), key=lambda x:x[0], reverse=True))

    with open(f"saved_weights/epoch{epoch}.json", "w") as f:
        f.write(json.dumps(weightss))

    new_weightss = list(weightss[:4])
    for i in range(24):
        new_weightss.append(
            mutate(
                cross(
                    random.choice(weightss[:8]),
                    random.choice(weightss[:8]))
                )
            )
    for i in range(4):
        new_weightss.append(random_weights(keys))
    weightss = new_weightss

    with open(f"saved_weights/epoch{epoch}.json", "w") as f:
        json.dump(weightss, f)

    end = time.time()
    print(f"Epoch {epoch} completed!")
    print(f"Time for epoch = {end - start}")
    epoch += 1
