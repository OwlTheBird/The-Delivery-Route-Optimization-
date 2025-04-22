import BruteForce as BF
from Graph import DeliveryGraph
import Greedy as GD
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def int_2_char(temp, labels):
    temp_list = []
    for node in temp:
        if isinstance(node, int):
            temp_list.append(labels[node])
        else:
            temp_list.append(node)
    return temp_list

    return labels[index]

def visualize(tried_paths, costs, best_path, best_cost, locations, interval=1500):
    # Prepare labels and coordinates
    labels = list(locations.keys())
    coords = [locations[label] for label in labels]
    
    # Convert label-based paths to index-based paths
    def convert_to_indices(path):
        if not path:
            return path
        if isinstance(path[0], str):  # If path contains labels
            return [labels.index(p) for p in path]
        return path  # If path already contains indices
    
    # Convert paths to indices
    tried_paths = [convert_to_indices(path) for path in tried_paths]
    best_path = convert_to_indices(best_path)

    # Build frames: each element is a tuple (kind, path, cost)
    frames = []
    if isinstance(tried_paths, list) and isinstance(costs, list):
        if len(tried_paths) == len(costs):
            for path, cost in zip(tried_paths, costs):
                if isinstance(path, list) and isinstance(cost, (int, float)):
                    frames.append(('trial', path, cost))

    # Add final optimal frame
    if isinstance(best_path, list) and isinstance(best_cost, (int, float)):
        frames.append(('optimal', best_path, best_cost))
    else:
        print("Warning: Invalid best_path or best_cost format.")

    if not frames:
        print("No valid paths to visualize.")
        return

    # Set up plot
    fig, ax = plt.subplots()
    x_vals, y_vals = zip(*coords)
    scatter = ax.scatter(x_vals, y_vals, s=100)
    for i, label in enumerate(labels):
        ax.text(x_vals[i], y_vals[i], label, fontsize=12, ha='right')

    line, = ax.plot([], [], lw=2)
    title = ax.set_title('')

    # Update function for animation
    def update(frame_data):
        kind, path, cost = frame_data
        visited = path if kind == 'optimal' else path[:len(path)]
        colors = ['green' if i in visited and kind == 'optimal'
                  else 'yellow' if i in path and kind == 'trial'
                  else 'black'
                  for i in range(len(labels))]
        scatter.set_color(colors)

        x_route = [coords[i][0] for i in path]
        y_route = [coords[i][1] for i in path]
        line.set_data(x_route, y_route)

        if kind == 'trial':
            title.set_text(f"Trial: cost={cost:.2f}")
        else:
            route_labels = int_2_char(path, labels)
            title.set_text(f"Optimal: {'-'.join(route_labels)}, cost={cost:.2f}")

        return scatter, line

    ani = animation.FuncAnimation(
        fig, update, frames=frames,
        interval=interval, blit=True, repeat=False
    )
    plt.show()

def get_user_input():
    user_input = input("Enter locations like this 'x1,y1 x2,y2 x3,y3 ': ").strip()
    locations = {}
    labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    points = user_input.split()
    for i, point in enumerate(points):
     x, y = map(float, point.split(','))
     label = labels[i]
     locations[label] = (x, y)

    return locations

def choose_algo(locations):
    while True:
        print("Options:")
        print("  1. Brute Force Algo")
        print("  2. Greedy Algo")
        print("  3. Graph Nearest Neighbor Algo")
        print("  4. 2-opt local refinement Algo")
        print("  5. Exit")

        choice = input("Enter the number of your choice: ").strip()

        if choice == '1':
            tried_paths, costs, opt_route, opt_cost = BF.bruteForce(locations)
            visualize(tried_paths, costs, opt_route, opt_cost, locations)
            
        elif choice == '2':
            opt_route, opt_cost = GD.greedy_delivery_route(locations)
            visualize([], [], opt_route, opt_cost, locations)

        elif choice == '3':
            graph = DeliveryGraph(locations)
            opt_route, opt_cost = graph.nearest_neighbor(0)  # Start from first node
            visualize([], [], opt_route, opt_cost, locations)

        elif choice == '4':
            graph = DeliveryGraph(locations)
            # Get initial tour using nearest neighbor
            nn_tour, nn_dist = graph.nearest_neighbor()
            # Improve it using two_opt
            opt_tour = graph.two_opt(nn_tour)
            opt_dist = graph.tour_length(opt_tour)
            # Pass the optimized tour and its cost to visualize
            visualize([nn_tour], [nn_dist], opt_tour, opt_dist, locations)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")


if __name__ == '__main__':
    locs = get_user_input()
    graph = DeliveryGraph(locations = {})
    choose_algo(locs)
