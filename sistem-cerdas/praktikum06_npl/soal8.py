import speech_recognition as sr

listener = sr.Recognizer()

def dengar(prompt):
    """Merekam suara dan mengembalikannya sebagai teks (kosong jika gagal)."""
    with sr.Microphone() as sumber:
        listener.adjust_for_ambient_noise(sumber, duration=1)
        print(prompt)
        try:
            audio = listener.listen(sumber, timeout=5, phrase_time_limit=8)
            return listener.recognize_google(audio, language="id-ID")
        except (sr.WaitTimeoutError, sr.UnknownValueError):
            return ""
        except sr.RequestError:
            print("Tidak bisa terhubung ke layanan, cek internet")
            return ""

def diisi(teks):
    return teks.strip().lower() not in ("", "0", "nol")

nama = dengar("Sebutkan nama Anda ...")
print("Nama terdeteksi:", nama if nama else "(tidak diisi)")

if diisi(nama):
    print(f"Baik {nama}, silakan memilih menu selanjutnya")

    hobi = dengar("Sebutkan hobi Anda ...")
    print("Hobi terdeteksi:", hobi if hobi else "(tidak diisi)")

    if diisi(hobi):
        print(f"Wow, hobi anda adalah {hobi}")

print("Terima kasih")