import librosa
import os
import glob

DATA_PATH = "/raid/kaisar_dauletbek/segment_speech/voice_conversion_segmented"

audios = glob.glob(DATA_PATH + "/*/*.wav")
f = open("audios_more_than_20s.txt", "w")

for audio in audios:
    if librosa.get_duration(filename=audio) < 1.99:
        os.remove(audio)
        print("Removed: ", audio)
    elif librosa.get_duration(filename=audio) > 20.0:
        f.write(audio+"\n")