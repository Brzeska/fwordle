import time
tinit = time.time()
import math
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn.functional as F

def showtime():
    '''
    Call this at any point to print time since program started running.
    '''
    print(f'{time.time() - tinit:.4f}')

#read in data
data = open('data.txt').read().split('\n.....\n')

#create line to int mapping
ctoi = {np.base_repr(i,3).zfill(5):i+1 for i in range(243)}
ctoi['.....']=0
itoc = {s:i for i,s in ctoi.items()}

#hyperparameter definitions
block_size = 6
embedding_dimension = 10
hidden_neurons = 120
batch_size = 35

#generate unlabeled instances and labels
X,Y = [],[]
for i in data:
    context = [0]*block_size
    instance = i.splitlines() + ['.....']
    for line in instance:
        X.append(context)
        Y.append(ctoi[line])
        context = context[1:] + [ctoi[line]]

X = torch.tensor(X)
Y = torch.tensor(Y)

g = torch.Generator().manual_seed(42)

#print(minibatch)
#note: Y[ix] is associated labels

#Embedding layer: each line gets embedded into a space with dimension embedding_dimension
C = torch.randn(244,embedding_dimension,requires_grad=True)
W1 = torch.randn((block_size*embedding_dimension,hidden_neurons),requires_grad=True)
b1 = torch.randn(hidden_neurons,requires_grad=True)
W2 = torch.randn(hidden_neurons,244, requires_grad=True)
b2 = torch.randn(244, requires_grad=True)
parameters = [C,W1,b1,W2,b2]


for i in range(30000):
    lr = .1 if i < 15000 else .01
    ix = torch.randint(0,len(X),(batch_size,))
    minibatch = X[ix]
    emb = C[minibatch]
    h = (emb.view(batch_size,block_size*embedding_dimension) @ W1 + b1).tanh()
    
    #softmax
    
    logits = h@W2 + b2
    
    loss = F.cross_entropy(logits, Y[ix])
    
    #backward pass
    for p in parameters:
        p.grad = None
    loss.backward()
    
    #update
    for p in parameters:
        p.data += -lr*p.grad
    
    print(loss.data)


batch_size = len(X)
ix = torch.randint(0,len(X),(batch_size,))
batch = X
emb = C[X]
h = (emb.view(batch_size,block_size*embedding_dimension) @ W1 + b1).tanh()

#softmax
    
logits = h@W2 + b2
    
loss = F.cross_entropy(logits, Y)

print(loss)

torch.save({
    'C': C,
    'W1': W1, 'b1': b1,
    'W2': W2, 'b2': b2,
    # etc.
}, 'fwordle_net.pt')
