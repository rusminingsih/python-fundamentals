import pyttsx3

engine = pyttsx3.init()

for v in engine.getProperty('voices'):
    if 'damayanti' in v.name.lower():
        engine.setProperty('voice', v.id)
        break

def bicara(teks):
    print("Suara:", teks)
    engine.say(teks)
    engine.runAndWait()

def diisi(teks):
    return teks.strip() != "" and teks.strip() != "0"

nama = input("Masukkan nama: ")

if diisi(nama):
    bicara(f"Baik {nama}, silakan memilih menu selanjutnya")

    hobi = input("Masukkan hobi: ")

    if diisi(hobi):
        bicara(f"Wow, hobi anda adalah {hobi}")

bicara("Terima kasih")