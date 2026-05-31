# ============================================================
# main.py - Subway Navigation System (Main Application)
# Data Structures Project 2025-2026 (2nd Term)
# Core Concepts: Graphs, Breadth-First Search (BFS)
# ============================================================
# Cairo Metro - 3 Lines, 66 Stations
# ============================================================

from graph import SubwayGraph
from bfs import bfs_shortest_path, display_path_result


# ─────────────────────────────────────────────────────────────
#  BUILD THE SUBWAY GRAPH
# ─────────────────────────────────────────────────────────────

def build_cairo_metro():
    """
    Build a SubwayGraph for the Cairo Metro network.
    Line 1: Helwan ↔ New El-Marg  (36 stations)
    Line 2: Shobra El-Kheima ↔ El-Mounib  (20 stations)
    Line 3: Adly Mansour ↔ Kit Kat  (17 stations, partial)
    Interchange stations connect the lines.
    """
    graph = SubwayGraph()

    # ── Line 1 Stations (Helwan → New El-Marg) ──────────────
    line1 = [
        "Helwan", "Ain Helwan", "Helwan University", "Wadi Hof",
        "Hadayek Helwan", "El-Maasara", "Tora El-Asmant",
        "Kozzika", "Tora El-Balad", "Sakanat El-Maadi",
        "Maadi", "Hadayek El-Maadi", "Dar El-Salam",
        "El-Zahraa", "Mar Girgis", "El-Malek El-Saleh",
        "Al-Sayeda Zeinab", "Saad Zaghloul", "Sadat",
        "Nasser", "Orabi", "Al-Shohadaa",
        "Ghamra", "El-Demerdash", "Manshiet El-Sadr",
        "Kobri El-Qobba", "Hammamat El-Qobba", "Saray El-Qobba",
        "Hadayek El-Zeitoun", "Helmeyet El-Zeitoun",
        "El-Matareyya", "Ain Shams", "Ezbet El-Nakhl",
        "El-Marg", "New El-Marg"
    ]

    # ── Line 2 Stations (Shobra El-Kheima → El-Mounib) ─────
    line2 = [
        "Shobra El-Kheima", "Kolleyyet El-Zeraa", "Mezallat",
        "Khalafawy", "St. Teresa", "Rod El-Farag",
        "Massarra", "Al-Shohadaa",        # interchange with Line 1
        "Attaba", "Mohamed Naguib",
        "Sadat",                           # interchange with Line 1
        "Opera", "Dokki", "El-Bohoos",
        "Cairo University", "Faisal",
        "Giza", "Omm El-Masryeen",
        "Sakiat Mekky", "El-Mounib"
    ]

    # ── Line 3 Stations (Adly Mansour → Kit Kat) ────────────
    line3 = [
        "Adly Mansour", "El-Haykestep", "Omar Ibn El-Khattab",
        "Qobaa", "Hesham Barakat", "El-Nozha",
        "Nadi El-Shams", "Alf Maskan", "Heliopolis Square",
        "Haroun", "Stadium", "Abbaseya",
        "Abdou Pasha", "El-Geish", "Bab El-Shaeria",
        "Attaba",                          # interchange with Line 2
        "Nasser",                          # interchange with Line 1
        "Maspero", "Zamalek", "Kit Kat"
    ]

    # ── Add all stations ────────────────────────────────────
    all_stations = set(line1 + line2 + line3)
    for station in all_stations:
        graph.adjacency_list[station] = __import__('graph').LinkedList()
        graph.num_stations += 1

    # ── Add Line 1 tracks (consecutive stations) ────────────
    for i in range(len(line1) - 1):
        graph.add_track(line1[i], line1[i + 1])

    # ── Add Line 2 tracks ───────────────────────────────────
    for i in range(len(line2) - 1):
        graph.add_track(line2[i], line2[i + 1])

    # ── Add Line 3 tracks ───────────────────────────────────
    for i in range(len(line3) - 1):
        graph.add_track(line3[i], line3[i + 1])

    return graph


# ─────────────────────────────────────────────────────────────
#  HELPER DISPLAY FUNCTIONS
# ─────────────────────────────────────────────────────────────

