# file: fft_analyzer.py
import matplotlib.pyplot as plt
import numpy as np
#Basic FFT computation
def compute_fft(signal, fs):
    N = len(signal)
    fft_vals = np.fft.fft(signal)
    fft_vals = np.abs(fft_vals) / N      # normalize magnitude
    freqs = np.fft.fftfreq(N, 1/fs)
  # Only keep positive frequencies
    mask = freqs >= 0
    return freqs[mask], fft_vals[mask]

#visualizes the waveform in the time domain
def plot_time_domain(signal, fs, title="Time-domain Signal"):
    """
    Plot the time-domain signal.
    """
    t = np.arange(len(signal)) / fs
    plt.figure(figsize=(8, 3))
    plt.plot(t, signal)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
#visualizes the magnitude spectrum in the frequency domain
def plot_frequency_spectrum(freqs, magnitude, title="Magnitude Spectrum"):
    """
    Plot the frequency-domain magnitude spectrum.
    """
    plt.figure(figsize=(8, 3))
    plt.plot(freqs, magnitude)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
def compare_frequency_response(freqs1, mag1, freqs2, mag2,
                               label1="Original", label2="Filtered"):
    """
    Plot two magnitude spectra for comparison.
    """
    plt.figure(figsize=(8, 3))
    plt.plot(freqs1, mag1, label=label1)
    plt.plot(freqs2, mag2, label=label2)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title("Frequency-domain Comparison")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()