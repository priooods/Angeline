from voice_identification.prepocessing import Preposessing
import librosa
import utils
import os
from scipy.io import wavfile


# utils.create_voice_model(r"C:\Users\prio\Desktop\Angeline\artificial\audio\prio",1)

# directory model audio
_directory = r"C:\Users\prio\Desktop\Angeline\artificial\audio\prio\prio_1.wav"

preposes = Preposessing(_directory)
print(f"output {preposes._sprectral_extraction()}")
# # membuat looping dari keseluruhan audio model pada dir model
# for i,file in enumerate(os.listdir(_directory)):
#     _signal,_sample_rate = librosa.load(f"{_directory}\{file}")
#     sample = Processing(_signal,16000)
#     # print(f"librosa === resulting ke {i} , nilai : \n {sample.get_mfcc_()} ")
#     print(f"speech === resulting ke {i} , nilai : \n {sample.get_mfcc_two()} ")
