from battlehack20 import CodeContainer, Game
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

    MAX_ROUNDS = 500

    epoch1 = sys.argv[1]
    bot1 = 0
    epoch2 = sys.argv[2]
    bot2 = 0

    if "/" in epoch1:
        epoch1, bot1 = epoch1.split("/")
        bot1 = int(bot1)

    if "/" in epoch2:
        epoch2, bot2 = epoch2.split("/")
        bot2 = int(bot2)
    
    
    with open(f"saved_weights/epoch{epoch1}.json") as f:
        weights1 = json.load(f)[bot1]
        
    with open(f"saved_weights/epoch{epoch2}.json") as f:
        weights2 = json.load(f)[bot2]
    
    r1 = Robot("test", weights1)
    r2 = Robot("test", weights2)
    c1 = CodeContainer.from_directory(r1.bot_directory)
    c2 = CodeContainer.from_directory(r2.bot_directory)

    game = Game([c1, c2], board_size=16, max_rounds=MAX_ROUNDS, debug=False, seed=None)
    start = time.time()
    while game.running:
        print('.', end='', flush=True)
        game.turn()
    print()
    end = time.time()
    print(f"Winner is {game.winner}")
    print(f"Time taken = {end - start}")
    viewer = FancyViewer(game.board_size, game.board_states, window_size=800)
    viewer.play(delay=0.02)
