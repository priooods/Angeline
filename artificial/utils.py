import os
import wave,struct
import pyaudio

def read_audio_file(_file = "",_print_log=False):
    wav = wave.open(f"{_file}",'r')
    
    if _print_log:
        print(f"read file {_file}")
        
    _channel, _sample_width, _sample_rate, _nframes, _comptype, _compname = wav.getparams()
    assert _channel == 2 and _sample_width == 2 and _comptype == 'NONE'
    _frames = wav.readframes(_nframes * _channel)
    _sound = struct.unpack_from((str(_nframes)+'h') * _channel, _frames)
    wav.close()
    return _sample_rate, _channel, _sample_width, _sound

def save_audio_file(_new_filename = "", _sample_rate = 44100, _n_channels = 1
                    , _sample_width = 1, _sound = None, _print_log=False):
    wav = wave.open(_new_filename, "w")
    wav.setnchannels(_n_channels)
    wav.setsampwidth(_sample_width)
    wav.setframerate(_sample_rate)
    
    if _print_log:
        print(f"create new file {_new_filename}")
    
    for i in range(0, len(_sound)):
        wav.writeframesraw(struct.pack('<h', _sound[i]))
    
    
def manipulate_audio_filename(_directory = None, _new_filename = "", _remove_file=False):
    for i,file in enumerate(os.listdir(_directory), start=1):
        _sample_rate, _channel, _sample_width, _sound = read_audio_file(f"{_directory}\{file}",True)
        new_file = save_audio_file(f"{_directory}\{_new_filename}_{i}.wav",_sample_rate,_channel,_sample_width,_sound)
        if _remove_file:
            os.remove(f"{_directory}\{file}")
            
            
def create_voice_model(path_destination,_model_number=0,_format=pyaudio.paInt16,_channel=2,_rate=44100,_chunk=1024,_durasi_record=4):
    MODEL_NAME = input("Masukan nama untuk model voice anda ? ")
    MODEL_WAVE_OUT = f"{MODEL_NAME}_{_model_number}.wav"
    audio = pyaudio.PyAudio()
    
    stream = audio.open(format=_format,channels=_channel,rate=_rate,input=True,frames_per_buffer=_chunk)
    print("starting recording ...")
    
    frames = []
    for i in range(0, int(_rate / _chunk * _durasi_record)):
        data = stream.read(_chunk)
        frames.append(data)

    # Stop recording
    print("done recording !")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    wf = wave.open(os.path.join(path_destination,MODEL_WAVE_OUT), 'wb')
    wf.setnchannels(_channel)
    wf.setsampwidth(audio.get_sample_size(_format))
    wf.setframerate(_rate)
    wf.writeframes(b"".join(frames))
    wf.close()
    
    


import librosa
import librosa.display
import numpy as np
import scipy
from scipy.stats import entropy as en
import matplotlib.pyplot as plt

# Func untuk mengambarkan value dari frequensi 
# dan menghasilkan value berupa data frame
def describe_frequency(_signal,_sample_rate) -> float:
    
    # librosa.display.waveplot(_signal, sr=_sample_rate)
    # plt.xlabel("signal")
    # plt.ylabel("amplitude")
    # plt.show()
    # return
    
    # melakukan one-dimensional discrete Fourier Transform
    # untuk pemilihan konsep fft lainnya yang sesuai kebutuhan
    # dapat dilihat pada sumber : https://numpy.org/doc/stable/reference/routines.fft.html
    fft = np.fft.fft(_signal)
    # mendapatkan magnitude
    _magnitude = np.abs(fft)
    # mendapatkan frequency
    _frequency = np.linspace(0,_sample_rate,len(_magnitude))
    
    # mendapatkan mean frequency
    meanfreq = np.mean(_frequency)
    # mendapatkan standard deviation
    # refs articel : https://en.wikipedia.org/wiki/Standard_deviation
    std = np.std(_frequency) 
    # mendapatkan max fundamental frequency measured
    # refs articel : https://en.wikipedia.org/wiki/Fundamental_frequency
    maxfun = np.amax(_frequency)
    # mendapatkan min fundamental frequency measured
    # refs articel : https://en.wikipedia.org/wiki/Fundamental_frequency
    minfun = np.amin(_frequency) 
    # mendapatkan median frequency
    # refs articel : https://www.sciencedirect.com/topics/engineering/median-frequency
    median = np.median(_frequency)
    # mendapatkan skewnes
    # refs articel : https://en.wikipedia.org/wiki/Skewness
    skew = scipy.stats.skew(_frequency)
    # mendaptkan kurtosis
    # refs articel : https://en.wikipedia.org/wiki/Kurtosis
    kurt = scipy.stats.kurtosis(_frequency)
    # mendapatkan quantile pertama ( dengan besar Q = 0,25 )
    # refs articel : https://en.wikipedia.org/wiki/Quartile
    q1 = np.quantile(_frequency, 0.25)
    # mendapatkan quantile ketiga ( dengan besar Q = 0,75 )
    # refs articel : https://en.wikipedia.org/wiki/Quartile
    q3 = np.quantile(_frequency, 0.75)
    # medapatkan mode frequency
    # refs articel : https://en.wikipedia.org/wiki/Normal_mode
    mode = scipy.stats.mode(_frequency)[0][0]
    # mendapatkan interquantile range
    # refs articel : https://en.wikipedia.org/wiki/Interquartile_range
    iqr = scipy.stats.iqr(_frequency)
    
    sp_ent = en(_frequency, base=2)
    
    result = {
        "mean" : meanfreq,
        "std" : std,
        "median" : median,
        "skew" : skew,
        "kurt" : kurt,
        "q1" : q1,
        "q3" : q3,
        "iqr" : iqr,
        "sp_ent" : sp_ent,
    }
    
    return result

def extract_low_feature(_signal):
    zcr = librosa.feature.zero_crossing_rate(_signal)
    
    return zcr