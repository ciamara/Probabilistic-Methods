import random

def generate_x():

    num = random.random()

    # 1 -> 50%
    # 2 -> 20%
    # 3 -> 20%
    # 4 -> 10%
    if num < 0.5:
        return 1
    if num < 0.7:
        return 2
    if num < 0.9:
        return 3
    return 4

def generate_y(x):

    num = random.random()

    # x == 1 -> 20% (1), 80% (4)
    # x == 2 -> 100% (1)
    # x == 3 -> 50% (2), 50% (4)
    # x == 4 -> 100% (3)
    if x == 1:
        if num < 0.2:
            return 1
        return 4
    if x == 2:
        return 1
    if x == 3:
        if num < 0.5:
            return 2
        return 4
    if x == 4:
        return 3

def create_random_vector():
    x = generate_x()
    y = generate_y(x)
    return x, y


results = [[0 for _ in range(5)] for _ in range(5)]

for _ in range(100000):
    x, y = create_random_vector()
    results[x][y] += 1


print("X/Y", end="\t")
for i in range(1, 5):
    print(i, end="\t")
print()
for i in range(1, 5):
    print(i, end="\t")
    for j in range(1, 5):
        print(results[i][j], end="\t")
    print()