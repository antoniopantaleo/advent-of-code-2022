DEMO = False

data = open("input-demo.txt" if DEMO else "input.txt").readlines()
data = list(map(lambda x: [x.strip()[:len(x) // 2], x.strip()[len(x) // 2:]], data))

# Pytohn 3.9+
mapping = { letter:(value+1) for (value, letter) in enumerate([chr(i) for i in range(97,123)]) } | { letter:(value+27) for (value, letter) in enumerate([chr(i) for i in range(65,91)]) }

accumulator = 0

for compartments in data:
    set0 = { item for item in compartments[0] }
    set1 = { item for item in compartments[1] }
    target = set0.intersection(set1).pop()
    accumulator += mapping[target]

print(accumulator)

