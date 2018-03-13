def poker_pro(hands):
    return max(hands, key=hand_rank)

def hand_rank(hand):
    # counts is the count of each rank; ranks list correspoding ranks
    # E.g. '7 T 7 9 7' => counts = (3, 1, 1); ranks = (7, 10, 9)
    groups = group(['--23456789TJQKA'.index(r) for r,s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks) - min(ranks) == 4
    flush = len(set([s for r,s in hand])) == 1
    #return (9 if (5,) == counts else 
    #        8 if straight and flush else 
    #        7 if (4, 1) == counts else 
    #        6 if (3, 2) == counts else 
    #        5 if flush else 
    #        4 if straight else 
    #        3 if (3, 1, 1) else 
    #        2 if (2, 2, 1) else 
    #        1 if (2, 1, 1, 1) else 
    #        0), ranks
    return max(count_rankings[counts], 4*straight + 5*flush), ranks

count_rankings = {(5,):10, (4, 1):7, (3, 2):6, (3, 1, 1):3, (2, 2, 1):2, (2, 1, 1, 1):1, (1, 1, 1, 1, 1):0}

def group(items):
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)

def unzip(pairs): return zip(*pairs)