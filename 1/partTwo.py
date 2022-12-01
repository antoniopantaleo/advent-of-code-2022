DEMO = False

data = open("input-demo.txt" if DEMO else "input.txt").readlines()
data = list(map(lambda x: x.strip(), data))
data.append("")

bag = []
currentAccumulator = 0

for line in data:
    try:
        number = int(line)
        currentAccumulator += number
    except:
        bag.append(currentAccumulator)
        if len(bag) > 3:
            bag.remove(min(bag))
        currentAccumulator = 0

print(sum(bag))
