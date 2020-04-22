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


if __name__ == "__main__":
    MAX_ROUNDS = 250
    GAMES = 20

    wins = [0, 0]
    
    p1 = sys.argv[1]
    p2 = sys.argv[2]

    c1 = CodeContainer.from_directory(p1)
    c2 = CodeContainer.from_directory(p2)

    for i in range(GAMES):
        game = Game([c1, c2], board_size=16, max_rounds=MAX_ROUNDS, debug=True, seed=None, random_pieces=2)
        while game.running:
            game.turn()
        if game.winner == Team.WHITE:
            wins[0] += 1
        else:
            wins[1] += 1
        
        os.system("cls")
        print(f"{round((i+1)/GAMES*100, 2)}% complete.\nCurrent ratio:")
        print(f"{wins} --> {round(wins[0] / (wins[0] + wins[1]) * 100, 2)}%")

