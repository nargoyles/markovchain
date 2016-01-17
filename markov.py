import random
import string
from IPython import embed
from collections import defaultdict

possibilities = {}
seedlist = []
dup_dict = defaultdict(list)

def readintxt ():
    novel = open("novel.txt", "r", 1)
    novel.seek(0)
    words = novel.read()
    words = words.split()
    return words

def states (words):
    total = len(words) - 3
    for word in range(total):
        dup_dict[words[word], words[word+1]].append(words[word+2])
        if "." in words[word] or "!" in words[word] or "?" in words[word]:
            seedlist.append([words[word+1], words[word+2]])

def newtext (dup_dict, sentances):
    seed = random.randint(0, len(seedlist))
    #print seed
    seed_word, next_word = seedlist[seed][0], seedlist[seed][1]
    w1, w2 = seed_word, next_word
    new_text = []
    sentance_counter = 0
    while sentance_counter<sentances:
        new_text.append(w1)
        w3 = w1
        w1 = w2
        #embed()
        w2 = random.choice(dup_dict[(w3, w2)])
        if "." in w2 or "!" in w2 or "?" in w2:
            sentance_counter+=1
    new_text.append(w2)
    #print possibilities
    print ' '.join(new_text)

words = readintxt()
states(words)
sentances = input("How many words to sentances?")
newtext(dup_dict,sentances)
