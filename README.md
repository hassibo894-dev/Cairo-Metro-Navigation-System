# 🚇 Cairo Metro Navigation System

A high-performance Python application designed to find the shortest and most efficient routes within the Cairo Metro network using advanced data structures and graph algorithms.

---

## 🚀 Features
* **Shortest Path Calculation:** Implements Breadth-First Search (BFS) to discover the path with the minimum number of stations between any two locations.
* **Dynamic Graph Representation:** Utilizes an adjacency list graph structure to map out metro lines, intersections, and transfer stations accurately.
* **User-Friendly Interface:** Clear command-line prompts that guide users to input their departure and destination stations seamlessly.

---

## 📂 Project Structure
The repository consists of the following core modules:
* `main.py` - The main entry point handling user interactions, inputs, and orchestrating the route planning flow.
* `graph.py` - Contains the `Graph` class definition responsible for building and managing the metro network's topology.
* `bfs.py` - Houses the core Breadth-First Search algorithm optimized for unweighted graph pathfinding.

---

## 🧠 Algorithms & Data Structures
This project demonstrates solid foundations in Computer Science principles:
* **Graph Theory:** Stations are treated as *Vertices* (Nodes) and the tracks connecting them as *Edges*.
* **BFS Algorithm:** Chosen specifically because the metro network is an unweighted graph, making BFS the most optimal choice ($O(V + E)$ time complexity) to guarantee the absolute shortest path.
* **Queues:** Utilized within the BFS implementation to manage node exploration order.

---

## 💻 How to Run
1. Clone this repository:
```bash
   git clone [https://github.com/hassibo894-dev/Cairo-Metro-Navigation-System.git](https://github.com/hassibo894-dev/Cairo-Metro-Navigation-System.git) 