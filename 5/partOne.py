import re

DEMO = False

data = open("input-demo.txt" if DEMO else "input.txt").read()
data = data.split("\n\n")

stacks_number = data[0].split("\n")[-1]
stacks_number = len(re.findall("\d+", stacks_number))

lines = []
stacks = []

for i in range(0,stacks_number):
    line = data[0].split("\n")[i]
    line = re.sub("\s{1,2}", "-", line)
    line = re.sub("[\[\]]","",line)
    lines.append(line)

for i in range(0, stacks_number*2, 2):
    stack = []
    for line in lines:
        if match := re.search("[A-Z]", line[i]):
            stack.append(match.group())
    stacks.append(stack)

def make_move(instruction):
    move = int(re.search("(?<=move )\d+", instruction).group())
    _from = int(re.search("(?<=from )\d+", instruction).group()) - 1
    to = int(re.search("(?<=to )\d+", instruction).group()) - 1
    for i in range(0, move):
        block = stacks[_from].pop(0)
        stacks[to].insert(0, block)

for instruction in data[1].split("\n"):
    make_move(instruction)

print("".join([stack[0] for stack in stacks]))
