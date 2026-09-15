# membuat graph tree
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'I'],
    'D': ['I'],
    'E': [],
    'F': [],
    'G': [],
    'I': []
}
# visit_complete = daftar yang digunakan untuk melacak simpul-simpul yang telah dikunjungi
# graph = graph yang akan dijelajahi, biasanya dalam bentuk dictionary, di mana setiap simpul adalah kunci (key)
# dan tetangga-tetangga dari simpul tersebut disimpan dalam list sebagai nilainya.
# current_node = simpul awal

def bfs(visit_complete, graph, current_node):
    
    # menginisialisasi pencarian dengan menambahkan simpul awal ke dalam list visit_complete
    visit_complete.append(current_node)
    
    # inisiasi queue
    queue = []
    
    # simpul awal ditambahkan ke dalam queue
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
                
                # menambahkan tetangga tersebut ke list visit_complete
                visit_complete.append(neighbour)
                
                # memasukkan ke queue
                queue.append(neighbour)

print("Hasil Algoritma Breadth-First Search:")
# panggil fungsi bfs
bfs([], graph, 'A')
