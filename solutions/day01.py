from collections import Counter

def solve_puzzles(data):
    left, right = zip(*data)
    total_distance = sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))
    right_count = Counter(right)
    similarity_score = sum(num * right_count[num] for num in left)

    return total_distance, similarity_score

with open('input/day01.txt', 'r') as file:
    data = [tuple(map(int, line.split())) for line in file]
print(solve_puzzles(data))
