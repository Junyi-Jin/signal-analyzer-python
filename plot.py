import matplotlib.pyplot as plt
import numpy as np

def plot_time_domain(t,original,filtered,title):
    plt.figure(figsize=(10,4))
    plt.plot(t,original,label="Original Signal",alpha=0.7)
    plt.plot(t,filtered,label="Filtered Signal",linewidth=2)
    plt.xlabel("Time(s)")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.legend
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_fft (freqs,original_fft,filtered_fft,title):
    plt.figure(figsize=(10,4))
    plt.plot(freqs, np.abs(original_fft),label="Original FFT")
    plt.plot(freqs,np.abs(filtered_fft),label="Filtered FFT")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()