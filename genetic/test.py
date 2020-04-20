from battlehack20 import CodeContainer, Game
import battlehack20
Team = battlehack20.game.team.Team

import time

def run_game(dir1, dir2, board_size=16, max_rounds=250, debug=False):
    c1 = CodeContainer.from_directory(dir1)
    c2 = CodeContainer.from_directory(dir2)
    game = Game([c1, c2], board_size=board_size, max_rounds=max_rounds, debug=debug, seed=None)
    while game.running:
        game.turn()
    return game.winner.value

if __name__ == "__main__":
    import os, sys, json, time
    from fancyviewer import FancyViewer
    from robot import Robot

##    if len(sys.argv) >= 2:
##        epoch = sys.argv[1]
##    else:
##        epoch = 0
##        while os.path.isfile(f"saved_weights/epoch{epoch}.json"):
##            epoch += 1
##        epoch -= 1
##        print(f"Using epoch {epoch}")
##    
##    with open(f"saved_weights/epoch{epoch}.json") as f:
##        weights = json.load(f)[0]
##        
##    r1 = Robot("test1", weights)
##    c1 = CodeContainer.from_directory(r1.bot_directory)
    c1 = CodeContainer.from_directory("testbot")
    c2 = CodeContainer.from_directory("examplefuncsplayer")
    w = 0
    l = 0
    for test in range(10):
        game = Game([c1, c2], board_size=16, max_rounds=250, debug=False, seed=None)
        while game.running:
            game.turn()
        if game.winner == Team.WHITE:
            w += 1
        else:
            l += 1
        print(round(w/(w+l)*100, 2))
    viewer = FancyViewer(game.board_size, game.board_states, window_size=800)
    viewer.play(delay=0.5)
