def solution1(file):
    data = open(file).read().split()
    data.remove("Time:")
    data.remove("Distance:")
    mid = int(len(data) / 2)
    time = data[:mid]
    distance = data[mid:]
    inputs = []
    for i in range(0, len(time)):
        inputs.append((time[i], distance[i])) 
    
    # Now inputs are (time, distance) tuples
    solutions = []
    for pair in inputs:
        time = int(pair[0])
        distance = int(pair[1])

        # I want ButtonPressed and Time - ButtonPressed 
        # combinations 
        # Such that ButtonPressed * Time - ButtonPressed is greater than 9 
        Bp = []
        for i in range(0, time):
            ButtonPressed = i 
            TimeMoved = time - ButtonPressed
            distanceMoved = ButtonPressed * TimeMoved 
            if distanceMoved > distance:
                Bp.append(ButtonPressed)
        solutions.append(len(Bp))
    ans = 1 
    for item in solutions:
        ans = ans*item 
    print("Solution 1: ", ans )
            
def solution2(file):
        data = open(file).read().split()
        data.remove("Time:")
        data.remove("Distance:")
        mid = int(len(data) / 2)
        time = data[:mid]
        distance = data[mid:]

        totalTime = ""
        totalDistance = ""
        for i in range(0, len(time)):
             totalTime = totalTime + time[i]
             totalDistance =  totalDistance + distance[i]
        
        inputs = [(int(totalTime), int(totalDistance))]
        # Now inputs are (time, distance) tuples
        solutions = []
        for pair in inputs:
            time = int(pair[0])
            distance = int(pair[1])

            # I want ButtonPressed and Time - ButtonPressed 
            # combinations 
            # Such that ButtonPressed * Time - ButtonPressed is greater than 9 
            Bp = []
            for i in range(0, time):
                ButtonPressed = i 
                TimeMoved = time - ButtonPressed
                distanceMoved = ButtonPressed * TimeMoved 
                if distanceMoved > distance:
                    Bp.append(ButtonPressed)
            solutions.append(len(Bp))
        ans = 1 
        for item in solutions:
            ans = ans*item 
        print("Solution 2: ", ans )

solution1("problem6\input.txt")
solution2("problem6\input.txt")