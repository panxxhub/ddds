#read csv file generate by spinalhdl /tmp/sin_wave_generator.csv
# do some fft anaylsis

from typing import List
import numpy as np
import matplotlib.pyplot as plt
import csv
import math
from scipy.fft import fft, fftfreq, fftshift

if __name__ == '__main__':
    data: List[float] = []
    with open('/tmp/sine_wave_generator.csv', 'r') as csvfile:
        # two column, first column is time, second column is data
        signal_reader = csv.reader(csvfile, delimiter=',')
        # read header first
        next(signal_reader)
        for row in signal_reader:
            time = float(row[0])
            # append data to list
            t = float(row[1]) + 8000 * np.sin(time)
            data.append(t)
    # convert list to numpy array
    data_serias = np.array(data)
    # do fft
    sp = fftshift(fft(data_serias))
    # get frequency
    freq = fftshift(fftfreq(data_serias.shape[-1]))
    # plot
    plt.plot(freq, sp.real, freq, sp.imag)
    plt.show()