# algoritma DFS
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': [],
    '8': []
}

visited = set()  # set/himpunan graf yg dikunjungi

def dfs(visited, graph, node):
    # memeriksa apakah simpul saat ini belum pernah dikunjungi
    if node not in visited:

        # mencetak simpul saat ini yang sedang dijelajahi
        print(node)

        # menandai simpul saat ini sebagai telah dikunjungi dan menambahkan ke set visited
        visited.add(node)

        # mengiterasi melalui tetangga-tetangga dari simpul saat ini
        for neighbour in graph[node]:

            # memanggil fungsi dfs secara rekursif untuk menjelajahi tetangga yang belum pernah dikunjungi
            dfs(visited, graph, neighbour)

# Cetak jalur
print("Hasil Algoritma Depth-First Search:")
dfs(visited, graph, '5')

