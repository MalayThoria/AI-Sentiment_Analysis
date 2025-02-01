import wave
import matplotlib.pyplot as plt
import numpy as np

obj=wave.open("C:/Users/Malay Thoria/Desktop/ai_ml_pro/wave/malay.wav",'rb')

sample_freq=obj.getframerate()
n_sample=obj.getnframes()
signal_wave=obj.readframes(-1)

obj.close()

t_audio=n_sample/sample_freq

print(t_audio)

signal_array=np.frombuffer(signal_wave,dtype=np.int16)
times = np.linspace(0, t_audio, num=len(signal_array))
if len(times) != len(signal_array):
    print("Error: Dimensions of times and signal_array do not match.")
    exit()

plt.figure(figsize=(15,5))
plt.plot(times,signal_array)
plt.title("audio Signal")
plt.ylabel("signal Wave")
plt.xlabel("Time(s)")
plt.xlim(0,t_audio)
plt.show()