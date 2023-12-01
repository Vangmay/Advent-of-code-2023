import re
def problem1(filePath):
    f = open(filePath, "r")
    acc = 0 
    for x in f: 
        line = x 
        # While loop to gather the first and last digit
        numbers = re.findall(r'\d', x)
        number = int(numbers[0] + numbers[-1])
        acc = acc + number
    print(acc)

def problem1_part2(filePath):
    f = open(filePath).read().strip()
    ans = 0
    for line in f.split('\n'):
        digits = [] 
        for i,c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            for d,val in enumerate(['one', 'two', 'three','four','five', 'six', 'seven', 'eight', 'nine']):
                if line[i:].startswith(val):
                    digits.append(str(d+1))
        score = int(digits[0] + digits[-1])
        ans += score
        print(ans)
problem1_part2("problem1\input.txt")

