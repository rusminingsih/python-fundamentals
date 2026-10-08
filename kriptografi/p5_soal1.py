from collections import Counter
from math import gcd
from functools import reduce

ct = "CACGBIPMVTLTSAAJIMLAXGVWTLNQCDLNCGLTXAYGUALRVYMEFRHNJXCKNYXXYTVTOALRHYLBAIAJIAVAAJIKTSRXDXCUGGUTDEOKTNXPEUAXDDVSCELIFGTBYAAJIMLAXGVWTSVSXTYDVXCTYGNXABALNSICLNTGVFPNTOZBXKNTQGQOESILTIAOSXAAQGXBSAXRIBY"

# 1. Kasiski: cari pola 4 huruf yang berulang, hitung jarak, cari FPB
posisi = {}
for i in range(len(ct) - 3):
    posisi.setdefault(ct[i:i+4], []).append(i + 1)
jarak = []
for pola, p in posisi.items():
    if len(p) > 1:
        d = [p[j+1] - p[j] for j in range(len(p) - 1)]
        jarak += d
        print("Pola", pola, "posisi", p, "jarak", d)
m = reduce(gcd, jarak)
print("Panjang kunci (FPB) =", m)

# 2. Analisis frekuensi tiap kolom
kunci = ""
for j in range(m):
    kolom = ct[j::m]
    freq = Counter(kolom)
    print("Kolom", j+1, freq.most_common(3))
    # skor: A*19 + N*15 + I*7 (frekuensi bahasa Indonesia)
    skor = {}
    for k in range(26):
        skor[k] = (19*freq.get(chr(k+65), 0)
                   + 15*freq.get(chr((13+k) % 26 + 65), 0)
                   + 7*freq.get(chr((8+k) % 26 + 65), 0))
    kunci += chr(max(skor, key=skor.get) + 65)
print("Kunci =", kunci)

# 3. Dekripsi: P = (C - K) mod 26
pt = "".join(chr((ord(c) - ord(kunci[i % m])) % 26 + 65) for i, c in enumerate(ct))
print("Plaintext =", pt)