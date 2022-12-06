DEMO = False

data = open("input-demo.txt" if DEMO else "input.txt").readlines()
data = list(map(lambda x: x.strip().split(","), data))
data = list(map(lambda x: [range(int(i.split("-")[0]),int(i.split("-")[1]) + 1) for i in x], data))

accumulator = 0

for pair in data:
    set0 = { i for i in pair[0] }
    set1 = { i for i in pair[1] }
    if len(set0.intersection(set1)) > 0:
        accumulator += 1

print(accumulator)

