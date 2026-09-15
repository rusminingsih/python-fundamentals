import matplotlib.pyplot as plt

# Memasukkan data secara langsung di dalam kode program
# untuk menghindari error pembacaan file Excel yang rusak
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei']
penjualan = [12000, 15000, 18000, 14000, 20000]

# Membuat Bar Chart (Grafik Batang) warna biru
plt.bar(bulan, penjualan, color='blue')

# Menambahkan label sumbu x, y, dan judul grafik
plt.xlabel('Bulan')
plt.ylabel('Penjualan (juta)')
plt.title('Grafik Penjualan Produk per Bulan')

# Menampilkan grafik batang
plt.show()
