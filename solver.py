import random

with open('words.txt', 'r') as f:
    wordSet = set(f.read().splitlines())#f.read() stores words.txt as a string, splitlines() converts that string into a list

def giveFeedback(guess,answer):
    '''
    guess and answer are both 5 character strings
    giveFeedback returns a five character string of x's y's and g's
    g: this position in guess is correct
    y: this position in guess is incorrect, but the character does appear in the answer
    x: this character does not appear in the answer
    '''
    #convert answer into dictionary:
    answer_list = list(answer)
    guess_list = list(guess)
    answer_dict = {}
    for i in answer_list:
        answer_dict[i] = answer_dict.get(i,0) + 1
    
    returnValue = ''
    
    for i in range(len(guess)): #first pass: assign hits (g) and misses (x, some will get updated to y in second pass)
        if guess_list[i] == answer_list[i]:
            returnValue += 'g'
            answer_dict[guess[i]] = answer_dict.get(guess[i],0) - 1
        else:
            returnValue += 'x'
    
    return_list = list(returnValue)

    for i in range(len(guess)):#second pass: assign y's
        if returnValue[i] == 'x':
            if answer_dict.get(guess_list[i],0):
                return_list[i] = 'y'
                answer_dict[guess[i]] = answer_dict.get(guess[i],0) - 1

    returnValue = "".join(return_list)
    return returnValue

'''
answer = random.choice(list(wordSet))


while True:
    guess = input("enter guess: ")
    print(giveFeedback(guess,answer))
'''

def isConsistent(guess, feedback, new_guess):
    '''
    Boolean function. Takes a word-feedback pair and determines if newGuess is consistent with the feedback given.
    '''

    new_guess_set = set(list(new_guess))
    for i in range(len(guess)):
        if feedback[i] == 'g': #meaning guess and newGuess should match here
            if guess[i] != new_guess[i]:
                return False
        elif feedback[i] == 'x':
            if guess[i] == new_guess[i]:
                return False
        if feedback[i] == 'y':
            if new_guess_set.isdisjoint({guess[i]}):
                return False
            if guess[i] == new_guess[i]:
                return False

    return True

def narrowSet(wordSet, guess, feedback):
    '''
    this looks at most recent guess and feedback, and throws out all words not consistent with the feedback
    '''
    new_set = set()
    for i in wordSet:
        if isConsistent(guess, feedback, i):
            new_set.add(i)

    return new_set


#print(narrowSet(wordSet,'hello','ggggx'))


answer = random.choice(list(wordSet))
guess = random.choice(list(wordSet))
#print(f"answer: {answer}")
#print(f"guess: {guess}")
info = 'zzzzz' #placeholder, z means nothing

for i in range(6):
    info = giveFeedback(guess,answer)
    wordSet = narrowSet(wordSet, guess, info)
    guess = random.choice(list(wordSet))
    #print(f"guess: {guess} info: {giveFeedback(guess,answer)}")
    print(giveFeedback(guess,answer))
    if giveFeedback(guess,answer) == 'ggggg':
        break
    
