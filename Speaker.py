import os
import random
import playsound
from gtts import gTTS


def voice_assist(input_text, *n):
    audio = gTTS(text=input_text, lang='en')
    r = random.randint(1, 10000)
    audio_file = 'audio-' + str(r) + '.mp3'
    audio.save(audio_file)
    print(input_text, *n)
    playsound.playsound(audio_file)
    os.remove(audio_file)
