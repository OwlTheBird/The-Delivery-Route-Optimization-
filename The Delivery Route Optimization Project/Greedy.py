def greedy_delivery_route(locations):
    # Convert dictionary to list of points while keeping track of labels
    labels = list(locations.keys())
    points = [locations[label] for label in labels]
    
    n = len(points)
    if n == 0:
        return [], 0.0

    visited = [False] * n
    path = []
    path_indices = []  # Keep track of indices for label conversion
    current = 0  # Start at the first point
    visited[current] = True
    path.append(points[current])
    path_indices.append(current)

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
        path_indices.append(next_point)
        current = next_point

    # Add return to start
    path.append(points[0])
    path_indices.append(0)

    # Calculate total distance
    total_distance = 0.0
    for i in range(len(path) - 1):
        dx = path[i][0] - path[i+1][0]
        dy = path[i][1] - path[i+1][1]
        total_distance += (dx**2 + dy**2) ** 0.5

    # Convert indices to labels for output
    route_labels = [labels[i] for i in path_indices]
    
    print("\nOptimized Delivery Route:")
    print(" -> ".join(route_labels))
    print(f"Total Round-Trip Distance: {total_distance:.2f} units")

    return route_labels, total_distance