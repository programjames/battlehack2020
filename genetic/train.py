import random
import json
import os
import time
import threading

from robot import Robot
from run import run_game

MAX_ROUNDS = 500
LOAD_FROM_FILE = True

def cross(weights1, weights2):
    return {key: (weights1[key] + weights2[key])/2 for key in weights1}

def mutate(weights, amount=1):
    return {key: weight + random.random() * 2 * amount - amount for key, weight in weights.items()}

def random_weights(keys, amount=10):
    return {key: random.random() * 2 * amount - amount for key in keys}

class ThreadManager():
    def __init__(self, robots):
        self.wins = [0 for i in range(len(robots))]
        self.games_finished = 0
        self.total = 5*len(robots)/2
        self.robots = robots
    def run_game(self, i, j):
        winner = run_game(self.robots[i].bot_directory, self.robots[j].bot_directory, board_size=16, max_rounds=MAX_ROUNDS)
        if winner == 0:
            self.wins[i] += 1
        else:
            self.wins[j] += 1
        self.games_finished += 1
        print(f"\r{round(self.games_finished/self.total*100, 1)}% complete!", end='')
    
    def new_game_thread(self, i, j):
        t = threading.Thread(target=self.run_game, args=(i, j))
        t.start()
        return t
        

keys = ["advanced", "back", "capture", "chains", "count", "filled",
        "horizontal", "promoted", "stalemate", "threats", "vertical", "wedges",
        "center", "distance_enemy", "distance_friendly", "finished", "left",
        "pawns"]

LOAD_FROM_FILE = True
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
    robots = [Robot(f"bot{i}", weights) for i, weights in enumerate(weightss)]
    tm = ThreadManager(robots)
    threads = []
    for i, robot1 in enumerate(robots):
        for c in range(5):
            j = i ^ (1 << c)
            threads.append(tm.new_game_thread(i, j))
    for needle in threads:
        needle.join()

    wins = tm.wins
    
    print(f"\r{round(game_counter/total*100, 1)}%", end='', flush=True)
            
    print()
    wins, weightss = zip(*sorted(zip(wins, weightss), key=lambda x:x[0], reverse=True))

    with open(f"saved_weights/epoch{epoch}.json", "w") as f:
        f.write(json.dumps(weightss))

    new_weightss = list(weightss[:4])
    for i in range(20):
        new_weightss.append(
            mutate(
                cross(
                    random.choice(weightss[:32]),
                    random.choice(weightss[:32]))
                )
            )
    for i in range(8):
        new_weightss.append(random_weights(keys))
    weightss = new_weightss

    with open(f"saved_weights/epoch{epoch}.json", "w") as f:
        json.dump(weightss, f)

    end = time.time()
    print(f"Epoch {epoch} completed!")
    print(f"Time for epoch = {end - start}")
    epoch += 1
