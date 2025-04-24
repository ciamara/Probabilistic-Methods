import numpy as np
import math
import random

# ZLICZANIE PRZEDZIALOW DLA GENEROWANYCH LICZB
def count_interval(generated, M=150, m=50, buckets=10):
    
    counts = [0] * buckets
    div = (M - m) / buckets

    for num in generated:
        index = int((num - m) / div)
        if index >= buckets:
            index = buckets - 1
        counts[index] += 1

    print("Buckets:")
    for i, count in enumerate(counts):
        bucket_start = m + i * div
        bucket_end = bucket_start + div
        print(f"Bucket {i+1} ({bucket_start:.1f} – {bucket_end:.1f}): {count}")


def count_simple(generated):
    
    counts = {1: 0, 2: 0, 3: 0, 4: 0}

    for num in generated:
        if num in counts:
            counts[num] += 1
        else:
            print(f"error: {num}")

    print("Buckets:")
    for value in sorted(counts):
        print(f"Value {value}: {counts[value]}")


# U(0,1) odwracanie dystrybuanty
def generator_50_150(n):

    results = []

    for _ in range(n):
        liczba = random.random()
        results.append(100*liczba + 50)

    return results


def generator_rozklad_dyskretny(n):

    results = []

    compartments = [
        (1, 0.2),
        (2, 0.5),
        (3, 0.9),
        (4, 1.0)
    ]

    for _ in range(n):

        u = random.random()  # losowa liczba z przedziału [0, 1)
        for num, treshold in compartments:
            if u < treshold:
                results.append(num)
                break

    return results


def _main():

    # liczba probek
    n = 100000

    dystrybuanta = generator_50_150(n)
    print("Generator (metoda odwracania dystrybuanty) 50-150: ")
    count_interval(dystrybuanta, 150, 50, 10)

    dyskretny = generator_rozklad_dyskretny(n)
    print("Generator (metoda rozklad dyskretny) 1-4: ")
    print("1 -> 0.2")
    print("2 -> 0.3")
    print("3 -> 0.4")
    print("4 -> 0.1")
    count_simple(dyskretny)

















_main()


