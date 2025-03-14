import math

def generate_variations(data: list, k: int, current: list = None, n: int = 0, results: list = None):
    # variations of length k

    if current is None:
        current = []
    if results is None:
        results = []

    #the variation is complete
    if len(current) == k:
        print(n+1, [x.id for x in current])
        results.append(current)
        return (n+1, results)
    
    for elem in data:
        
        # copy of current & data, current -> element, element is taken from data
        new_current = current.copy()
        new_data = data.copy()

        new_current.append(elem)
        new_data.remove(elem)   #so it isnt used again

        # recursive call
        n, results = generate_variations(new_data, k, new_current, n, results)

    # permutations(orders)
    return (n, results)

def generate_subsets(data: list, m: int, current: list = None, n: int = 0, results: list = None):

    if current is None:
        current = []
    if results is None:
        results = []

    # finished subset
    if len(current) == m:
        print(n+1, [x.id for x in current])
        results.append(current)
        return (n+1, results)

    #copy so that the original data isnt changed
    data_copy = data.copy()
    for elem in data:

        new_current = current.copy()

        new_current.append(elem)
        n, results = generate_subsets(data_copy, m, new_current, n, results)

        data_copy.remove(elem)
    return (n, results)

class City:
    def __init__(self, id: int, name: str, population: int, lat: float, lon: float):
        self.id = id
        self.name = name
        self.population = population
        self.lat = lat #latitude
        self.lon = lon #longitude

    def __str__(self):
        return self.name

    def distance(self, other):
        return ((self.lat - other.lat)**2 + (self.lon - other.lon)**2)**0.5

n = 5 # how many cities -> n first from data
k = 3 # length of variations
m = 3 # size of subsets
variations_formula = (math.factorial(n)/math.factorial(n-k))
subsets_formula = (math.factorial(k+n-1)/(math.factorial(k)*(math.factorial(n-1))))

#input and format data
with open("france.txt", "r") as file:
    data: list[City] = []
    for line in file.readlines()[1:n+1]:
        line_data = line.strip().replace('\n', '').split(' ')
        data.append(City(int(line_data[0]), line_data[1], int(line_data[2]), float(line_data[3]), float(line_data[4])))

#create variations (porzadki odwiedzin M z N)
print("Variations(without repeats)")
variations_count, variations = generate_variations(data, k)
print(f"n = {n}, k = {k}, variations_count = {variations_count}\n")
print("Variations number from formula = ")
print(variations_formula)
print("\n\n")

#subsets(podzbiory z mozliwymi powtorzeniami)
print("Subsets: ")
subsets_count, subsets = generate_subsets(data, m)
print(f"n = {n}, m = {m}, subsets_count = {subsets_count}\n\n")
print("Subset number from formula = ")
print(subsets_formula)
print("\n\n")

#distances for all permutations(orders)
distances = []
for order in variations:
    result = 0
    current = order[0]
    for city in order[1:]:
        result += current.distance(city)
        current = city
        #print(result)
        #print("\n")
    result += current.distance(order[0])
    distances.append(result)
    #print(result)
    #print("\n")

# ascending sort so the first entry is the smallest
order_distances = list(zip(variations, distances))
order_distances.sort(key=lambda x: x[1])

#shortest trip in the beginning
print("Shortest trip (cycle): ")
shortest_trip = [str(city) for city in order_distances[0][0]] + [str(order_distances[0][0][0])]
print(shortest_trip, order_distances[0][1])
print("\n")


# population for subsets

total_population = sum(city.population for city in data[:n])
target_population = total_population / 2

best_match = float('inf')  #initial difference -> infinity
best_subset = None

populations = []
valid_subsets = [] #without repetitions (valid)

for subset in subsets:

    if len(set(subset)) != len(subset):  # if a city is doubled -> skip
        continue

    result = 0
    used = set() #no duplicates

    for city in subset:
        result += city.population

    populations.append(result)
    valid_subsets.append(subset)

    # if closer to 50% than previous match?
    if abs(result - target_population) < best_match:
        best_match = abs(result - target_population)
        best_subset = subset

# grouping subsets with their populations
subset_population = list(zip(valid_subsets, populations))
subset_population.sort(key=lambda x: abs(x[1] - target_population))  # sort by distance from 50%

print(f"Total population: {total_population}")
print(f"Target 50% population: {target_population:.2f}")
print("Closest subset to 50% of total population: ")
print([str(city) for city in best_subset], best_match + target_population)
print("\n")

# Population for subsets

total_population = sum(city.population for city in data[:n])
lower_bound = 0.4 * total_population
upper_bound = 0.6 * total_population

valid_count = 0  # Count of subsets within the 40%-60% range

populations = []
valid_subsets = []  # Subsets that do not contain repeated cities
total_subsets = len(subsets)  # Total number of generated subsets

for subset in subsets:
    if len(set(subset)) != len(subset):  # Skip subsets with duplicate cities
        continue

    subset_population = sum(city.population for city in subset)
    populations.append(subset_population)
    valid_subsets.append(subset)

    # Check if subset population is within the 40%-60% range
    if lower_bound <= subset_population <= upper_bound:
        valid_count += 1

# Compute probability
probability = valid_count / total_subsets if total_subsets > 0 else 0

print(f"Total population: {total_population}")
print(f"Population range for probability calculation: {lower_bound:.2f} - {upper_bound:.2f}")
print(f"Total subsets checked: {total_subsets}")
print(f"Valid subsets in range: {valid_count}")
print(f"Probability of a random subset falling within 40%-60% of total population: {probability:.4f}")