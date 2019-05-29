from python_speech_features import mfcc
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np

mfcc_feat = [[]]

(rate,sig) = wav.read("Data/apple2.wav")
mfcc_feat = mfcc(sig,rate)
# print(type(mfcc_feat))
# print(len(mfcc_feat))
# for i in range(len(mfcc_feat)):
#     mfcc_feat /= 45
mfcc_mean = mfcc_feat
plt.plot(mfcc_mean)
plt.show()