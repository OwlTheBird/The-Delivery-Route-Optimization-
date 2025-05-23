import math

locations = {
    'A': (0, 0),
    'B': (1, 1),
    'C': (2, 3),
    'D': (3, 2)
}
temp = [0, 1, 2, 3]

# Convert index-based paths to human-readable city labels

def int_2_char(temp):
    temp_list = []
    lables = list(locations.keys())
    for i in range(len(temp)):
        temp_list.append(lables[temp[i]])
    return temp_list

# Euclidean distance calculation between two coordinate points

def Distances_EuclideanEquation(C, C2):  # C = (x1, y1), C2 = (x2, y2)
    x_diff = C[0] - C2[0]
    y_diff = C[1] - C2[1]
    distance = math.sqrt(x_diff**2 + y_diff**2)
    return distance

# Build full pairwise distance matrix for the cities

def distances_MatrixResults(locations):
    cityNum = len(locations)
    lables = list(locations.keys())
    distancesMatrix = [[0 for _ in range(cityNum)] for _ in range(cityNum)]
    for row in range(cityNum):
        for column in range(cityNum):
            CityOne = locations[lables[row]]
            CityTwo = locations[lables[column]]
            distancesMatrix[row][column] = Distances_EuclideanEquation(CityOne, CityTwo)
    return distancesMatrix

# Recursive permutation generator

def permutations(lst):
    if len(lst) <= 1:
        return [lst]
    result = []
    for i in range(len(lst)):
        rest = lst[:i] + lst[i+1:]
        for perm in permutations(rest):
            result.append([lst[i]] + perm)
    return result

# Brute-force TSP: collect all tried paths + their costs, then return optimal solution

def bruteForce(locations):
    distance_Matrix = distances_MatrixResults(locations)
    length = len(locations)
    city_indices = list(range(length))

    tried_paths = []   # list of all paths tested
    costs = []         # corresponding cost for each path
    min_cost = None    # best cost found
    best_path = []     # best path found

    # Fix city 0 as the starting and ending point
    for perm in permutations(city_indices[1:]):
        path = [0] + perm + [0]
        tried_paths.append(path)
        cost = sum(
            distance_Matrix[path[i]][path[i+1]]
            for i in range(len(path) - 1)
        )
        print("Trying path:", int_2_char(path))
        print(f"  --> Cost: {cost:.2f}\n")

        costs.append(cost)
        if min_cost is None or cost < min_cost:
            min_cost = cost
            best_path = path

    print("* Best Path:", int_2_char(best_path))
    print(f"* Minimum Cost: {min_cost:.2f}")

    return tried_paths, costs, best_path, min_cost