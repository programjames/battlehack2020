# Battlehack 2020
## By D5: programjames & cooljoseph

Here's the code for the genetic algorithm you've all been waiting for. Lots of duplicated files, because lots of changes in the last day of Battlehack and we didn't want to break anything.
A quick rundown of the repo and different things we did:

1. `genetic/bh20min/`

This folder contains the `custom` branch of the `battlehack20-minimal` engine. It runs around 30x faster than Teh Dev's
engine at the sacrifice of not checking for illegal moves, and not putting tape around people's code. It also lets you
import whatever you want, so it's ideal for training. The difference between the `custom` and `master` branches is that
the `custom` gives a "partial" win. So, you may get 0.9 points instead of 1 point for a win.

2. `genetic/`

The rest of this folder is the code used to train our heuristic-based genetic algorithm. Basically, we made a bunch of heuristics to
determine how good a position was: how many pawns are diagonal to each other? an our pawn get captured in this position? etc. We did
the same thing with the overlords. You can check out `template.py` for all of the heuristics.

The file `train.py` does what you would assume; it trains the bots. The "genes" are a bunch of weights that are placed into the template
file to make a bot. Then, the bots play against each other. The top survive, and the rest are mutated from the top bots or are completely
new random bots.

One issue we found with this heuristic was the linearity. After a certain point it couldn't learn any further. So, we decided to introduce
a (simple) neural net to get rid of this linearity.

3. `nn/`

This was the first attempt at a neural net. The other folders, `nn2` and `nn3` were similar but with slightly different template files
and we didn't want to lose our initial training (and were too lazy to delete the previous folders). Instead of a bunch of heuristics,
we made a small neural network (`27 inputs --> 8 --> 8 --> 4 outputs`) with the sigmoid activator. The "genes" (which we called weights
throughout our code) corresponded to the weights in the neural network. There were of course now dozens more genes, and it took a little
longer to train. We were able to use `numpy` for training though which sped it up. Another thing I should mention is that we used
multiprocessing to speed up training. This way we could have 5 or more games running at once. Overall, we sped up training by several
hundred (or maybe several thousand?) times compared to when using the restricted engine.

4. `nn2/superbot/` (And the other places it is copied to.)

This was a handcrafted bot Joseph made. We were hoping for one of our machine learning bots to eventually be able to beat it. The
closest we got was around a 30% winrate by epoch (generation) 124 in `nn2/` (run `extract.py` to grab the code for this bot). We think
with more training time our neural net would have eventually beat this bot. Unfortunately, we only started training the neural net the
night before the submission deadline, so we only got a few hundred generations in.

5. Miscellaneous

These files are copied in several locations and pretty much all do the same thing.


`run.py` - Runs a match between two epochs. You can specify the bot within the epoch as well. Usage:
```
run.py epoch1/num epoch2/num <max rounds>
```

`r.py` - It runs a match between two bots on the `battlehack20-minimal` engine. Usage:
```
r.py folder1 folder2
```

`extract.py` - It makes a folder with a `bot.py` file out of an epoch (using the `saved_weights/<epoch>.json` file). Usage:
```
extract.py
Epoch? <epoch>
Name? <save-folder>
```

`ready.py` - Changes the line `IN_TRAINING = True` to `IN_TRAINING = False` for our neural net bots. Usage:
```
ready.py
Name? <Name of folder with bot.py>
```
