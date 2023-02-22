
def main():
    with open("poker.txt") as f:
        content = f.readlines()
    content = [x[:-1] for x in content]
    content = [x.split(' ') for x in content]
    hands = [(x[:5],x[5:]) for x in content]

    numofwins = 0
    for i in hands:
        if winner(i) == 1:
            numofwins = numofwins + 1
    print(numofwins)
    return

def winner(hands):
    print("winner.hands = {}".format(hands))
    p1 = besthand(hands[0])
    p2 = besthand(hands[1])

    if p1 == p2:
        if p1 == 1:
            return bestPair(hands)
        else:
            return highestCard(hands)
    elif p1 > p2:
        return 1
    elif p1 < p2:
        return 2

def highestCard(hands):
    print("highestCard.hands = {}".format(hands))
    h1 = hands[0]
    h2 = hands[1]
    print("highestCard.h1 = {}".format(h1))
    print("highestCard.h2 = {}".format(h2))
    h1 = [x[0] for x in h1]
    h2 = [x[0] for x in h2]
    print("highestCard.h1 = {}".format(h1))
    print("highestCard.h2 = {}".format(h2))
    check = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    p1max = 0
    for a in h1:
        if check.index(a) > p1max:
            p1max = check.index(a)
    p2max = 0
    for b in h2:
        if check.index(b) > p2max:
            p2max = check.index(b)
    if p1max > p2max:
        return 1
    return 2
    
def bestPair(hands):
    hands = [x[0] for x in hands]
    h1 = sorted(hands[:5])
    h2 = sorted(hands[5:])
    for i in range(len(h1)-1):
        if h1[i]==h1[i+1]:
            print(h1[i])
            break
    for j in range(len(h2)-1):
        if h2[j]==h2[j+1]:
            print(h2[j])
            break
    check = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    for a in range(len(check)):
        if h1[i]==check[a]:
            break
    for b in range(len(check)):
        if h2[j]==check[b]:
            break
    if a > b:
        return 1
    return 2

def besthand(hand):
    print("besthand.hand = {}".format(hand))
    straight = hasStraight(hand)
    flush = hasFlush(hand)
    royal = isRoyal(hand)
    fourofakind = hasFourOfAKind(hand)
    threeofakind = hasThreeOfAKind(hand)
    twopair = hasTwoPair(hand)
    pair = hasPair(hand)
    if straight and flush and royal:
        return 9
    elif straight and flush:
        return 8
    elif fourofakind:
        return 7
    elif threeofakind and pair:
        return 6
    elif flush:
        return 5
    elif straight:
        return 4
    elif threeofakind:
        return 3
    elif twopair:
        return 2
    elif pair:
        return 1
    else:
        return 0

def isRoyal(hand):
    x = {y[0] for y in hand}
    check = [{'A','K','Q','J','T'}]
    if x in check:
        return True
    return False
    
    
def hasPair(hand):
    x = [y[0] for y in hand]
    x.sort()
    if x[:2]==[x[0] for i in range(2)] or x[1:3]==[x[1] for i in range(2)] or x[2:4]==[x[2] for i in range(2)] and x[3:]==[x[3] for i in range(2)]:
        return True
    return False

def hasTwoPair(hand):
    x = [y[0] for y in hand]
    x.sort()
    tmp = []
    for i in range(len(x)-1):
        if x[i:i+2]==[x[i],x[i]]:
            tmp.append(x[i])
            tmp.append(x[i+1])
    if len(tmp)==4:
        return True
    return False

def hasThreeOfAKind(hand):
    x = [y[0] for y in hand]
    x.sort()
    if x[:3]==[x[0] for i in range(3)] or x[1:4]==[x[1] for i in range(3)] or x[2:]==[x[2] for i in range(3)]:
        return True
    return False

def hasFourOfAKind(hand):
    x = [y[0] for y in hand]
    x.sort()
    if x[:4]==[x[0] for i in range(4)] or x[1:]==[x[1] for i in range(4)]:
        return True
    return False
    
def hasStraight(hand):
    x = {y[0] for y in hand}
    check = [{'3', '2', '5', '4', '6'}, {'3', '5', '4', '7', '6'}, {'8', '5', '4', '7', '6'}, {'9', '8', '5', '7', '6'}, {'9', '8', 'T', '7', '6'}, {'9', '8', 'J', 'T', '7'}, {'9', '8', 'J', 'Q', 'T'}, {'Q', '9', 'K', 'J', 'T'}, {'Q', 'A', 'K', 'J', 'T'}]
    if x in check:
        return True
    return False

def hasFlush(hand):
    x = [y[1] for y in hand]
    check = [x[0] for i in range(5)]
    if x == check:
        return True
    return False
    
if __name__ == "__main__":
    main()
