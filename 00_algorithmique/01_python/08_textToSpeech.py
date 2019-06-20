from gtts import tts
import os
audio = tts.gTTS(text="Bonjour, ceci est un test",lang="fr")
audio.save("test.mp3")
os.system("mpg321 test.mp3")
os.system("rm test.mp3")