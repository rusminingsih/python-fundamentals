from gtts import gTTS
from playsound import playsound

teks = input("Masukkan teks yang ingin diucapkan: ")
tts = gTTS(text=teks, lang='id', slow=True)
tts.save("suara.mp3")
print("Memutar suara...")
playsound("suara.mp3")