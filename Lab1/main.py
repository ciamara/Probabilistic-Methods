def generate_orders(data: list, k: int, current: list = None, n: int = 0, results: list = None):
    # permutations(orders) of length k

    if current is None:
        current = []
    if results is None:
        results = []

    #the permutation is complete
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
        n, results = generate_orders(new_data, k, new_current, n, results)

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

n = 5
k = 3
m = 3

#input and format data
with open("italy.txt", "r") as file:
    data: list[City] = []
    for line in file.readlines()[1:n+1]:
        line_data = line.strip().replace('\n', '').split(' ')
        data.append(City(int(line_data[0]), line_data[1], int(line_data[2]), float(line_data[3]), float(line_data[4])))

#create orders(porzadki odwiedzin M z N)
print("Permutations(orders)")
orders_count, orders = generate_orders(data, k)
print(f"n = {n}, k = {k}, orders_count = {orders_count}\n\n")

#subsets(podzbiory z mozliwymi powtorzeniami)
print("Subsets: ")
subsets_count, subsets = generate_subsets(data, m)
print(f"n = {n}, m = {m}, subsets_count = {subsets_count}\n\n")

#distances for all permutations(orders)
distances = []
for order in orders:
    result = 0
    current = order[0]
    for city in order[1:]:
        result += current.distance(city)
        current = city
    result += current.distance(order[0])
    distances.append(result)

# ascending sort so the first entry is the smallest
order_distances = list(zip(orders, distances))
order_distances.sort(key=lambda x: x[1])

#shortest trip in the beginning
print("Shortest trip: ")
print([str(x) for x in order_distances[0][0]], order_distances[0][1])
print("\n")


# population for subsets

total_population = sum(city.population for city in data[:n])
target_population = total_population / 2

best_match = float('inf')  #initial difference -> infinity
best_subset = None

populations = []
for subset in subsets:
    result = 0
    used = set() #no duplicates

    for city in subset:
        if city in used:
            continue  # we skip the cities that have been used
        result += city.population
        used.add(city)

    #population
    populations.append(result)

    # if closer to 50% than previous match?
    if abs(result - target_population) < best_match:
        best_match = abs(result - target_population)
        best_subset = subset

# grouping subsets with their populations
subset_population = list(zip(subsets, populations))
subset_population.sort(key=lambda x: abs(x[1] - target_population))  # sort by distance from 50%

print(f"Total population: {total_population}")
print(f"Target 50% population: {target_population:.2f}")
print("Closest subset to 50% of total population: ")
print([str(city) for city in best_subset], best_match + target_population)
print("\n")