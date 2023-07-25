from funasr_onnx import Fsmn_vad
import librosa
import numpy as np
from pydub import AudioSegment
import os
import glob

M_PATH_TO_AUDIO = '/raid/kaisar_dauletbek/datasets/Voice_Conversion/voice_male/'
F_PATH_TO_AUDIO = '/raid/kaisar_dauletbek/datasets/Voice_Conversion/voice_female/'

# f_voices_to_check = open("f_voices_to_check_edited.txt", "r")
# m_voices_to_check = open("m_voices_to_check_edited.txt", "r")

# f_voices_to_check = f_voices_to_check.readlines()
# f_voices_to_check = [F_PATH_TO_AUDIO+"female_218_002.wav"]
# f_voices_to_check = [F_PATH_TO_AUDIO + line.strip() + '.wav' for line in f_voices_to_check]

# m_voices_to_check = m_voices_to_check.readlines()
# m_voices_to_check = [M_PATH_TO_AUDIO+"male_169_001.wav", M_PATH_TO_AUDIO+"male_100_001.wav"]
# m_voices_to_check = [M_PATH_TO_AUDIO + line.strip() + '.wav' for line in m_voices_to_check]

# m_voices_to_check = m_voices_to_check[:20]
# f_voices_to_check = f_voices_to_check[:20]

m_voices = glob.glob(M_PATH_TO_AUDIO + "*.wav")
f_voices = glob.glob(F_PATH_TO_AUDIO + "*.wav")

m_voices_reject = glob.glob("/raid/saida_mussakhojayeva/datasets/Voice_Conversion/voice_male_rejected/*.wav")
f_voices_reject = glob.glob("/raid/saida_mussakhojayeva/datasets/Voice_Conversion/voice_female_rejected/*.wav")

for reject in m_voices_reject:
    # try:
    reject = M_PATH_TO_AUDIO + reject.split("/")[-1]
    m_voices.remove(reject)
    # except:
        # pass

for reject in f_voices_reject:
    # try:
    reject = F_PATH_TO_AUDIO + reject.split("/")[-1]
    f_voices.remove(reject)
    # except:
        # pass

def segment_audio(input_file, intervals):
    file_name = input_file.split("/")[-1].split(".")[0]
    examples_dir = "/raid/kaisar_dauletbek/segment_speech/voice_conversion_segmented"
    os.mkdir(f"{examples_dir}/{file_name}")
    audio = AudioSegment.from_file(input_file)

    for i, (start_time, end_time) in enumerate(intervals):
        chunk = audio[start_time:end_time]
        chunk.export(f"{examples_dir}/{file_name}/{i}.wav", format="wav")

def generate_intervals(input_audio, model):
    print(f"Generating intervals...")
    intervals = model(input_audio)
    return intervals[0]

model_dir = "./FSMN-VAD"
model = Fsmn_vad(model_dir, quantize=True)


for i, audio in enumerate(m_voices):
    print(f"Processing {i} male audio")
    intervals = generate_intervals(audio, model)
    segment_audio(audio, intervals)

for i, audio in enumerate(f_voices_reject):
    print(f"Processing {i} female audio")
    intervals = generate_intervals(audio, model)
    segment_audio(audio, intervals)