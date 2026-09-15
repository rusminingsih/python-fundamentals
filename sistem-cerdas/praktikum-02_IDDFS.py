def iddfs(graph, start, end, depth):
    """
    graph: Graf yang akan dicari.
    start: Simpul awal.
    end: Simpul tujuan.
    depth: Batas kedalaman pencarian.
    """
    # Buat stack untuk menyimpan (simpul, kedalaman, JALUR) yang belum dikunjungi.
    stack = []

    # Tambahkan simpul awal ke stack.
    stack.append((start, 0, [start]))

    # Looping sampai stack kosong.
    while stack:
        # Ambil simpul, kedalaman, dan jalurnya dari stack.
        node, current_depth, path = stack.pop()

        # Jika simpul tersebut adalah simpul tujuan, maka return jalur.
        if node == end:
            return path

        # Jika kedalaman pencarian belum mencapai batas, maka lanjutkan pencarian.
        if current_depth < depth:
            # Tambahkan semua simpul tetangga ke stack (dari kanan agar urutan kiri-ke-kanan terjaga),
            # dengan kedalaman +1 dan jalur yang diperbarui.
            for neighbor in reversed(graph[node]):
                if neighbor not in path:
                    stack.append((neighbor, current_depth + 1, path + [neighbor]))

    # Jika tujuan tidak ditemukan dalam batas kedalaman
    return None

# Definisikan graf
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': [],
    'F': ['K'],
    'G': [],
    'H': [],
    'I': [],
    'K': []
}

# Mulai pencarian dari simpul "A" ke simpul "G" dengan kedalaman 4.
path = iddfs(graph, 'A', 'G', 4)

# Cetak jalur.
print("Hasil Algoritma Iterative-Deepening Depth-First Search:")
print(path)