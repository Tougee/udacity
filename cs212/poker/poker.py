import itertools

def poker(hands):
    return max(hands, key=hand_rank)

def hand_rank(hand):
    ranks = card_rank(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)

def card_rank(cards):
    ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def straight(ranks):
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
    colors = [c for r, c in hand]
    return len(set(colors)) == 1

def kind(n, ranks):
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

# def test():
#     "Test cases for functions in poker program."
#     sf = "6C 7C 8C 9C TC".split()
#     fk = "9D 9H 9S 9C 7D".split()
#     fh = "TD TC TH 7C 7D".split()
#     tp = "5S 5D 9H 9C 6S".split()
#     fkranks = card_rank(fk)
#     tpranks = card_rank(tp)
#     assert kind(4, fkranks) == 9
#     assert kind(3, fkranks) == None
#     assert kind(2, fkranks) == None
#     assert kind(1, fkranks) == 7
#     assert two_pair(fkranks) == None
#     assert two_pair(tpranks) == (9, 5)
#     assert straight([9, 8, 7, 6, 5]) == True
#     assert straight([9, 7, 7, 6, 5]) == False
#     assert flush(sf) == True
#     assert flush(fk) == False
#     assert card_rank(sf) == [10, 9, 8, 7, 6]
#     assert card_rank(fk) == [9, 9, 9, 9, 7]
#     assert card_rank(fh) == [10, 10, 10, 7, 7]
#     assert poker([sf, fk, fh]) == sf
#     assert poker([fk, fh]) == fk
#     assert poker([fh, fh]) == fh
#     assert poker([sf] + 99*[fh]) == sf
#     assert hand_rank(sf) == (8, 10)
#     assert hand_rank(fk) == (7, 9, 7)
#     assert hand_rank(fh) == (6, 10, 7)
#     return "test pass"

# print test()

def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand."
    return max(itertools.combinations(hand,5), key=hand_rank)

def test_best_hand():
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_hand passes'

print(test_best_hand())

allranks = '23456789TJQKA'
blackcards = [r+s for r in allranks for s in 'SC']
redcards = [r+s for r in allranks for s in 'DH']

def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."
    hands = set(best_hand(h) 
                for h in itertools.product(*map(replacement, hand)))
    return max(hands, key=hand_rank)
    
def replacement(card):
    if card == '?B': return blackcards
    elif card == '?R': return redcards
    else: return [card]

def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'

print(test_best_wild_hand())