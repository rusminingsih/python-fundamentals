# Definisikan graf.
graph = {
    '1': ['2', '3', '4'],
    '2': [],
    '3': ['5', '6', '7', '8'],
    '4': [],
    '5': [],
    '6': ['9', '10'],
    '7': [],
    '8': [],
    '9': [],
    '10': []
}

def dfs(graph, start, end):

    # Buat stack untuk menyimpan JALUR (list simpul), bukan simpul tunggal.
    stack = []

    # Tambahkan jalur awal ke stack.
    stack.append([start])

    # Buat list simpul yang sudah dikunjungi.
    visited = []

    # Looping sampai stack kosong.
    while stack:
        # Ambil jalur terakhir dari stack (LIFO).
        path = stack.pop()

        # Ambil simpul terakhir dari jalur tersebut.
        node = path[-1]

        # Jika simpul tersebut adalah simpul tujuan, maka return jalur.
        if node == end:
            return path

        if node not in visited:
            visited.append(node)

            # Tambahkan semua simpul tetangga ke stack, mulai dari yang paling kanan
            # (supaya urutan pop tetap sesuai urutan kiri-ke-kanan).
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append(new_path)

    return None

# Mulai pencarian dari simpul "1" ke simpul "10".
path = dfs(graph, '1', '10')

# Cetak jalur.
print("Hasil Algoritma Depth-First Search:")
print(path)