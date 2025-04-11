import numpy as np

# 2.2 --> Xn+1 = (a*Xn +c) mod M
# 2.3 --> Xn+1 = A*Xn mod M
# 2.6 --> bi = b(i-p) xor b(i-q)

def checkValidityLinear(vec, M):

    counts = {
        'I': 0,
        'II': 0,
        'III': 0,
        'IV': 0,
        'V': 0,
        'VI': 0,
        'VII': 0,
        'VIII': 0,
        'IX': 0,
        'X': 0
    }
    
    # Check each number in the vector
    for num in vec:
        if 0 <= num <= (M/10):
            counts['I'] += 1
        elif (M/10 +1) <= num <= (2*M/10):
            counts['II'] += 1
        elif (2*M/10) <= num <= (3*M/10):
            counts['III'] += 1
        elif (3*M/10) <= num <= (4*M/10):
            counts['IV'] += 1
        elif (4*M/10) <= num <= (5*M/10):
            counts['V'] += 1
        elif (5*M/10) <= num <= (6*M/10):
            counts['VI'] += 1
        elif (6*M/10) <= num <= (7*M/10):
            counts['VII'] += 1
        elif (7*M/10) <= num <= (8*M/10):
            counts['VIII'] += 1
        elif (8*M/10) <= num <= (9*M/10):
            counts['IX'] += 1
        elif (9*M/10) <= num <= M:
            counts['X'] += 1
    
    return counts

def checkValidityShift(vec, b):

    counts = {
        'I': 0,
        'II': 0,
        'III': 0,
        'IV': 0,
        'V': 0,
        'VI': 0,
        'VII': 0,
        'VIII': 0,
        'IX': 0,
        'X': 0
    }
    
    # Check each number in the vector
    for num in vec:
        if 0 <= num <= (2**len(b)/10):
            counts['I'] += 1
        elif (2**len(b)/10) <= num <= (2*2**len(b)/10):
            counts['II'] += 1
        elif (2*2**len(b)/10) <= num <= (3*2**len(b)/10):
            counts['III'] += 1
        elif (3*2**len(b)/10) <= num <= (4*2**len(b)/10):
            counts['IV'] += 1
        elif (4*2**len(b)/10) <= num <= (5*2**len(b)/10):
            counts['V'] += 1
        elif (5*2**len(b)/10) <= num <= (6*2**len(b)/10):
            counts['VI'] += 1
        elif (6*2**len(b)/10) <= num <= (7*2**len(b)/10):
            counts['VII'] += 1
        elif (7*2**len(b)/10) <= num <= (8*2**len(b)/10):
            counts['VIII'] += 1
        elif (8*2**len(b)/10) <= num <= (9*2**len(b)/10):
            counts['IX'] += 1
        elif (9*2**len(b)/10) <= num <= (2**len(b)):
            counts['X'] += 1   
    return counts


def shiftGen(n, p, q, b, length):

    bits = []
    previous = b.copy()

    for i in range(n * length):
        new_bit = previous[-p] ^ previous[-q]
        previous = previous[1:] + [new_bit]
        bits.append(new_bit)

    # bits to ints
    results = []
    for i in range(n):
        chunk = bits[i * length:(i + 1) * length]
        number = 0
        for bit in chunk:
            number = (number << 1) | bit
        results.append(number)

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
    #ciag.append(X0)

    for i in range(n):
        X0 = (a*X0 + c) % M
        ciag.append(X0)

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
    length = len(b)

    # generator liniowy
    lin = linearGen(n, X0, a, c, M)
    print("Generator liniowy: ")
    print(lin)
    print("Counted: ", checkValidityLinear(lin, M))

    # generator wektorow
    # vec = vectorGen(n, M)
    # print("Generator wektorow (pierwsze 10): ")
    # for i, v in enumerate(vec[:10]):
    #     print(f"X{i} =", v)

    sh = shiftGen(n, p, q, b, length)
    print("Generator po przesunieciu: ")
    print(sh)
    print("Counted: ", checkValidityShift(sh, b))


_main()