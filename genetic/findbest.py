import os, sys, json, time, math
from battlehack20 import CodeContainer, Game
import battlehack20
Team = battlehack20.game.team.Team
from robot import Robot
import time

def update_elo(e1, e2, r, k=10):
    p1 = 1/(1+math.pow(10, (e1-e2)/400))
    p2 = 1 - p1
    return e1 + k*(r-p1), e2 + k*(p2-r)

def run_game(dir1, dir2, board_size=16, max_rounds=250, debug=False):
    c1 = CodeContainer.from_directory(dir1)
    c2 = CodeContainer.from_directory(dir2)
    game = Game([c1, c2], board_size=board_size, max_rounds=max_rounds, debug=debug, seed=None)
    while game.running:
        game.turn()
    return game.winner.value

epoch_start = 50
epoch_end = 130

elos = [1500 for i in range(epoch_end - epoch_start)]

total = ((epoch_end - epoch_start)**2 - (epoch_end - epoch_start))//2
t = 0
for x, epoch1 in enumerate(range(epoch_start, epoch_end)):
    for y, epoch2 in enumerate(range(epoch1 + 1, epoch_end)):
        t += 1
        bot1 = 0
        bot2 = 0
        with open(f"saved_weights/epoch{epoch1}.json") as f:
            weights1 = json.load(f)[bot1]
            
        with open(f"saved_weights/epoch{epoch2}.json") as f:
            weights2 = json.load(f)[bot2]
        
        r1 = Robot("test1", weights1)
        r2 = Robot("test2", weights2)
        c1 = CodeContainer.from_directory(r1.bot_directory)
        c2 = CodeContainer.from_directory(r2.bot_directory)

        game = Game([c1, c2], board_size=16, max_rounds=500, debug=False, seed=None)
        while game.running:
            game.turn()
        os.system("cls")
        print(f"{round(t/total*100, 2)}% complete.\nCurrent best:")
        r = 1 if game.winner == Team.WHITE else 0
        e1, e2 = update_elo(elos[x], elos[y], r)
        elos[x] = e1
        elos[y] = e2
        n = 10
        top = sorted(range(len(elos)), key=lambda i: elos[i], reverse=True)[:n]
        for i in range(n):
            print(f"{i+1}. {top[i] + epoch_start} - {round(elos[top[i]], 1)}", flush=True)

        with open("elos.json", "w") as f:
            json.dump(elos, f)