def print_header():
    print("\n" + "╔" + "═" * 58 + "╗")
    print("║" + "  🚇  CAIRO METRO SUBWAY NAVIGATION SYSTEM  🚇  ".center(58) + "║")
    print("║" + "  Data Structures Project 2025-2026 (2nd Term)  ".center(58) + "║")
    print("╚" + "═" * 58 + "╝")


def print_main_menu():
    print("\n" + "─" * 60)
    print("  MAIN MENU")
    print("─" * 60)
    print("  1. Find Shortest Route (BFS)")
    print("  2. View All Stations")
    print("  3. View Station Connections")
    print("  4. Add a New Station")
    print("  5. Add a New Track Between Stations")
    print("  6. Remove a Station")
    print("  7. Display Full Network Map")
    print("  0. Exit")
    print("─" * 60)


def list_all_stations(graph):
    stations = graph.get_all_stations()
    print(f"\n  {'─'*56}")
    print(f"  Total Stations in Network: {len(stations)}")
    print(f"  {'─'*56}")
    # Print in 3 columns
    col_width = 26
    for i, s in enumerate(stations):
        end = "\n" if (i + 1) % 3 == 0 or i == len(stations) - 1 else ""
        print(f"  {s:<{col_width}}", end=end)
    print()


# ─────────────────────────────────────────────────────────────
#  MAIN PROGRAM LOOP
# ─────────────────────────────────────────────────────────────

def main():
    print_header()
    print("\n  Building Cairo Metro network...")
    graph = build_cairo_metro()
    print(f"\n  ✓ Network ready: {graph.num_stations} stations, {graph.num_tracks} tracks.\n")

    while True:
        print_main_menu()
        choice = input("  Enter your choice: ").strip()

        # ── Option 1: Find Shortest Route ───────────────────
        if choice == "1":
            print("\n  ── FIND SHORTEST ROUTE ──")
            list_all_stations(graph)
            start = input("\n  Enter START station: ").strip()
            dest  = input("  Enter DESTINATION station: ").strip()

            if not start or not dest:
                print("  [ERROR] Station names cannot be empty.")
                continue

            path = bfs_shortest_path(graph, start, dest)
            display_path_result(path, start, dest)

        # ── Option 2: View All Stations ──────────────────────
        elif choice == "2":
            print("\n  ── ALL STATIONS ──")
            list_all_stations(graph)

        # ── Option 3: View Station Connections ───────────────
        elif choice == "3":
            print("\n  ── STATION CONNECTIONS ──")
            station = input("  Enter station name: ").strip()
            if not station:
                print("  [ERROR] Station name cannot be empty.")
                continue
            if not graph.station_exists(station):
                print(f"  [ERROR] Station '{station}' not found.")
            else:
                neighbors = graph.get_neighbors(station)
                print(f"\n  '{station}' connects to:")
                if neighbors:
                    for n in neighbors:
                        print(f"    → {n}")
                else:
                    print("    (No connections)")

        # ── Option 4: Add New Station ────────────────────────
        elif choice == "4":
            print("\n  ── ADD NEW STATION ──")
            name = input("  Enter new station name: ").strip()
            if not name:
                print("  [ERROR] Station name cannot be empty.")
            else:
                graph.add_station(name)

        # ── Option 5: Add New Track ──────────────────────────
        elif choice == "5":
            print("\n  ── ADD NEW TRACK ──")
            s1 = input("  Enter first station: ").strip()
            s2 = input("  Enter second station: ").strip()
            if not s1 or not s2:
                print("  [ERROR] Station names cannot be empty.")
            else:
                graph.add_track(s1, s2)

        # ── Option 6: Remove Station ─────────────────────────
        elif choice == "6":
            print("\n  ── REMOVE STATION ──")
            name = input("  Enter station name to remove: ").strip()
            if not name:
                print("  [ERROR] Station name cannot be empty.")
            else:
                graph.remove_station(name)

        # ── Option 7: Display Full Network Map ───────────────
        elif choice == "7":
            print("\n  ── FULL NETWORK MAP (Adjacency List) ──")
            graph.display_graph()

        # ── Exit ──────────────────────────────────────────────
        elif choice == "0":
            print("\n  Thank you for using the Cairo Metro Navigation System!")
            print("  Safe travels! 🚇\n")
            break

        # ── Invalid Input ─────────────────────────────────────
        else:
            print(f"\n  [ERROR] Invalid choice '{choice}'. Please enter a number from 0 to 7.")


# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
