import librosa
import librosa.display
import numpy as np
import scipy


# Func untuk mengambarkan value dari frequensi 
# dan menghasilkan value berupa data frame
def describe_frequency(freqs):
    # mendapatkan mean frequency
    meanfreq = np.mean(freqs)
    # mendapatkan standard deviation
    # refs articel : https://en.wikipedia.org/wiki/Standard_deviation
    std = np.std(freqs) 
    # mendapatkan max fundamental frequency measured
    # refs articel : https://en.wikipedia.org/wiki/Fundamental_frequency
    maxfun = np.amax(freqs)
    # mendapatkan min fundamental frequency measured
    # refs articel : https://en.wikipedia.org/wiki/Fundamental_frequency
    minfun = np.amin(freqs) 
    # mendapatkan median frequency
    # refs articel : https://www.sciencedirect.com/topics/engineering/median-frequency
    median = np.median(freqs)
    # mendapatkan skewness
    skew = scipy.stats.skew(freqs)
    # mendaptkan kurtosis
    kurt = scipy.stats.kurtosis(freqs)
    q1 = np.quantile(freqs, 0.25)
    q3 = np.quantile(freqs, 0.75)
    mode = scipy.stats.mode(freqs)[0][0]
    iqr = scipy.stats.iqr(freqs)