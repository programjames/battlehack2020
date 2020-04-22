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

    MAX_ROUNDS = 250

    p1 = sys.argv[1]
    p2 = sys.argv[2]

    c1 = CodeContainer.from_directory(p1)
    c2 = CodeContainer.from_directory(p2)

    game = Game([c1, c2], board_size=16, max_rounds=MAX_ROUNDS, debug=True, seed=None)
    start = time.time()
    while game.running:
        print('.', end='', flush=True)
        game.turn()
    print()
    end = time.time()
    print(f"Winner is {game.winner}")
    print(f"Time taken = {end - start}")
    viewer = FancyViewer(game.board_size, game.board_states, window_size=800)
    viewer.play(delay=0.1)
