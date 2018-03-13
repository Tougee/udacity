import random
from poker import *
from poker_pro import *

def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]

hands = deal(2)
print(hands)
print(poker(hands))
print(poker_pro(hands))

hands = deal(2, 7)
print(hands)

