DEMO = False

data = open("input-demo.txt" if DEMO else "input.txt").readlines()
data = list(map(lambda x: x.strip(), data))

currentMax = 0
currentAccumulator = 0
for line in data:
    try:
        number = int(line)
        currentAccumulator += number
    except:
        currentMax = max(currentMax, currentAccumulator)
        currentAccumulator = 0

print(currentMax)
