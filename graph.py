# ============================================================
# graph.py - Custom Graph Implementation using Adjacency List
# Subway Navigation System - Data Structures Project 2025-2026
# ============================================================

class Node:
    """
    Represents a single node in a linked list used for adjacency lists.
    Each node holds a station neighbor and a pointer to the next node.
    """
    def __init__(self, station):
        self.station = station   # Name of the neighboring station
        self.next = None         # Pointer to next neighbor node


class LinkedList:
    """
    A custom Linked List to store neighbors of each station.
    Used as the value in the adjacency dictionary.
    """
    def __init__(self):
        self.head = None

    def add_neighbor(self, station):
        """Add a new neighboring station to the linked list."""
        new_node = Node(station)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get_neighbors(self):
        """Return all neighbors as a Python list."""
        neighbors = []
        current = self.head
        while current:
            neighbors.append(current.station)
            current = current.next
        return neighbors

    def __str__(self):
        neighbors = self.get_neighbors()
        return " -> ".join(neighbors) if neighbors else "(no neighbors)"


class SubwayGraph:
    """
    An undirected, unweighted Graph representing a subway system.
    Stations are nodes; tracks between stations are edges.
    Adjacency list is stored using a dictionary of custom LinkedLists.
    """
    def __init__(self):
        # adjacency_list: { station_name: LinkedList of neighbors }
        self.adjacency_list = {}
        self.num_stations = 0
        self.num_tracks = 0

    def add_station(self, station):
        """
        Add a new station (node) to the graph.
        If station already exists, do nothing.
        """
        if station not in self.adjacency_list:
            self.adjacency_list[station] = LinkedList()
            self.num_stations += 1
            print(f"  [+] Station '{station}' added.")
        else:
            print(f"  [!] Station '{station}' already exists.")

    def add_track(self, station_a, station_b):
        """
        Add an undirected edge (track) between two stations.
        Both stations must exist in the graph first.
        """
        if station_a not in self.adjacency_list:
            print(f"  [ERROR] Station '{station_a}' not found.")
            return
        if station_b not in self.adjacency_list:
            print(f"  [ERROR] Station '{station_b}' not found.")
            return
        if station_a == station_b:
            print(f"  [ERROR] Cannot connect a station to itself.")
            return

        # Check if track already exists
        if station_b in self.adjacency_list[station_a].get_neighbors():
            print(f"  [!] Track between '{station_a}' and '{station_b}' already exists.")
            return

        # Add edge in both directions (undirected graph)
        self.adjacency_list[station_a].add_neighbor(station_b)
        self.adjacency_list[station_b].add_neighbor(station_a)
        self.num_tracks += 1
        print(f"  [+] Track added: {station_a} <---> {station_b}")

    def remove_station(self, station):
        """
        Remove a station and all its connected tracks from the graph.
        """
        if station not in self.adjacency_list:
            print(f"  [ERROR] Station '{station}' not found.")
            return

        # Remove all edges pointing TO this station from neighbors
        neighbors = self.adjacency_list[station].get_neighbors()
        for neighbor in neighbors:
            self._remove_neighbor(neighbor, station)
            self.num_tracks -= 1

        # Remove the station itself
        del self.adjacency_list[station]
        self.num_stations -= 1
        print(f"  [-] Station '{station}' and all its tracks removed.")

    def _remove_neighbor(self, from_station, target):
        """
        Helper: Remove 'target' from the neighbor linked list of 'from_station'.
        """
        ll = self.adjacency_list[from_station]
        if ll.head is None:
            return
        # If head is the target
        if ll.head.station == target:
            ll.head = ll.head.next
            return
        current = ll.head
        while current.next:
            if current.next.station == target:
                current.next = current.next.next
                return
            current = current.next

    def get_neighbors(self, station):
        """Return the list of neighbors for a given station."""
        if station not in self.adjacency_list:
            print(f"  [ERROR] Station '{station}' not found.")
            return []
        return self.adjacency_list[station].get_neighbors()

    def display_graph(self):
        """Print the full adjacency list of the graph."""
        if not self.adjacency_list:
            print("  (Graph is empty)")
            return
        print(f"\n  {'STATION':<25} CONNECTED TO")
        print("  " + "-" * 55)
        for station, ll in sorted(self.adjacency_list.items()):
            print(f"  {station:<25} {ll}")
        print(f"\n  Total Stations: {self.num_stations} | Total Tracks: {self.num_tracks}")

    def station_exists(self, station):
        """Check if a station exists in the graph."""
        return station in self.adjacency_list

    def get_all_stations(self):
        """Return a sorted list of all station names."""
        return sorted(self.adjacency_list.keys())
