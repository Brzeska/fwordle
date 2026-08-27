# note

This project is mostly being created as a vehicle for me to learn git/github, as well as a little machine learning

# fwordle

Automatic wordle emoji card generator. Currently, solver.py 
selects a random valid wordle guess and tries to solve it by
literally playing wordle (locally, all the logic is in solver.py).
The algorithm isn't optimized yet (it reuses letters it should 
know from feedback are not in the word), but it manages to solve
in 6 or less ~70% of the time. It passes its output (the feedback
it received) to raw.txt

wrapper.py then reads in raw.txt, does some math to figure out
what number wordle this should be based on the current time
(currently configured for west coast), and generates the card
with the proper emojis.

Now you can feel included with your friends without ever having
to play wordle

# future:
The goal is to use the current system to generate thousands (or
more) of sample cards, then to use ML techniques (details to be
filled in later) to teach the computer to generate cards without
actually solving a sample puzzle, since ideally even our machines 
should be spared from having to play wordle.

# how to run
Go into the directory and type `zsh fwordle.sh`
