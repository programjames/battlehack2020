import os

class Robot:
    def __init__(self, epoch, number, multipliers, max_rounds, root="robots/"):
        self.epoch = epoch
        self.number = number
        self.epoch_directory = os.path.join(root, f"epoch{self.epoch}/")
        self.bot_directory = os.path.join(self.epoch_directory, f"bot{self.number}/")
        self.file = os.path.join(self.bot_directory, "bot.py")
        with open("robot.py.template") as f:
            self.code = f.read()
        
        for key, val in multipliers.items():
            self.code = self.code.replace(f"{{{key}_multiplier}}", str(val))
        self.code = self.code.replace("{game_end}", str(max_rounds))
        if not os.path.isdir(self.epoch_directory):
            os.mkdir(self.epoch_directory)
        if not os.path.isdir(self.bot_directory):
            os.mkdir(self.bot_directory)
        with open(self.file, 'w') as f:
            f.write(self.code)
