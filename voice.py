import pyttsx3

# Inisialisasi engine TTS
engine = pyttsx3.init()

# Atur kecepatan bicara (opsional)
engine.setProperty('rate', 150)  # 150 kata per menit

# Atur volume (opsional)
engine.setProperty('volume', 0.9)  # Nilai dari 0.0 sampai 1.0

# Fungsi untuk berbicara
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Input dari pengguna
text = input("Masukkan teks yang ingin dibaca: ")
speak(text)
