# 1. Mengambil input dua angka dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua:   "))

# 2. Menampilkan pilihan operasi
print("\nPilih Operasi:")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")

pilihan = input("Masukkan pilihan (1/2/3/4): ")

# 3. Proses hitung berdasarkan pilihan
if pilihan == '1':
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil}")
elif pilihan == '2':
    hasil = angka1 - angka2
    print(f"Hasil: {angka1} - {angka2} = {hasil}")
elif pilihan == '3':
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} * {angka2} = {hasil}")
elif pilihan == '4':
    # Antisipasi error pembagian dengan angka nol
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil}")
    else:
        print("Error: Angka tidak bisa dibagi dengan nol!")
else:
    print("Pilihan operasi tidak valid!")
