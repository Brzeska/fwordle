import time

with open('raw.txt', 'r') as f:
    lines = list(f.read().splitlines())#f.read() stores words.txt as a string, splitlines() converts that string into a list

t=int(time.time()/86400-7/24)-18797

l = len(lines)
if (l==6) and (lines[5]!='22222'):
    l = 'X'

out = f"Wordle {t:,} {l}/6*\n\n"

for i in lines:
    outStr = ''
    for j in i:
        if j == '0':
            outStr += '⬛'
        elif j == '1':
            outStr += '🟨'
        elif j == '2':
            outStr += '🟩'
    outStr += '\n'
    out += outStr

print(out)
