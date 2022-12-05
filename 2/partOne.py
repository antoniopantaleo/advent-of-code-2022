DEMO = False

data = open("input-demo.txt" if DEMO else "input.txt").readlines()
data = list(map(lambda x: x.strip().split(" "), data))

opponent_moves = ["A", "B", "C"]
my_moves = ["X", "Y", "Z"]

score_matrix = [
    [3, 6, 0],
    [0, 3, 6],
    [6, 0, 3]
]

accumulator = 0

def point_for_round(round):
    opponent_move = opponent_moves.index(round[0])
    my_move = my_moves.index(round[1])
    return (my_move + 1) + score_matrix[opponent_move][my_move]

for round in data:
    accumulator += point_for_round(round)

print(accumulator)

