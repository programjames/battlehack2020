import random
import json
import os
import time
import multiprocessing
import sys

from robot import Robot
from run import run_game

MAX_ROUNDS = 500
SHAPE = [27, 16, 16, 4]
LOAD_FROM_FILE = True

def cross(weights1, weights2):
    return {key: [(weights1[key][i] + weights2[key][i])/2 for i in range(len(weights1[key]))] for key in weights1 if key in weights2}

def mutate(weights, amount=1):
    return {key: [w + random.random() * 2 * amount - amount for w in ws] for key, ws in weights.items()}

def random_weight(amount=10):
    return random.random() * 2 * amount - amount

def random_weights(num, amount=10):
    return [random_weight(amount) for i in range(num)]

def random_dict_weights(keys, amount=10):
    return {key: random_weights(keys[key], amount) for key in keys}

class ProcessManager():
    def __init__(self, robots=None):        
        self.games_finished = multiprocessing.Value('i', 0)
        if robots is not None:
            self.wins = multiprocessing.Array('i', len(robots))
            self.robots = robots

    def new_robots(self, robots):
        self.wins = multiprocessing.Array('i', len(robots))
        self.games_finished.value = 0
        self.robots = robots
    
    def run_game(self, dir1, dir2, i, j):
        winner = run_game(dir1, dir2, board_size=16, max_rounds=MAX_ROUNDS)
        if winner == 0:
            self.wins[i] += 1
        else:
            self.wins[j] += 1
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

    num_weights = sum(SHAPE[i]*SHAPE[i+1] for i in range(len(SHAPE) - 1))
    num_biases = sum(SHAPE[i+1] for i in range(len(SHAPE) - 1))
    keys = {"weight_list": num_weights,
            "biases_list": num_biases}

    if  LOAD_FROM_FILE:
        epoch = 0
        while os.path.isfile(f"saved_weights/epoch{epoch}.json"):
            epoch += 1
        with open(f"saved_weights/epoch{epoch-1}.json") as f:
            weightss = json.load(f)
            for weights in weightss:
                for key in keys:
                    if key not in weights:
                        weights[key] = random_weights(keys[key])
    else:
        weightss = [random_dict_weights(keys) for i in range(32)]
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

        wins = pm.wins
                
        print()
        wins, weightss = zip(*sorted(zip(wins, weightss), key=lambda x:x[0], reverse=True))

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
            new_weightss.append(random_dict_weights(keys))
        weightss = new_weightss

        with open(f"saved_weights/epoch{epoch}.json", "w") as f:
            json.dump(weightss, f)

        end = time.time()
        print(f"Epoch {epoch} completed!")
        print(f"Time for epoch = {end - start}")
        epoch += 1
