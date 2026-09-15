def ucs(graph, start, end):
    """
        graph: Graf yang akan dicari
        start: Simpul awal
        end: Simpul tujuan
    """
    # Buat queue untuk menyimpan simpul-simpul yang belum dikunjungi
    queue = []

    # Tambahkan simpul awal ke queue dengan biaya awal 0
    queue.append((start, 0))

    # Buat dictionary untuk menyimpan jalur dan biaya setiap simpul
    path_cost = {start: 0}
    path = {}

    # Looping sampai queue kosong
    while queue:
        # Ambil simpul dan biayanya dari queue
        node, cost = queue.pop(0)

        # Jika simpul tersebut adalah simpul tujuan, maka rekonstruksi jalur dan return
        if node == end:
            path_nodes = []
            while node != start:
                path_nodes.append(node)
                node = path[node]
            path_nodes.append(start)
            return list(reversed(path_nodes))

        # Tambahkan semua tetangga simpul tersebut ke queue, diurutkan berdasarkan biaya
        for neighbor, neighbor_cost in graph.get(node, {}).items():
            new_cost = cost + neighbor_cost
            if neighbor not in path_cost or new_cost < path_cost[neighbor]:
                path_cost[neighbor] = new_cost
                queue.append((neighbor, new_cost))
                path[neighbor] = node

    # Jika tidak ada jalur yang ditemukan
    return None


# Definisikan graf berbobot: {simpul: {tetangga: biaya}}
graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'C': 3, 'D': 2},
    'B': {'G': 5},
    'C': {'E': 5},
    'D': {'G': 3},
    'E': {'G': 5},
    'G': {}
}

# Mulai pencarian dari simpul "S" ke simpul "G"
path = ucs(graph, 'S', 'G')

# Cetak jalur
if path:
    print("Jalur terpendek:", path)
else:
    print("Tidak ada jalur yang ditemukan.")