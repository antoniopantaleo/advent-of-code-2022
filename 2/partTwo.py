DEMO = False

data = open("input-demo.txt" if DEMO else "input.txt").readlines()
data = list(map(lambda x: x.strip().split(" "), data))

moves = ["A", "B", "C"]
end_results = ["X", "Y", "Z"]

score_matrix = [
    [3, 6, 0],
    [0, 3, 6],
    [6, 0, 3]
]

accumulator = 0

def point_for_round(round):
    opponent_move = round[0]
    my_result = end_results.index(round[1]) * 3
    return my_result + score_matrix[moves.index(opponent_move)].index(my_result) + 1

for round in data:
    accumulator += point_for_round(round)

print(accumulator)

