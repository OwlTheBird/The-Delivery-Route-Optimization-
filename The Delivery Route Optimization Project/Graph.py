import math
from BruteForce import int_2_char

class DeliveryGraph:
    def __init__(self, locations):
        """Initialize graph with locations dictionary {'A': (x,y), 'B': (x,y), ...}"""
        self.labels = list(locations.keys())  # ['A', 'B', 'C', ...]
        self.points = [locations[label] for label in self.labels]  # [(x,y), (x,y), ...]
        self.distances = self._calculate_distances()

    def _calculate_distances(self):
        """Calculate distances between all points"""
        n = len(self.points)
        distances = {}
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    p1 = self.points[i]
                    p2 = self.points[j]
                    distances[(i,j)] = self._distance(p1, p2)
        return distances

    def _distance(self, p1, p2):
        """Calculate Euclidean distance between two points"""
        x_diff = p2[0] - p1[0]
        y_diff = p2[1] - p1[1]
        return math.sqrt(x_diff**2 + y_diff**2)

    def tour_length(self, tour):
        """Calculate total tour distance"""
        total = 0
        for i in range(len(tour) - 1):
            total += self.distances[(tour[i], tour[i+1])]
        return total

    def nearest_neighbor(self, start=0):
        """Find a tour using nearest neighbor algorithm"""
        n = len(self.points)
        unvisited = set(range(n))
        
        # Handle string labels (e.g., 'A', 'B', etc.)
        if isinstance(start, str):
            start = self.labels.index(start)
            
        # Build tour
        tour = [start]
        unvisited.remove(start)
        
        while unvisited:
            current = tour[-1]
            # Find nearest unvisited point
            next_point = min(unvisited, 
                           key=lambda x: self.distances[(current, x)])
            tour.append(next_point)
            unvisited.remove(next_point)
            
        tour.append(start)  # Return to start
        new_tour = self.tour_length(tour)
        print(f"\nOptimized Delivery Route: {int_2_char(tour)}, Length = {new_tour}")
        return tour, self.tour_length(tour)

    def two_opt(self, tour):
        """Improve tour using 2-opt algorithm"""
        if tour is None:
            tour = list(range(len(self.points))) + [0]
            
        best = tour
        while True:
            improved = False
            
            # Try to improve tour by reversing segments
            for i in range(1, len(best) - 2):
                for j in range(i + 1, len(best) - 1):
                    new_tour = best[:i] + best[i:j+1][::-1] + best[j+1:]
                    if self.tour_length(new_tour) < self.tour_length(best):
                        best = new_tour
                        improved = True
                        break
                if improved:
                    break
                    
            if not improved:
                break
                
        return best

    def get_route_labels(self, tour):
        """Convert index-based tour to city labels"""
        return [self.labels[i] for i in tour]