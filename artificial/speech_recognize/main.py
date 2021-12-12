import librosa
import librosa.display
import IPython.display as ipd


data,rate = librosa.load(r"C:\Users\prio\Desktop\Angeline\artificial\audio\prio_217.wav")
librosa.display.waveplot(data,sr=rate)