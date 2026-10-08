import speech_recognition as sr

listener = sr.Recognizer()
with sr.Microphone() as input_source:
    listener.adjust_for_ambient_noise(input_source, duration=1)
    print("Silakan bicara dalam bahasa Indonesia ...")
    voice_input = listener.listen(input_source, timeout=5, phrase_time_limit=8)

try:
    text = listener.recognize_google(voice_input, language="id-ID")
    print("Hasil:", text)
except sr.UnknownValueError:
    print("Suara tidak dikenali, coba lagi")
except sr.RequestError:
    print("Tidak bisa terhubung ke layanan, cek internet")