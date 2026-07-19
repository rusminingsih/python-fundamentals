import time

# print
print ("Hallo Ningsih")
print ("Selamat datang di program latihan.py")

# variabel 
nama = "Ningsih"
umur = 18
jurusan = "Teknik Informasi "

print (nama)
print (umur)
print (jurusan)
print (type(umur))

x = 9.6
y = 5

print (x * y)
print (type(x * y))

# list
fruit = ["jeruk", "apel", "mangga", "pisang"]
print (fruit)
print (type(fruit))


x = "jingga"
print (x[3])

# perulangan
for i in range (5):
    print (i)

for i in range (1,7):
    print ("#" * i)

for i in range (1, 6):
    print ("★" * i)

for i in range (6, 0, -1):
    print ("★" * i)

# animasi

teks = "Selamat datang semua"
for huruf in teks:
    print (huruf, end="", flush=True)
    time.sleep(0.1)