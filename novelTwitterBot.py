import random
from collections import defaultdict

seedlist = []
better = defaultdict(list)

def readintxt ():
    text = random.choice([1,2])
    if text == 1:
        novel = open("novel.txt", "r", 1)
    elif text == 2:
        novel = open("Lyrics.txt", "r", 1)
    novel.seek(0)
    words = novel.read()
    words = words.split()
    return words

def states (words):
    total = len(words) - 3
    for word in range(total):
        better[words[word], words[word+1]].append(words[word+2])
        if "." in words[word] or "!" in words[word] or "?" in words[word]:
            seedlist.append([words[word+1], words[word+2], words[word+3]])

def newtext (better):
    seed = random.randint(0, len(seedlist))
    w1, w2 = seedlist[seed][0], seedlist[seed][1]
    new_text = []
    while sum([len(i) for i in new_text]) + len(w1) + len(new_text)<140:
        new_text.append(w1)
        w3 = w1
        w1 = w2
        w2 = random.choice(better[(w3, w2)])
    print ' '.join(new_text)

words = readintxt()
states(words)
newtext(better)
