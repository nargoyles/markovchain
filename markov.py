import random
import string
from collections import defaultdict
import os
import textwrap

possibilities = {}
seedlist = []
good = defaultdict(list)
better = defaultdict(list)
best = defaultdict(list)

def readintxt (text):
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
        good[words[word]].append(words[word+1])
        better[words[word], words[word+1]].append(words[word+2])
        best[words[word], words[word+1], words[word+2]].append(words[word+3])
        if "." in words[word] or "!" in words[word] or "?" in words[word]:
            seedlist.append([words[word+1], words[word+2], words[word+3]])

def newtext (good, better, best, readability, sentances):
    seed = random.randint(0, len(seedlist))
    if readability == 1:
        w1 = seedlist[seed][0]
        new_text = []
        sentance_counter = 0
        while sentance_counter<sentances:
            new_text.append(w1)
            if "." in w1 or "!" in w1 or "?" in w1:
                sentance_counter+=1
            w2 = w1
            w1 = random.choice(good[(w2)])
        os.system('cls' if os.name == 'nt' else 'clear')
        markovchain = ' '.join(new_text)
        print textwrap.fill(markovchain, 75)
    elif readability == 2:
        w1, w2 = seedlist[seed][0], seedlist[seed][1]
        new_text = []
        sentance_counter = 0
        while sentance_counter<sentances:
            new_text.append(w1)
            if "." in w1 or "!" in w1 or "?" in w1:
                sentance_counter+=1
            w3 = w1
            w1 = w2
            w2 = random.choice(better[(w3, w2)])
        os.system('cls' if os.name == 'nt' else 'clear')
        markovchain = ' '.join(new_text)
        print textwrap.fill(markovchain, 75)
    elif readability == 3:
        w1, w2, w3 = seedlist[seed][0], seedlist[seed][1], seedlist[seed][2]
        new_text = []
        sentance_counter = 0
        while sentance_counter<sentances:
            new_text.append(w1)
            if "." in w1 or "!" in w1 or "?" in w1:
                sentance_counter+=1
            w4 = w1
            w1 = w2
            w2 = w3
            w3 = random.choice(best[(w4, w1, w2)])
        os.system('cls' if os.name == 'nt' else 'clear')
        markovchain = ' '.join(new_text)
        print textwrap.fill(markovchain, 75)


os.system('cls' if os.name == 'nt' else 'clear')
text = input("Choose what text to use.\n1: My 2015 Nanowrimo novel, 'Yes, There Might be Some Hurting'\n2: Lyrics from songs I've written\n")
words = readintxt(text)
states(words)
os.system('cls' if os.name == 'nt' else 'clear')
readability = input("Choose the level of readability.\n1: Gibberish\n2: Less gibberishy\n3: Close to the real deal \n")
os.system('cls' if os.name == 'nt' else 'clear')
sentances = input("How many sentances?\n")
newtext(good, better, best, readability, sentances)
