import random

# karten: zweistellige tuples (farbe, rang)
# im nachhinein besser: Karten klasse implementieren mit farbe, rang __str__ methode, konstruktoren für bestimmte/zufällige karte
ranks = {0:"2",
         1:"3",
         2:"4",
         3:"5",
         4:"6",
         5:"7",
         6:"8",
         7:"9",
         8:"10",
         9:"Bube",
         10:"Dame",
         11:"König",
         12:"Ass"
         }

 
cards = []
for r in range(0,13):
    for c in range(0,4):
        cards.append((c,r))

def printCard(c):
   print(["Karo", "Herz", "Pik", "Kreuz"][c[0]] + " " + ranks[c[1]])

def printHand(h):
    for c in h:
        printCard(c)

def getCard():
    return cards[random.randint(0,len(cards)-1)]

def drawHand(hand):
    for i in range(len(hand),5):
        r = getCard()
        while r in hand:
            r = getCard()
        hand.append(r)
    return hand

## SHOW ME YOUR HAAAANDSS ##
def isFlush(hand):
    color = hand[0][0]
    for c in hand:
        if color != c[0]:
            return False
    return True

def isStraight(hand):
    rs = []
    for c in hand:
        rs.append(c[1])
    for i in range(min(rs), min(rs)+5):
        if not i in rs:
            return False
    return True

def nOfAKind(hand):
    rs = []
    for i in range(0,13):
        rs.append(0)
    for c in hand:
        rs[c[1]]+=1
    return rs

rankings = {
    0:"Royal Flush",
    1:"Straight Flush",
    2:"Four Of A Kind",
    3:"Full House",
    4:"Flush",
    5:"Straight",
    6:"Three Of A Kind",
    7:"Two Pair",
    8:"Pair",
    9:"High Card"
}

def getRanking(hand):
    multiples = nOfAKind(hand)

    if max(hand) == 12 and isFlush(hand):
        return 0

    if isStraight(hand) and isFlush(hand):
       return 1

    if 4 in multiples:
        return 2

    if 3 in multiples and 2 in multiples:
        return 3

    if isFlush(hand):
        return 4

    if isStraight(hand):
        return 5

    if 3 in multiples:
        return 6
    
    if 2 in multiples:
        multiples.remove(2)
        if 2 in multiples:
            return 7
        return 8

    return 9

if __name__ == "__main__":
    statistics = []
    for i in range(0,10):
        statistics.append(0)

    for i in range(0, 100000):
        test = drawHand([])
        print(test)
        print(rankings[getRanking(test)])
        statistics[getRanking(test)]+=1
        print()

    for i in range(0,10):
        print(rankings[i] + ": " + str(statistics[i]/1000) + "%")
