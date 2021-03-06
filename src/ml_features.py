
import numpy as np
import os
import pandas as pd

import config


def audio_to_fft(path):
    rate, data = wav.read(path)
    # wav file is mono.
    channel_1 = data[:]
    fourier = np.fft.fft(channel_1)
    return fourier


def extract_features():
    # Labelling Females and Males
    all_features = []
    y = []

    for filename in os.listdir(config.male_dir):
        # name = os.path.join(
        #     config.male_dir, filename)
        # fft = audio_to_fft(name)
        # fft.resize(30000)

        # ffts.append([fft.min().imag, fft.max().imag,
        #              np.std(fft).imag,
        #              np.mean(fft).imag,
        #              np.median(fft).imag
        #              ])
        # x = librosa.load(name, sr=None)

        df = pd.read_csv(os.path.join(config.male_dir, filename))
        features = df.values.tolist()
        all_features.append(features[0])

        y.append(0)

    for filename in os.listdir(config.female_dir):
        # fft = audio_to_fft(os.path.join(
        #     config.female_dir, filename))
        # fft.resize(30000)

        # ffts.append([
        #     fft.min().real,
        #     fft.max().real,
        #     np.std(fft).imag,
        #     np.mean(fft).imag,
        #     np.median(fft).imag,
        # ])
        # ffts.append(fft)

        df = pd.read_csv(os.path.join(config.female_dir, filename))
        features = df.values.tolist()
        all_features.append(features[0])

        y.append(1)
    return y, all_features
