import matplotlib.pyplot as plt
import sounddevice as sd
plt.close('all')

#
Fs = 16000;
d = 3;

# record voice
print('Start Speaking')

a = sd.rec(int(d*Fs), Fs, 1)
sd.wait()
print('stop speaking')

plt.plot(a)
plt.title("Recorded Sound")

sd.play(a, Fs)