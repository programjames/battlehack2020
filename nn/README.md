## Neural Nets

We found while training the heuristic-based genetic algorithm (this was when pawns also were being trained with a heuristic) that the bot
peaked around generation 70 and didn't seem to be able to improve much more after that (see `../genetic/findbest.py`; it takes a while to
run, but the results are that the bot ends up peaking and then declining). We decided that the issue was with linearity, so we decided to
make a neural net to introduce some non-linearity to it. This happened the night before submissions were due, and in the morning we changed
up the neural net a bit. To avoid losing code that was already trained, we just copied the entire folder so that's why `../nn2` and `../nn3`
exist. Actually, `nn2` is where the "final" neural net code is, but we know you're going to click on this folder first.

Okay, so how does this actually work? I initially wanted to do some deep reinforcement learning earlier in the week (see
[here](https://towardsdatascience.com/qrash-course-deep-q-networks-from-the-ground-up-1bbda41d3677) for a brief overview on reinforcement
learning). But that would require a *lot* of changes to the engine to allow it to send rewards to each player and have each player
update their q-tables. So, we went with the heuristic genetic algorithm in `../genetic/`. However, when we realized that we needed
non-linearity, we adapted the genetic algorithm. Instead of the genes determining weights for each heuristic, the genes determined the
weights and biases in a neural net!

The neural net is pretty basic. It uses the sigmoid activation function, and has 27 input nodes, 2 hidden layers with 8 nodes each, and
then 4 outputs (`27 --> 8 --> 8 --> 4`). So, there needs to be a total of 332 different genes to train the neural net. At first we
worried that the neural network would be too big, and training would take much too long. But, by using `numpy` for the neural network, it
actually took about the same long to run each game as with the heuristic-based genetic algorithm. Overall, each generation took around
2 minutes to run (on our computers), so we were able to get around 200 generations in before the submission deadline.

Unfortunately, this wasn't enough. With more time, the neural net bots could have improved a lot more. As it is, the best ended up with
only a 30% winrate against our hard-coded bot (which wasn't a top bot anyway).

### Overlord

We determined how our overlord placed pawns by taking our hard-coded bot for the pawns, and using a genetic algorithm for the overlord.
Actually, this is what is currently in `../genetic/`. Then, once we found good weights for the overlord (once the performance peaked),
we copied them over to `template.py`. So, the overlord was trained independently and was deterministic while we trained just the pawns
with the neural net.

### Pawns

Each pawn took the 25 squares it could see, as well as its row and column, as inputs to a neural net. The 4 outputs determined how
strong the different moves (sitting, moving forward, capturing left or right) were. The pawns moved forward as fast as they could to
begin, until they saw an enemy pawn. Then, they switched over to obeying their neural nets. Whenever the pawn had an opportunity to
capture, it always would. The neural net broke ties if it could capture two different enemies. Otherwise, if the pawn couldn't capture
anything, the neural net decided whether the pawn should move forward or stay still.

It turns out that the pawns were not nearly aggressive enough when they were close to the spawn point. So, we ended up just setting
row to be always equal to 0.5, or halfway across the board, because they performed much better there. The pawns performed much better
and even started beating hard-coded bots!
