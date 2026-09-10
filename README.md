# what is fwordle?

Essentially a joke project, but also a vehicle for me to practice:

- git/github
- deep learning
- general programming

For anyone who is not me, fwordle could possibly provide a mild 
quantity of amusement or utility.

It generates these things:

Wordle 1,894 3/6*

🟨🟩⬛⬛🟩

⬛🟩🟨🟨🟩

🟩🟩🟩🟩🟩

without you having to play wordle.

# generating the cards

There are now two ways to generate a wordle card. The first is
to use the classical method (detailed below): a script called
`solver.py` actually creates and solves a wordle puzzle, 
generating the data that becomes the card. 

Run `bash fwordle.sh` in the directory to generate a card this
way.

The second, newer method, is to use a multi-layer perceptron
which has been trained on a dataset of 10,000 cards (generated
by `solver.py`) to generate new cards which it thinks are 
statistically-likely. 

Run `bash fwordle_gen.sh` in the directory to generate a card
this way.

# classical solution

`solver.py ` selects a random valid wordle guess and tries to 
solve it by literally playing wordle (locally, all the logic is
in solver.py). The algorithm isn't optimized yet (it reuses 
letters it should know from feedback are not in the word), but 
it manages to solve in 6 or less ~70% of the time. It passes 
its output (the feedback it received) to raw.txt. Each line is
output as a 5-long base three number: 2 for green, 1 for yellow
0 for black. Five periods `.....` represents the start/end.

wrapper.py then reads in raw.txt, does some math to figure out
what number wordle this should be based on the current time
(currently configured for west coast), and generates the card
with the proper emojis, based on the base-3 numbers.

# (current) ML solution

The current ML solution uses a multi-layer perceptron with a
ten dimensional embedding matrix (using lines as tokens)
one hidden tanh layer, and a softmax layer with cross entropy
loss. The network was trained on 100,000 wordle outputs generated
by `solver.py` using standard backpropagation. After cross 
validation, the best performing model had six embedding dimensions,
200 hidden neurons, and was trained on 150,000 iterations of 
gradient descent, with a learning rate of 0.1 for the first
75,000 iterations, and 0.01 for the second 75,000. It had a
dev loss of 2.2620, and a test loss of 2.2706.

# known bugs

wrapper.py: the classical solver and the MLP output in slightly
different formats, and wrapper.py handles these with a series 
of confusing if statements which sometimes produce an incorrect
count (e.g. X/6* despite the card showing a solve in <=6).
Plan to split into two separate wrapper scripts.

MLP: has learned structure much better, but still outputs
impossible cards ~10% of the time (typically by violating hard
mode rules).

# future:
Three outstanding fixes: model optimizations, detailed above,
train on a larger dataset (10k cards only took ~5 mins to 
generate on my macbook so could be bumped up to 100k or so
just letting it run overnight), and fix `solver.py ` so its
win-rate is a little better.

In the far future, possibly overhaul the model architecture.
This MLP (taken from Bengio et al 2003 via Andrej Karpathy)
is the first model design I came across that was up to the 
task. There are probably more suitable architectures, of 
which I am presently ignorant.

# thanks
Thanks to GitHub user dracos for the list of valid wordle words,
and to Andrej Karpathy for his excellent 'Zero to Hero' series 
on youtube, which is at this time my chief deep learning resource.
