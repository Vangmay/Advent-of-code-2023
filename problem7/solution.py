def score(hand):
    unique = list(set(hand))
    if len(unique) == 1:
        return 7 
        # Five of a kind 
    elif len(unique) == 2:
        if (hand.count(unique[0]) in [1,4]):
            return 6
            # Four of a kind 
        else:
            return 5
            # Full House 
    elif len(unique) == 3: 
        counts = map(hand.count, unique)
        if 3 in counts: 
            return 4 
            # Three of a kind 
        else: return 3
            # Two Pair
    elif len(unique) == 4: return 2 
    else: return 1
letter_map = {"T":"A", "J":".", "Q":"C", "K":"D", "A":"E"}
def strength(hand):
    return (score(hand), [letter_map.get(char, char) for char in hand])         

def solution1(file):
    data = open(file).read().split()
    inputs = []
    for i in range(0, len(data), 2):
        inputs.append([data[i],int(data[i+1])])
    inputs.sort(key = lambda play:strength(play[0]))
    sum = 0
    for idx, hand in enumerate(inputs, 1):
        sum += idx * hand[1]
    print("Solution 1: ", sum)  

def solution2(file):
    data = open(file).read().split()
    inputs = []
    for i in range(0, len(data), 2):
        inputs.append([data[i],int(data[i+1])])
    inputs.sort(key = lambda play:strength(play[0]))
    print([strength(play[0]) for play in inputs])
    sum = 0
    for idx, hand in enumerate(inputs, 1):
        sum += idx * hand[1]
    print("Solution 2: ", sum) 

solution1("problem7\input.txt")
# solution2("./short.txt")
