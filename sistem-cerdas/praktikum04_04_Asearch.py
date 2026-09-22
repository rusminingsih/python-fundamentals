def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {}          # menyimpan jarak (cost) dari start_node ke setiap node
    parents = {}    # menyimpan parent setiap node untuk merekonstruksi jalur

    # jarak start_node ke dirinya sendiri = 0
    g[start_node] = 0
    # start_node adalah root, jadi parent-nya adalah dirinya sendiri
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None

        # cari node di open_set dengan nilai f(n) = g(n) + h(n) terkecil
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node or Graph_nodes[n] is None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                # jika m belum pernah dilihat, tambahkan ke open_set
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # jika m sudah pernah dilihat, cek apakah jalur baru lewat n lebih pendek
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n is None:
            print('Path does not exist!')
            return None

        # kalau node saat ini adalah goal, rekonstruksi jalurnya
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()

            print('Path found: {}'.format(path))
            return path

        # pindahkan n dari open_set ke closed_set karena semua tetangganya sudah diperiksa
        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None


def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }
    return H_dist[n]


# graf: setiap key adalah node, isinya adalah list (tetangga, bobot)
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
}

if __name__ == "__main__":
    aStarAlgo('A', 'G')
    