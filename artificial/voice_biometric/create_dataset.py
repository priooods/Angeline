from prepocessing import Preposessing
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os, fnmatch

class Dataset():
    def __init__(self,_outdir,_audio_dir):
        self._outdir = _outdir
        self._audio_dir = _audio_dir
        
    # membuat csv dengan pandas dataframe
    # secara default filename csv diberi nama ab_dataset (Audio Biometric Dataset)
    def _new_dataset(self, _label='', _filename_dataset='ab_dataset.csv'):
        
        # filtering file audio berdasatkan label input
        # pastikan audio yang ingin anda lakukan extraction memiliki filename sama dengan label yang anda masukan
        _files = fnmatch.filter(os.listdir(self._audio_dir),f'{_label}*.wav')
        if not _files:
            return print("WARNING : filename dengan nama {} tidak ditemukan".format(_label))
        
        # melakukan looping untuk mendapatkan semua audio file pada path audio
        _list = []
        for _audio in _files:
            # mengeluarkan data hasil extraksi
            _processing = Preposessing(f"{self._audio_dir}/{_audio}")._feature_extraction()
            # menambahkan variabel label pada object extract
            # label berguna untuk melabeli data setiap hasil extraksi
            _processing['label'] = _label
            # save semua value ke dalam array list
            _list.append(_processing)
        
        # membuat data frame
        _output = pd.DataFrame(data=_list)
        # kita lakukan encoder untuk setiap masing masing label
        _encoder = LabelEncoder()
        if not os.path.isfile(f"{self._outdir}/{_filename_dataset}"): # check apabila file dataset tidak ada
            # save column encoder dengan value hasil dari encoder column label
            _output['label_code'] = _encoder.fit_transform(_output['label'])
            # buat csv dataset baru
            return _output.to_csv(f"{self._outdir}/{_filename_dataset}",index=False)
        else: # kalau file dataset sudah ada
            # tambah row baru ke csv yang sudah ada
            # baca file csv yang udah ada
            _read_dataset = pd.read_csv(f"{self._outdir}/{_filename_dataset}")
            # update dengan cara menggabungkan array sebelum ( _read_dataset ) dengan array baru ( _ouput )
            _update = pd.concat([_read_dataset,_output])
            # karena ada case label name akan berbeda ketika update
            # maka kita panggil lagi encoder untuk membedakan encode pada label yang berbeda
            _update['label_code'] = _encoder.fit_transform(_update['label'])
            # save ke csv baru dengan nama sama
            # ga perlu index True karena dengan pandas read_csv index sudah autoincrement
            return _update.to_csv(f"{self._outdir}/{_filename_dataset}",index=False)