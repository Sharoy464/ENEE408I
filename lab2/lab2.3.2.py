##Lab 2##

from scipy.io.wavfile import read as read_wav
import numpy as np
import matplotlib.pyplot as plt

#3.2 Part B
# (1) Calculate the rms values for each of the audio signals M1.wav, M2.wav and M3.wav using
# Python. (Here M1.wav is the audio signal received by the microphone M1)

m1_sampling_rate, m1 = read_wav("M1.wav")
m2_sampling_rate, m2 = read_wav("M2.wav")
m3_sampling_rate, m3 = read_wav("M3.wav")

m1 = m1.astype(np.float64)
m2 = m2.astype(np.float64)
m3 = m3.astype(np.float64)

m = np.vstack([m1, m2, m3])
squared = np.square(m)
means = np.mean(squared, axis=1)
rms = np.sqrt(means)
print("RMS:", rms)

# (3) Using crosscorrelation, calculate the time delay between the audio signals received
# between M1 and M2 using Python. Try to compute this without the use of inbuilt functions.

N = len(m1)
M = len(m2)

m1_padded = np.pad(m1, M-1)
cross = np.zeros(N + M - 1)

for i in range(N + M - 1):
    segment = m1_padded[i:i+M]
    cross[i] = np.sum(segment * m2)

print("Cross-correlation:", cross)
