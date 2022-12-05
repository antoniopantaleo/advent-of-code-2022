DEMO = False

def divide_array(arr, intoGroups):
    for i in range(0, len(arr), intoGroups):
        yield arr[i: i+intoGroups]

data = open("input-demo.txt" if DEMO else "input.txt").readlines()
data = list(divide_array(list(map(lambda x: x.strip(), data)), 3))

# Pytohn 3.9+
mapping = { letter:(value+1) for (value, letter) in enumerate([chr(i) for i in range(97,123)]) } | { letter:(value+27) for (value, letter) in enumerate([chr(i) for i in range(65,91)]) }

accumulator = 0

for groups in data:
    _set = set()
    for racksack in groups:
        items = {item for item in racksack}
        if len(_set) == 0:
            _set = items
        else:
            _set = _set.intersection(items)
    target = _set.pop()
    accumulator += mapping[target]

print(accumulator)
