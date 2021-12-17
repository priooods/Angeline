import numpy as np
from scipy.stats import gmean
from scipy.io import wavfile
from pyAudioAnalysis import audioFeatureExtraction
import librosa

class Preposessing():
    
    def __init__(self, _audio_file):
        self.audio = _audio_file
    
    def _sprectral_extraction(self):
        # 1 . kita membaca signal audio dan sample rate dari sample audio yang kita punya
        _signal, _sample_rate = librosa.load(self.audio)


        # untuk pemilihan metode extraksi lainnya yang sesuai kebutuhan dan keinginan anda
        # dapat dilihat pada sumber : https://numpy.org/doc/stable/reference/routines.fft.html
        
        # 2 . memanggil func feature extraction dari module
        F,f_name = audioFeatureExtraction.stFeatureExtraction(_signal, _sample_rate, 0.050*_sample_rate, 0.025*_sample_rate)
        ## f_name ( merupakan label dari tiap masing masing value output extraksi feature ) 
        ## anda dapat melihat output dan mengambil value sesuai keperluan anda dengan code dibawah
        ### print(f"label : {f_name}")
        ## memanggil value dari masing-masing label dengan code dibawah
        ### contoh ---->  zcr = F[0]
        
        
        # 3 . memetakan output extraksi kedalam tiap-tiap variable
        # mendapatkan spectrum audio
        spec = np.abs(np.fft.rfft(_signal))
        # mendapatkan frequensi dari audio
        freq = np.fft.rfftfreq(len(_signal), d=1 / _sample_rate)
        peakf = np.argmax(freq) # tidak dipakai
        # mendapatkan amplitudo dari audio
        amp = spec / spec.sum()
        # mendapatkan mean frequency (Hz)
        mean = (freq * amp).sum()
        # mendapatkan standard deviation (Hz)
        # refs articel : https://en.wikipedia.org/wiki/Standard_deviation
        sd = np.sqrt(np.sum(amp * ((freq - mean) ** 2)))
        # mendapatkan jumlah kumulatif dari amplitudo
        amp_cumsum = np.cumsum(amp)
        # mendapatkan median frequency (Hz)
        # refs articel : https://www.sciencedirect.com/topics/engineering/median-frequency
        median = freq[len(amp_cumsum[amp_cumsum <= 0.5]) + 1]
        # medapatkan mode frequency (Hz)
        # refs articel : https://en.wikipedia.org/wiki/Normal_mode
        mode = freq[amp.argmax()]
        # mendapatkan quantile pertama ( dengan besar Q <= 0,25 ) (Hz)
        # refs articel : https://en.wikipedia.org/wiki/Quartile
        Q25 = freq[len(amp_cumsum[amp_cumsum <= 0.25]) + 1]
        # mendapatkan quantile ketiga ( dengan besar Q = 0,75 ) (Hz)
        # refs articel : https://en.wikipedia.org/wiki/Quartile
        Q75 = freq[len(amp_cumsum[amp_cumsum <= 0.75]) + 1]
        # mendapatkan interquantile range (Hz)
        # merupakan range antara Q75 dengan Q25
        # refs articel : https://en.wikipedia.org/wiki/Interquartile_range
        IQR = Q75 - Q25
        # mengeluarkan z dari amplitudo
        z = amp - amp.mean()
        # mendapatkan besar weight dari amplitudio
        w = amp.std()
        
        # mendapatkan skewnes
        # refs articel : https://en.wikipedia.org/wiki/Skewness
        skew = ((z ** 3).sum() / (len(spec) - 1)) / w ** 3
        # mendaptkan kurtosis
        # refs articel : https://en.wikipedia.org/wiki/Kurtosis
        kurt = ((z ** 4).sum() / (len(spec) - 1)) / w ** 4
        # mendaptkan Spectral flatness
        # refs articel : https://en.wikipedia.org/wiki/Spectral_flatness
        spec_flatness = gmean(spec**2)/np.mean(spec**2)

        result_d = {
            'meanfreq': mean/1000, # (kHz)
            'sd': sd/1000, # (kHz)
            'median': median/1000, # (kHz)
            'Q25': Q25/1000, # (kHz)
            'Q75': Q75/1000, # (kHz)
            'IQR': IQR/1000, # (kHz)
            'skew': skew,
            'kurt': kurt,
            'sp.ent': F[5].mean(),
            'sfm': spec_flatness,
            'mode': mode/1000, # (kHz)
            'centroid': F[3].mean()/1000, # (kHz)
        }
        return result_d
