def greedy_delivery_route(points):
    n = len(points)
    if n == 0:
        return [], 0.0

    visited = [False] * n
    path = []
    current = 0  # Start at the first point
    visited[current] = True
    path.append(points[current])

    while len(path) < n:
        min_dist = float('inf')
        next_point = -1
        for i in range(n):
            if not visited[i]:
                # Calculate Euclidean distance
                dx = points[current][0] - points[i][0]
                dy = points[current][1] - points[i][1]
                dist = (dx ** 2 + dy ** 2) ** 0.5
                if dist < min_dist:
                    min_dist = dist
                    next_point = i
        if next_point == -1:
            break  # All points visited (safety check)
        visited[next_point] = True
        path.append(points[next_point])
        current = next_point

    # Calculate total distance including return to start
    total_distance = 0.0
    for i in range(len(path) - 1):
        dx = path[i][0] - path[i+1][0]
        dy = path[i][1] - path[i+1][1]
        total_distance += (dx**2 + dy**2) ** 0.5
    # Add distance from last point back to start
    dx = path[-1][0] - path[0][0]
    dy = path[-1][1] - path[0][1]
    total_distance += (dx**2 + dy**2) ** 0.5

    return path, total_distance

# Test case
locations = [(0, 0), (1, 1), (2, 3), (3, 2)]
route, distance = greedy_delivery_route(locations)

print("Optimized Delivery Route:")
print(" -> ".join([f"({x}, {y})" for x, y in route]))
print(f"Total Round-Trip Distance: {distance:.2f} units")