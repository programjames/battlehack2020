from battlehack20 import CodeContainer, Game

def run_game(dir1, dir2, board_size=16, max_rounds=250):
    c1 = CodeContainer.from_directory(dir1)
    c2 = CodeContainer.from_directory(dir2)
    game = Game([c1, c2], board_size=board_size, max_rounds=max_rounds, debug=False)
    while game.running:
        game.turn()
    return game.winner.value

if __name__ == "__main__":
    import os, json
    from fancyviewer import FancyViewer
    from robot import Robot
    
    epoch = 0
    while os.path.isfile(f"saved_weights/epoch{epoch}.json"):
        epoch += 1
    epoch -= 1
    epoch = 0
    with open(f"saved_weights/epoch{epoch}.json") as f:
        weightss = json.load(f)
    weights1 = weightss[0]
    weights2 = weightss[1]
    r1 = Robot("test", "1", weights1)
    r2 = Robot("test", "2", weights2)
    c1 = CodeContainer.from_directory(r1.bot_directory)
    c2 = CodeContainer.from_directory(r2.bot_directory)
    game = Game([c1, c2], board_size=16, max_rounds=100, debug=False)
    while game.running:
        game.turn()
    print(f"Winner is {game.winner}")
    viewer = FancyViewer(game.board_size, game.board_states, window_size=800)
    viewer.play(delay=0.5)
