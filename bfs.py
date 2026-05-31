# ============================================================
# bfs.py - Breadth-First Search (BFS) Algorithm
# Subway Navigation System - Data Structures Project 2025-2026
# ============================================================


class Queue:
    """
    A custom Queue implementation (FIFO) using a Python list.
    Used by BFS to process stations level by level.
    """
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self._items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self._items.pop(0)

    def is_empty(self):
        """Return True if the queue has no items."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self._items)

    def __str__(self):
        return "Queue: " + str(self._items)


def bfs_shortest_path(graph, start, destination):
    """
    Perform Breadth-First Search to find the shortest path
    (fewest stops) between 'start' and 'destination' in the subway graph.

    Parameters:
    -----------
    graph       : SubwayGraph object
    start       : Name of the starting station (string)
    destination : Name of the destination station (string)

    Returns:
    --------
    path        : List of station names forming the shortest path,
                  or None if no path exists.
    """

    # --- Input Validation ---
    if not graph.station_exists(start):
        print(f"  [ERROR] Start station '{start}' does not exist.")
        return None
    if not graph.station_exists(destination):
        print(f"  [ERROR] Destination station '{destination}' does not exist.")
        return None
    if start == destination:
        print(f"  [INFO] You are already at '{start}'.")
        return [start]

    # --- BFS Setup ---
    # visited: set of stations already explored
    visited = set()

    # Queue stores tuples of (current_station, path_so_far)
    # Each path_so_far is the list of stations from start to current
    bfs_queue = Queue()
    bfs_queue.enqueue((start, [start]))

    visited.add(start)

    # --- BFS Traversal ---
    while not bfs_queue.is_empty():
        current_station, current_path = bfs_queue.dequeue()

        # Explore all neighbors of current_station
        neighbors = graph.get_neighbors(current_station)
        for neighbor in neighbors:
            if neighbor not in visited:
                new_path = current_path + [neighbor]

                # Check if we reached the destination
                if neighbor == destination:
                    return new_path

                # Otherwise, mark as visited and enqueue
                visited.add(neighbor)
                bfs_queue.enqueue((neighbor, new_path))

    # If queue is exhausted and destination not found → no path exists
    return None


def display_path_result(path, start, destination):
    """
    Nicely format and print the BFS result to the console.
    """
    print("\n" + "=" * 60)
    print(f"  ROUTE: {start}  -->  {destination}")
    print("=" * 60)

    if path is None:
        print(f"  [!] No route found between '{start}' and '{destination}'.")
        print("  The stations may not be connected in the network.")
    else:
        num_stops = len(path) - 1
        print(f"  Shortest Route Found ({num_stops} stop{'s' if num_stops != 1 else ''}):\n")

        # Print each step with arrow
        for i, station in enumerate(path):
            if i == 0:
                marker = "  [START]"
            elif i == len(path) - 1:
                marker = "  [ END ]"
            else:
                marker = f"  [  {i:2d}  ]"
            print(f"{marker}  {station}")
            if i < len(path) - 1:
                print("           |")
                print("           v")

        print(f"\n  Total Stops: {num_stops}")
        print(f"  Full Path:   {' → '.join(path)}")

    print("=" * 60)
    return path
