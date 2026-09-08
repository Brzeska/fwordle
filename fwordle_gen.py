import math
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn.functional as F

model = torch.load('fwordle_net.pt')
W1 = model['W1']
b1 = model['b1']
W2 = model['W2']
b2 = model['b2']
C = model['C']

#print(C)

ctoi = {np.base_repr(i,3).zfill(5):i+1 for i in range(243)}
ctoi['.....']=0
itoc = {s:i for i,s in ctoi.items()}

block_size = 6
embedding_dimension = 10

context = [0]*block_size

while True:
    emb = C[torch.tensor(context)]
    h = (emb.view(block_size*embedding_dimension)@W1+b1).tanh()
    logits = h@W2 + b2
    counts = logits.exp()
    probs = counts/counts.sum()
    guess = int(torch.multinomial(probs, 1).data)
    print(itoc[guess])
    context = context[1:] + [guess]
    if guess == 0:
        break
    
    
