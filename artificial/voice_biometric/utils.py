import os
import wave,struct
import pyaudio

def read_audio_file(_file = "",_print_log=False):
    wav = wave.open(f"{_file}",'r') # pertama kita membaca file audio yang di jadikan input
    
    if _print_log: # nyalakan true kalau kita mau ngechek apakah method read_audio_file berhasil baca audio input nya
        print(f"read file {_file}") 
        
    # kita mengeluarkan output yang ada pada audio yang kita baca    
    _channel, _sample_width, _sample_rate, _nframes, _comptype, _compname = wav.getparams()
    # assert _channel == 2 and _sample_width == 2 and _comptype == 'NONE'
    _frames = wav.readframes(_nframes * _channel) # hasil output teersebut kita baca frame by frame nya
    _sound = struct.unpack_from((str(_nframes)+'h') * _channel, _frames) # kita petakan urutan audio nya jadi satu kesatuan
    wav.close() # setelah kita selesai membaca isi dari sebuah audio. kita hentikan proses membaca audionya
    return _sample_rate, _channel, _sample_width, _sound # keluarkan nilai-nilai output yang ingin kita baca

def save_audio_file(_new_filename = "", _sample_rate = 44100, _n_channels = 1
                    , _sample_width = 1, _sound = None, _print_log=False):
    wav = wave.open(_new_filename, "w") # kita buat sebuah file audio dengan ( filename = nama file yang kita buat , w = perintah write )
    wav.setnchannels(_n_channels) # kita atur nilai channel nya ( default = 1 )
    wav.setsampwidth(_sample_width) # kita atur nilai width nya ( default = 1)
    wav.setframerate(_sample_rate) # kita atur nilai rate nya ( default = 44100 )
    
    if _print_log: # check apakah file berhasil terbuat dengan mengubah menjadi TRUE
        print(f"create new file {_new_filename}")
    
    for i in range(0, len(_sound)): # setelah itu kita susun frame-frame audio menjadi kesatuan 
        wav.writeframesraw(struct.pack('<h', _sound[i]))
    
    
def manipulate_audio_filename(_directory = None, _new_filename = "", _remove_file=False):
    for i,file in enumerate(os.listdir(_directory), start=1): # kita panggil semua file audio yang ada pada sebuah directry folder audio kita
        # lalu kita bedah semua audio yang ada pada directory audio
        _sample_rate, _channel, _sample_width, _sound = read_audio_file(f"{_directory}\{file}",True) # kita keluarkan nilai nilai acuan dari audio yg kita baca
        # setelah itu kita buat audio file baru ( copy ) dengan nilai nilai yang sudah didapat dari audio sebelumnya ( audoi.wav )
        # dan simpan hasilnya ke audio dengan filename baru namun directory yang sama ( audio(1).wav )
        new_file = save_audio_file(f"{_directory}\{_new_filename}_{i}.wav",_sample_rate,_channel,_sample_width,_sound)
        if _remove_file: # kita juga bisa menghapus audio lama supaya tidak double ( audio.wav ) apabila dibutuhkan dengan mengubah nya jadi TRUE
            os.remove(f"{_directory}\{file}")
            
            
def create_voice_model(path_destination,_model_number=0,_format=pyaudio.paInt16,_channel=2,_rate=44100,_chunk=1024,_durasi_record=4):
    MODEL_NAME = input("Masukan nama untuk model voice anda ? ") # kita masukan input nama file diterminal sesuai yang kita mau
    MODEL_WAVE_OUT = f"{MODEL_NAME}_{_model_number}.wav" # output filename audio akan jadi sesuai dengan name yang anda input
    audio = pyaudio.PyAudio() # buka stream
    
    stream = audio.open(format=_format,channels=_channel,rate=_rate,input=True,frames_per_buffer=_chunk)
    print("starting recording ...") # mulai merecord
    
    frames = [] # frame hasil stream kita petakan disini
    for i in range(0, int(_rate / _chunk * _durasi_record)):
        data = stream.read(_chunk) # kita baca frame by frame dari stream
        frames.append(data) # kita satukan semua frame yang dibaca

    # Stop recording
    print("done recording !")
    stream.stop_stream() # hentikan stream
    stream.close() # tutup stream
    audio.terminate() # kita matikan audio record

    wf = wave.open(os.path.join(path_destination,MODEL_WAVE_OUT), 'wb') # kita buat file baru dengan filename yang kita masukan tdi
    wf.setnchannels(_channel) # atur nilai channelnya
    wf.setsampwidth(audio.get_sample_size(_format)) # atur nilai width nya
    wf.setframerate(_rate) # atur nilai sample rate nya
    wf.writeframes(b"".join(frames)) # masukan hasil frame yang telah dibaca
    wf.close() # tutup
    
    