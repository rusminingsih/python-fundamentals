# ============================================
# Graf peta kota-kota di Jerman (dua arah, dengan jarak/km sebagai bobot)
# ============================================
graph = {
    'Frankfurt': {'Mannheim': 85, 'Wurzburg': 217, 'Kassel': 173},
    'Mannheim': {'Frankfurt': 85, 'Karlsruhe': 80},
    'Karlsruhe': {'Mannheim': 80, 'Augsburg': 250},
    'Augsburg': {'Karlsruhe': 250, 'Munchen': 84},
    'Wurzburg': {'Frankfurt': 217, 'Erfurt': 186, 'Nurnberg': 103},
    'Erfurt': {'Wurzburg': 186},
    'Nurnberg': {'Wurzburg': 103, 'Stuttgart': 183, 'Munchen': 167},
    'Stuttgart': {'Nurnberg': 183},
    'Kassel': {'Frankfurt': 173, 'Munchen': 502},
    'Munchen': {'Kassel': 502, 'Augsburg': 84, 'Nurnberg': 167}
}


# ============================================
# a. BFS - menentukan jalur/urutan penjelajahan mulai dari Frankfurt
# ============================================
def bfs(visit_complete, graph, current_node):
    # menginisialisasi pencarian dengan menambahkan simpul awal ke dalam list visit_complete
    visit_complete.append(current_node)

    # inisiasi queue
    queue = []
    queue.append(current_node)

    # bila masih ada simpul yang harus dijelajahi
    while queue:
        # mengambil simpul pertama dari antrian queue
        s = queue.pop(0)

        # simpul yang sedang dijelajahi
        print(s)

        # mengiterasi melalui tetangga-tetangga dari simpul saat ini (s)
        for neighbour in graph[s]:
            # cek apakah tetangga tersebut belum pernah dikunjungi
            if neighbour not in visit_complete:
                visit_complete.append(neighbour)
                queue.append(neighbour)


print("=== a. Hasil Algoritma Breadth-First Search dari Frankfurt ===")
bfs([], graph, "Frankfurt")


# ============================================
# b. UCS - menentukan jalur TERMURAH dari Frankfurt ke Stuttgart
# ============================================
def ucs(graph, start, end):
    """
        graph: Graf yang akan dicari
        start: Simpul awal
        end: Simpul tujuan
    """
    queue = [(start, 0)]
    path_cost = {start: 0}
    path = {}

    while queue:
        node, cost = queue.pop(0)

        if node == end:
            path_nodes = []
            while node != start:
                path_nodes.append(node)
                node = path[node]
            path_nodes.append(start)
            return list(reversed(path_nodes)), path_cost[end]

        for neighbor, neighbor_cost in graph.get(node, {}).items():
            new_cost = cost + neighbor_cost
            if neighbor not in path_cost or new_cost < path_cost[neighbor]:
                path_cost[neighbor] = new_cost
                queue.append((neighbor, new_cost))
                path[neighbor] = node

    return None, None


print("\n=== b. Hasil Algoritma Uniform-Cost Search: Frankfurt -> Stuttgart ===")
route, total_cost = ucs(graph, 'Frankfurt', 'Stuttgart')
if route:
    print("Jalur termurah:", route)
    print("Total jarak:", total_cost, "km")
else:
    print("Tidak ada jalur yang ditemukan.")