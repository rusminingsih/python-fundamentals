"""
start: Simpul awal dari pencarian
goal: Simpul tujuan yang ingin dicapai
path: Daftar yang digunakan untuk melacak jalur yang sedang dieksplorasi
level: Kedalaman saat ini dalam pencarian
maxD: Kedalaman maksimum yang diizinkan dalam pencarian
"""

# Definisikan graf (relasi antar kota, dua arah)
graph = {
    'A': ['Z', 'S', 'T'],
    'Z': ['A', 'O'],
    'S': ['A', 'O', 'F', 'R'],
    'T': ['A', 'L'],
    'O': ['Z', 'S'],
    'F': ['S', 'B'],
    'R': ['S', 'C', 'P'],
    'L': ['T', 'M'],
    'B': ['F'],
    'C': ['R'],
    'P': ['R'],
    'M': ['L', 'D'],
    'D': ['M']
}

def DLS(start, goal, path, level, maxD):
    print('\nlevel sekarang-->', level)
    print('Node yg sedang dicek', start)

    # Simpul (start) saat ini ditambahkan pada list path
    path.append(start)

    # Pengecekan apakah simpul saat ini (start) sama dengan simpul tujuan (goal)
    if start == goal:
        print("Simpul tujuan")
        return path
    print('Bukan simpul tujuan')

    if level == maxD:
        return False
    print('\nLanjutkan dari simpul', start)

    # Jika simpul saat ini bukan merupakan simpul tujuan, pencarian melanjutkan ke simpul-simpul anak (child) dari simpul saat ini
    for child in graph[start]:

        # lewati simpul yang sudah ada di jalur saat ini (hindari balik ke leluhur/parent)
        if child in path:
            continue

        # Jika pencarian dari salah satu anak simpul berhasil mencapai tujuan
        if DLS(child, goal, path, level + 1, maxD):
            return path

        # simpul saat ini dihapus dari jalur
        path.pop()

    # Jika semua simpul anak telah dieksplorasi tanpa mencapai tujuan
    return False


start = 'A'
goal = input('Simpul tujuan:')
maxD = int(input("Maximum depth limit:"))
print()
path = list()
res = DLS(start, goal, path, 0, maxD)
if (res):
    print("\nJalur ke simpul tujuan telah ditemukan")
    print("Path", path)
else:
    print("\nJalur ke simpul tujuan tidak ditemukan dalam depth limit tsb.")