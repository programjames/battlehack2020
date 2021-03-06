import random
import json
import os
import time
import multiprocessing
import sys
import math

from robot import Robot
from run import run_game

MAX_ROUNDS = 500
RANDOM_PIECES = 10
LOAD_FROM_FILE = False

def cross(weights1, weights2):
    return {key: (weights1[key] + weights2[key])/2 for key in weights1}

def mutate(weights, amount=1):
    return {key: weight + random.random() * 2 * amount - amount for key, weight in weights.items()}

def random_weight(amount=10):
    return random.random() * 2 * amount - amount

def random_weights(keys, amount=10):
    return {key: random_weight(amount) for key in keys}

def update_elo(e1, e2, r, k=10):
    p1 = 1/(1+math.pow(10, (e1-e2)/400))
    p2 = 1 - p1
    return e1 + k*(r-p1), e2 + k*(p2-r)

class ProcessManager():
    def __init__(self, robots=None):        
        self.games_finished = multiprocessing.Value('i', 0)
        if robots is not None:
            self.new_robots(robots)

    def new_robots(self, robots):
        self.elos = multiprocessing.Array('f', len(robots))
        for i in range(len(self.elos)):
            self.elos[i] = 1500
        self.games_finished.value = 0
        self.robots = robots
    
    def run_game(self, dir1, dir2, i, j):
        result = run_game(dir1, dir2, board_size=16, max_rounds=MAX_ROUNDS, random_pieces=RANDOM_PIECES)
        elo1, elo2 = self.elos[i], self.elos[j]
        elo1, elo2 = update_elo(elo1, elo2, result)
        self.elos[i], self.elos[j] = elo1, elo2
        self.games_finished.value += 1

    def print_progress(self):
        while True:
            print(f"\r{round(self.games_finished.value/1.60, 1)}% complete!", end='')
            time.sleep(1)
            sys.stdout.flush()
    
    def new_game(self, i, j):
        p = multiprocessing.Process(target=self.run_game, args=(self.robots[i].bot_directory, self.robots[j].bot_directory, i, j))
        p.start()
        return p

if __name__ == "__main__":

    keys = ["advanced", "back_filled", "capture", "count", "neighbors",
            "support", "threats", "vertical", "center", "distance_enemy",
            "distance_friendly", "finished", "pawns", "odd"]

    if  LOAD_FROM_FILE:
        epoch = 0
        while os.path.isfile(f"saved_weights/epoch{epoch}.json"):
            epoch += 1
        with open(f"saved_weights/epoch{epoch-1}.json") as f:
            weightss = json.load(f)
            for weights in weightss:
                for key in keys:
                    if key not in weights:
                        weights[key] = random_weight()
    else:
        weightss = [random_weights(keys) for i in range(32)]
        epoch = 0

    pm = ProcessManager()    
    proc = multiprocessing.Process(target=pm.print_progress)
    proc.start()
    
    while epoch < 1000:
        start = time.time()
        robots = [Robot(f"bot{i}", weights) for i, weights in enumerate(weightss)]
        pm.new_robots(robots)
        processes = []
        for i, robot1 in enumerate(robots):
            for c in range(5):
                j = i ^ (1 << c)
                processes.append(pm.new_game(i, j))
        for proc in processes:
            proc.join()

        elos = pm.elos
                
        print()
        elos, weightss = zip(*sorted(zip(elos, weightss), key=lambda x:x[0], reverse=True))
        
        with open(f"saved_weights/epoch{epoch}.json", "w") as f:
            f.write(json.dumps(weightss))

        new_weightss = list(weightss[:4])
        for i in range(20):
            new_weightss.append(
                mutate(
                    cross(
                        random.choice(weightss[:8]),
                        random.choice(weightss[:8]))
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
