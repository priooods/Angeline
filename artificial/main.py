from voice_biometric.prepocessing import Preposessing
import json

# membaca directory model audio dari config.json
_config = open('./config.json')
# load file json
_config = json.load(_config)
# mendapatkan lokasi directori
_directory_audio = _config['angeline']['model']['audio_training_dir']
print(_directory_audio)
# 
# preposes = Preposessing()
# print(f"output {preposes._new_dataset('Prio',)}")
# # membuat looping dari keseluruhan audio model pada dir model
# for i,file in enumerate(os.listdir(_directory)):
#     _signal,_sample_rate = librosa.load(f"{_directory}\{file}")
#     sample = Processing(_signal,16000)
#     # print(f"librosa === resulting ke {i} , nilai : \n {sample.get_mfcc_()} ")
#     print(f"speech === resulting ke {i} , nilai : \n {sample.get_mfcc_two()} ")
