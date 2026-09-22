def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {}            # menyimpan jarak (cost) dari start_node ke tiap node
    parents = {}      # parents menyimpan peta induk (parent) tiap node

    # jarak start_node dari dirinya sendiri = 0
    g[start_node] = 0
    # start_node adalah root, jadi parent-nya adalah dirinya sendiri
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None

        # cari node dengan nilai f() = g(n) + h(n) terkecil di open_set
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node or Graph_nodes[n] is None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                # jika 'm' belum ada di open_set maupun closed_set, tambahkan
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    # jika sudah pernah ditemukan, cek apakah jalur baru lewat n lebih murah
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n is None:
            print('Path does not exist!')
            return None

        # jika node saat ini adalah goal, susun ulang jalurnya
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()

            print('Path found: {}'.format(path))
            print('Total cost: {}'.format(g[stop_node]))
            return path

        # pindahkan n dari open_set ke closed_set
        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None


# mengembalikan daftar tetangga & jarak dari node yang diberikan
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


# nilai heuristik tiap node (h) sesuai gambar soal
def heuristic(n):
    H_dist = {
        'S': 7,
        'A': 9,
        'B': 4,
        'C': 2,
        'D': 5,
        'E': 3,
        'G': 0,
    }
    return H_dist[n]


# graph sesuai gambar soal (arah panah S -> A/D -> ... -> G)
Graph_nodes = {
    'S': [('A', 3), ('D', 2)],
    'A': [('B', 5), ('C', 10)],
    'B': [('C', 2), ('E', 1)],
    'C': [('G', 4)],
    'D': [('B', 1), ('E', 4)],
    'E': [('G', 3)],
    'G': None,
}

aStarAlgo('S', 'G')