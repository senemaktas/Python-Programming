# Speech to text transcription from the audio file
# 1-install: pip/pip3 install SpeechRecognition  2-install: pip/pip3 install pydub  3-install : sudo apt install ffmpeg

import speech_recognition as sr
from pydub import AudioSegment

sound = AudioSegment.from_mp3("/home/.../output.mp3")

sound.export("text.wav" , format="wav")

text_audio = "text.wav"

r = sr.Recognizer()

with sr.AudioFile(text_audio) as source:
    textAudio = r.record(source)

X = r.recognize_google(textAudio)

print(X)
print(sr.__version__)

# Speech recognition using Google Speech Recognition
try:
    print("You said: " + X)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

text_file = open("/home/.../sample.txt", "w")  #write mode 
n = text_file.write(X)
text_file.close()
