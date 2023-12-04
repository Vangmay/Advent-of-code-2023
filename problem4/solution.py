
import re 

shortFile = "problem4\short.txt"
longFile = "problem4\input.txt"

def solution1(file):
    text = open(file).read().splitlines()
    matchList = []
    for line in text:
        numMatch = 0 
        splitted = line.split(":")[1].split("|")
        WinningDigits = list(map(int,re.findall(r'\d+', splitted[0])))
        digits = list(map(int, re.findall(r'\d+', splitted[1])))
        
        for digit in digits:
            if digit in WinningDigits:
                numMatch += 1
        matchList.append(int(pow(2, numMatch - 1)))
    print("Solution 1: ",  sum(matchList))

def solution2(file):
    text = open(file).read().splitlines(); 
    fileDict = {}
    for idx, cardLine in enumerate(text):
        splitted = cardLine.split(":")[1].split("|")
        WinningDigits = list(map(int,re.findall(r'\d+', splitted[0])))
        digits = list(map(int, re.findall(r'\d+', splitted[1])))
        fileDict[idx] = [WinningDigits, digits]

    def processCard(idx):
        '''
        Processes the card number _idx_ in fileDict
        '''
        WinningDigits = fileDict[idx][0]
        digits = fileDict[idx][1]
        numMatch = 0 
        if  (idx == len(fileDict)):
            return 0
        else:
            for digit in digits:
                if digit in WinningDigits:
                    numMatch += 1
            # print(idx, numMatch)
        for i in range(idx+1, idx + numMatch + 1):
            # print("I was at ", idx, "Now calling ", i)
            numMatch = numMatch + processCard(i)
        # print(numMatch)
        return numMatch
    cards = len(fileDict)
    for i in range(0, len(fileDict)):
        cards = cards + processCard(i)
    print(cards)
    
solution1(longFile)

solution2(longFile)