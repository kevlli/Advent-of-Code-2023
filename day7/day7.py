def getType(string):
    thisdict = {}
    for s in string:
        if s in thisdict:
            thisdict[s] += 1
        else:
            thisdict[s] = 1
    thisdict = sorted(thisdict.items(), key=lambda x: - x[1])
    typeHand = thisdict[0][1]
    if typeHand == 5:
        return 0
    elif typeHand == 4:
        return 1
    elif typeHand == 3:
        if thisdict[1][1] == 2:
            return 2
        return 3
    elif typeHand == 2:
        if thisdict[1][1] == 2:
            return 4
        return 5
    elif typeHand == 1:
        return 6

def compareHands(h1, h2):
    order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    for i in range(len(h1)):
        index1 = order.index(h1[i])
        index2 = order.index(h2[i])
        if (index1 == index2):
            continue
        if (index1 < index2):
            return 1
        if (index1 > index2):
            return 0
        
def insertList(list, tup):

    cards = tup[0]
    if not list:
        list.insert(0, tup)
        return list
    for i, hands in enumerate(list):
        if compareHands(cards, hands[0]):
            list.insert(i, tup)
            return list
    list.insert(len(list), tup)
    return list

def part1():
    file = open("input.txt", "r")

    hands = []
    line = file.readline()
    while line:
        line = line.split(" ")
        hands.append((line[0], int(line[1])))
        line = file.readline()
    #print(hands)

    fiveofakind = []
    fourofakind = []
    fullhouse = []
    threeofakind = []
    twopair = []
    onepair = []
    highcard = []

    allTypes = [fiveofakind, fourofakind, fullhouse, threeofakind, twopair, onepair, highcard]

    #print(hands)
    for hand in hands:
        cards = hand[0]
        thisType = getType(cards)
        insertList(allTypes[thisType], hand)
    
    sum = 0
    rank = len(hands)
    for types in allTypes:
        for tup in types:
            sum += tup[1] * rank
            #print(rank)
            rank -= 1
    print(sum)

def getType2(string):
    thisdict = {}
    numJ = 0
    for s in string:
        if s == 'J':
            numJ += 1
            continue
        if s in thisdict:
            thisdict[s] += 1
        else:
            thisdict[s] = 1
    if numJ == 5:
        return 0
    thisdict = sorted(thisdict.items(), key=lambda x: - x[1])

    typeHand = thisdict[0][1] + numJ
    if typeHand == 5:
        return 0
    elif typeHand == 4:
        return 1
    elif typeHand == 3:
        if thisdict[1][1] == 2:
            return 2
        return 3
    elif typeHand == 2:
        if thisdict[1][1] == 2:
            return 4
        return 5
    elif typeHand == 1:
        return 6

def compareHands2(h1, h2):
    order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    for i in range(len(h1)):
        index1 = order.index(h1[i])
        index2 = order.index(h2[i])
        if (index1 == index2):
            continue
        if (index1 < index2):
            return 1
        if (index1 > index2):
            return 0
        
def insertList2(list, tup):
    cards = tup[0]
    if not list:
        list.insert(0, tup)
        return list
    for i, hands in enumerate(list):
        if compareHands2(cards, hands[0]):
            list.insert(i, tup)
            return list
    list.insert(len(list), tup)
    return list

def part2():
    file = open("input.txt", "r")

    hands = []
    line = file.readline()
    while line:
        line = line.split(" ")
        hands.append((line[0], int(line[1])))
        line = file.readline()
    #print(hands)

    fiveofakind = []
    fourofakind = []
    fullhouse = []
    threeofakind = []
    twopair = []
    onepair = []
    highcard = []

    allTypes = [fiveofakind, fourofakind, fullhouse, threeofakind, twopair, onepair, highcard]

    #print(hands)
    for hand in hands:
        cards = hand[0]
        thisType = getType2(cards)
        insertList2(allTypes[thisType], hand)
    
    sum = 0
    rank = len(hands)
    for types in allTypes:
        for tup in types:
            sum += tup[1] * rank
            #print(rank)
            rank -= 1
    print(sum)

part2()
