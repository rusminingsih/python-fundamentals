nilai_kelas_1 = float(input("Masukkan nilai kelas 1 :"))
nilai_kelas_2 = float(input("Masukkan nilai kelas 2 :"))
nilai_kelas_3 = float(input("Masukkan nilai kelas 3 :"))
nilai_kelas_4 = float(input("Masukkan nilai kelas 4 :"))
nilai_kelas_5 = float(input("Masukkan nilai kelas 5 :"))
nilai_kelas_6 = float(input("Masukkan nilai kelas 6 :"))

total = nilai_kelas_1 + nilai_kelas_2 + nilai_kelas_3 + nilai_kelas_4 + nilai_kelas_5 + nilai_kelas_6
print(total)

if total >= 80:
    print("Grade A")
else :
    print("Grande B")