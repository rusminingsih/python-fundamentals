import pyttsx3

engine = pyttsx3.init()

# b) tempo lebih cepat 70
rate = engine.getProperty('rate')
print("Rate awal:", rate)
engine.setProperty('rate', rate + 70)
print("Rate baru:", engine.getProperty('rate'))

# c) volume lebih pelan 50%
engine.setProperty('volume', 0.5)
print("Volume:", engine.getProperty('volume'))

# a) dan d) suara perempuan berbahasa Indonesia
for v in engine.getProperty('voices'):
    if 'damayanti' in v.name.lower():
        engine.setProperty('voice', v.id)
        print("Suara dipakai:", v.name)
        break
else:
    print("Suara Damayanti tidak ditemukan")

teks = input("Masukkan teks yang ingin diucapkan: ")
print("Mengucapkan:", teks)
engine.say(teks)
engine.runAndWait()

print("Rate setelah bicara:", engine.getProperty('rate'))
print("Volume setelah bicara:", engine.getProperty('volume'))