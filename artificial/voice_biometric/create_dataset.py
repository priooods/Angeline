from voice_biometric.prepocessing import Preposessing
import pandas as pd
import os

class Dataset():
    def __init__(self,_directory_dataset,_directory_audio):
        self.directory = _directory_dataset
        self.audio = _directory_audio
        
    # membuat csv dengan pandas dataframe
    # secara default filename csv diberi nama ab_dataset (Audio Biometric Dataset)
    def _new_dataset(self, audio=None, _label='', _filename_dataset='ab_dataset.csv'):
        # mengeluarkan data hasil extraksi
        _processing = Preposessing(audio)._feature_extraction()
        # menambahkan variabel label pada object extract
        # label berguna untuk melabeli data setiap hasil extraksi
        _processing['label'] = _label
        
        # membuat data frame
        _output = pd.DataFrame(data=[_processing])
        if not os.path.isfile(f"{self.directory}/{_filename_dataset}"): # check apabila file dataset tidak ada
            # buat csv dataset baru
            _output.to_csv(f"{self.directory}/{_filename_dataset}",index=False)
        else: # kalau file dataset sudah ada
            # tambah row baru ke csv yang sudah ada
            _output.to_csv(f"{self.directory}/{_filename_dataset}",index=False,header=None,mode='a')
        return _output
    
    def _run(self):    
        # memanggil class Dataset
        _dataset = Dataset(self.directory)
        
        # melakukan looping untuk mendapatkan semua audio file pada path audio
        for i,_audio_file in enumerate(os.listdir(self.audio)):
            _dataset._new_dataset(f"{self.audio}/{_audio_file}",'Prio')
    