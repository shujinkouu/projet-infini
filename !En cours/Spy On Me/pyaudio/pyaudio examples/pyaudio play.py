import pyaudio
import wave
import sys


CHUNK = 1024
'''
if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % wave)
    sys.exit(-1)
'''
wf = wave.open("C:\\Users\\Asus\\Desktop\\pyaudio examples\\filename.wav", 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

print('test')


while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()

if data == '':
    print("this doesn't work and for good reasons the data is void")


p.terminate()