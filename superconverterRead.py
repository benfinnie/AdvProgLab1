#!/usr/bin/python3
import sys
import soundfile as sf
data, samplerate = sf.read('Trumpet.wav')

for x in range(len(data)):
	print(data[x]),
