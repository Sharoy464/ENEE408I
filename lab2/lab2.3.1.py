##Lab 2##

#3.1 Part A
# (2) Read the wav file “human_voice.wav” and write down its original sampling frequency.#

from scipy.io.wavfile import read as read_wav

sample_rate, data = read_wav("human_voice.wav")

print(f"The original sampling frequency is: {sample_rate} Hz")

# (3) Plot the signal using matplotlib#

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read as read_wav

sample_rate, data = read_wav("human_voice.wav")


if len(data.shape) > 1:
    data = data[:,0]

t = np.arange(len(data)) / sample_rate

plt.figure(figsize=(10,4))
plt.plot(t, data)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Original Signal")
plt.show()

# (4) Downsample the audio file to 8kHz without using inbuilt functions#

from scipy.io.wavfile import read as read_wav

sample_rate, data = read_wav("human_voice.wav")

new_fs = 8000
factor = sample_rate // new_fs

print("Original sampling rate:", sample_rate, "Hz")
print("New sampling rate:", new_fs, "Hz")
print("Downsampling factor:", factor)

# (6) Plot the downsampled signal using matplotlib.

downsampled = data[::factor]

if len(downsampled.shape) > 1:
    downsampled = downsampled[:,0]

t_new = np.arange(len(downsampled)) / new_fs

plt.figure(figsize=(10,4))
plt.plot(t_new, downsampled)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Downsampled Signal (8 kHz)")
plt.show()


# (7) Observe a section of the audio signal corresponding to the same time 
# period (hint: think of the sampling ratio and select two starting and 
# ending points). What differences do you notice? #

start_time = 0.5
end_time = 0.51

start_orig = int(start_time * sample_rate)
end_orig = int(end_time * sample_rate)

start_down = int(start_time * new_fs)
end_down = int(end_time * new_fs)

plt.figure(figsize=(10,4))
plt.plot(t[start_orig:end_orig], data[start_orig:end_orig], label="Original")
plt.plot(t_new[start_down:end_down], downsampled[start_down:end_down], label="Downsampled")
plt.legend()
plt.show()

