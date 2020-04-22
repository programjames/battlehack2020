import os

class Robot:
    def __init__(self, name, multipliers, root="robots/"):
        self.name = name
        self.bot_directory = os.path.join("robots/", name)
        self.file = os.path.join(self.bot_directory, "bot.py")
        with open("template.py") as f:
            self.code = f.read()
        
        for key, val in multipliers.items():
            self.code = self.code.replace(f"{{{key}_multiplier}}", str(val))
        if not os.path.isdir(self.bot_directory):
            os.mkdir(self.bot_directory)
        with open(self.file, 'w') as f:
            f.write(self.code)
