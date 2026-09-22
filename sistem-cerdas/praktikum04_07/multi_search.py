import heapq
from collections import deque


# =========================================================
# 1. BACA DATA
# =========================================================
def load_graph(filename="jalan.txt"):
    """Membaca jalan.txt -> graf dua arah {kota: [(tetangga, jarak), ...]}"""
    graph = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            city1 = parts[0].strip()
            city2 = parts[1].strip()
            cost = int(parts[2].strip())
            graph.setdefault(city1, []).append((city2, cost))
            graph.setdefault(city2, []).append((city1, cost))
    return graph


def load_heuristic(filename="heuristicjalan.txt"):
    """Membaca heuristicjalan.txt -> dict {kota: nilai heuristik ke Bucharest}"""
    h = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            node = parts[0].strip()
            val = int(parts[1].strip())
            h[node] = val
    return h


def reconstruct_path(parent, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path


def path_cost(graph, path):
    """Menghitung total jarak dari sebuah rute yang sudah ditemukan."""
    total = 0
    for i in range(len(path) - 1):
        for (city, cost) in graph[path[i]]:
            if city == path[i + 1]:
                total += cost
                break
    return total


# =========================================================
# 2. ALGORITMA PENCARIAN
# =========================================================
def bfs(graph, start, goal):
    frontier = deque([start])
    parent = {start: None}
    explored = []
    while frontier:
        node = frontier.popleft()
        explored.append(node)
        if node == goal:
            return reconstruct_path(parent, start, goal), explored
        for neighbor, _ in graph.get(node, []):
            if neighbor not in parent:
                parent[neighbor] = node
                frontier.append(neighbor)
    return None, explored


def dfs(graph, start, goal):
    stack = [start]
    parent = {start: None}
    visited = {start}
    explored = []
    while stack:
        node = stack.pop()
        explored.append(node)
        if node == goal:
            return reconstruct_path(parent, start, goal), explored
        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                stack.append(neighbor)
    return None, explored


def ucs(graph, start, goal):
    """Uniform Cost Search: selalu ambil node dengan g(n) (biaya kumulatif) terkecil."""
    frontier = [(0, start)]
    parent = {start: None}
    best_cost = {start: 0}
    visited = set()
    explored = []
    while frontier:
        cost, node = heapq.heappop(frontier)
        if node in visited:
            continue
        visited.add(node)
        explored.append(node)
        if node == goal:
            return reconstruct_path(parent, start, goal), explored, cost
        for neighbor, w in graph.get(node, []):
            new_cost = cost + w
            if neighbor not in best_cost or new_cost < best_cost[neighbor]:
                best_cost[neighbor] = new_cost
                parent[neighbor] = node
                heapq.heappush(frontier, (new_cost, neighbor))
    return None, explored, None


def gbfs(graph, start, goal, h):
    """Greedy Best-First Search: hanya mengejar h(n), tidak peduli biaya yang sudah ditempuh."""
    frontier = [(h.get(start, 0), start)]
    parent = {start: None}
    visited = set()
    explored = []
    while frontier:
        _, node = heapq.heappop(frontier)
        if node in visited:
            continue
        visited.add(node)
        explored.append(node)
        if node == goal:
            return reconstruct_path(parent, start, goal), explored
        for neighbor, w in graph.get(node, []):
            if neighbor not in visited:
                parent.setdefault(neighbor, node)
                heapq.heappush(frontier, (h.get(neighbor, 0), neighbor))
    return None, explored


def astar(graph, start, goal, h):
    """A*: memilih node dengan f(n) = g(n) + h(n) terkecil, meng-update g(n) bila jalur lebih murah ditemukan."""
    frontier = [(h.get(start, 0), start)]
    parent = {start: None}
    g_score = {start: 0}
    explored = []
    while frontier:
        f, node = heapq.heappop(frontier)
        explored.append(node)
        if node == goal:
            return reconstruct_path(parent, start, goal), explored, g_score[goal]
        for neighbor, w in graph.get(node, []):
            tentative_g = g_score[node] + w
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                parent[neighbor] = node
                f_score = tentative_g + h.get(neighbor, 0)
                heapq.heappush(frontier, (f_score, neighbor))
    return None, explored, None


# =========================================================
# 3. PROGRAM UTAMA (MENU PILIHAN ALGORITMA)
# =========================================================
def main():
    graph = load_graph()
    h = load_heuristic()

    print("=" * 55)
    print(" PROGRAM PENCARIAN RUTE KOTA ROMANIA")
    print(" Algoritma tersedia : BFS, DFS, UCS, GBFS, A*")
    print("=" * 55)

    asal = input("Masukkan kota asal   : ").strip()
    tujuan = input("Masukkan kota tujuan : ").strip()
    algo = input("Pilih algoritma (BFS/DFS/UCS/GBFS/A*) : ").strip().upper()

    if asal not in graph:
        print(f"\nKota asal '{asal}' tidak ditemukan dalam data.")
        return
    if tujuan not in graph:
        print(f"\nKota tujuan '{tujuan}' tidak ditemukan dalam data.")
        return

    cost = None
    if algo == "BFS":
        path, explored = bfs(graph, asal, tujuan)
    elif algo == "DFS":
        path, explored = dfs(graph, asal, tujuan)
    elif algo == "UCS":
        path, explored, cost = ucs(graph, asal, tujuan)
    elif algo == "GBFS":
        path, explored = gbfs(graph, asal, tujuan, h)
    elif algo in ("A*", "ASTAR", "A-STAR"):
        algo = "A*"
        path, explored, cost = astar(graph, asal, tujuan, h)
    else:
        print(f"\nAlgoritma '{algo}' tidak dikenali. Pilih salah satu: BFS, DFS, UCS, GBFS, A*")
        return

    print()
    print(f"Algoritma            : {algo}")
    if path:
        if cost is None:
            cost = path_cost(graph, path)
        print(f"Rute ditemukan       : {' -> '.join(path)}")
        print(f"Total jarak          : {cost} km")
        print(f"Jumlah kota dieksplorasi : {len(explored)}")
        print(f"Urutan eksplorasi    : {explored}")
    else:
        print("Rute tidak ditemukan.")


if __name__ == "__main__":
    main()