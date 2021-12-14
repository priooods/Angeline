import os
import wave,struct

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