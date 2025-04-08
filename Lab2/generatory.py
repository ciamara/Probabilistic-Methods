import numpy as np

# 2.2 --> Xn+1 = (a*Xn +c) mod M
# 2.3 --> Xn+1 = A*Xn mod M
# 2.6 --> bi = b(i-p) xor b(i-q)

def checkValidity(vec):

    counts = {
        '0-1K': 0,
        '1K+1-2K': 0,
        '2K+1-3K': 0,
        '3K+1-4K': 0,
        '4K+1-5K': 0,
        '5K+1-6K': 0,
        '6K+1-7K': 0,
        '7K+1-8K': 0,
        '8K+1-9K': 0,
        '9K+1-10K': 0
    }
    
    # Check each number in the vector
    for num in vec:
        if 0 <= num <= 10000000:
            counts['0-1K'] += 1
        elif 10000001 <= num <= 20000000:
            counts['1K+1-2K'] += 1
        elif 20000001 <= num <= 30000000:
            counts['2K+1-3K'] += 1
        elif 30000001 <= num <= 40000000:
            counts['3K+1-4K'] += 1
        elif 40000001 <= num <= 50000000:
            counts['4K+1-5K'] += 1
        elif 50000001 <= num <= 60000000:
            counts['5K+1-6K'] += 1
        elif 60000001 <= num <= 70000000:
            counts['6K+1-7K'] += 1
        elif 70000001 <= num <= 80000000:
            counts['7K+1-8K'] += 1
        elif 80000001 <= num <= 90000000:
            counts['8K+1-9K'] += 1
        elif 90000001 <= num <= 100000000:
            counts['9K+1-10K'] += 1
    
    return counts


def shiftGen(n, p, q, b):

    results = b.copy()

    for i in range(n):
        bi = results[i - p] ^ results[i - q]
        results.append(bi)

    return results

def vectorGen(n, M):

    # seed X0
    X = np.array([1, 2, 3])
    
    # macierz wspolczynnikow
    A = np.array([
        [2, 3, 1],
        [1, 2, 4],
        [3, 0, 1]
    ])
    
    results = [X]

    for _ in range(n):
        X = A.dot(X) % M
        results.append(X.copy())


    return results


def linearGen(n, X0, a, c, M):


    ciag = []
    ciag.append(X0)

    for i in range(n):
        X0 = (a*X0 + c) % M
        ciag.append(X0)

    print(ciag)

    return ciag



def _main():

    n = 100000
    X0 = 15
    a = 69069
    c = 1
    M = 2147483648

    p = 7
    q = 3
    b = [1, 1, 0, 1, 1, 0, 1]

    # generator liniowy
    lin = linearGen(n, X0, a, c, M)
    print("Generator liniowy (pierwsze 10): ")
    print(lin[:10])
    print("Counted: ", checkValidity(lin))

    # generator wektorow
    vec = vectorGen(n, M)
    print("Generator wektorow (pierwsze 10): ")
    for i, v in enumerate(vec[:10]):
        print(f"X{i} =", v)

    sh = shiftGen(n, p, q, b)
    print("Generator po przesunieciu (pierwsze 20): ")
    print(sh[:20])


_main()