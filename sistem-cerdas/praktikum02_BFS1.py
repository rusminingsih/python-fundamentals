# Definisikan sebuah kasus graf
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F': [],
    'G': ['J', 'K'],
    'H': [],
    'I': [],
    'J': [],
    'K': ['L'],
    'L': []
}

def bfs(graph, start, end):
    # Buat queue untuk menyimpan JALUR (list simpul), bukan simpul tunggal
    queue = []
    queue.append([start])

    # Buat list simpul yang sudah dikunjungi
    visited = []

    # Looping sampai queue kosong
    while queue:
        # Ambil jalur pertama dari queue
        path = queue.pop(0)

        # Ambil simpul terakhir dari jalur tersebut
        node = path[-1]

        # Jika simpul tersebut adalah simpul tujuan, maka return jalur
        if node == end:
            return path

        if node not in visited:
            visited.append(node)

            # mengiterasi melalui tetangga-tetangga dari simpul saat ini
            for neighbor in graph[node]:
                if neighbor not in visited:
                    # buat jalur baru = jalur lama + tetangga baru
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

    return None

# Kasus pencarian dari simpul A ke simpul L (akhir)
path = bfs(graph, 'A', 'L')

# Cetak jalur
print("Hasil Algoritma Breadth-First Search:")
print(path)