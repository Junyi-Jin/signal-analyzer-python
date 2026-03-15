import numpy as np

from filters import apply_lowpass_filter,apply_highpass_filter,apply_bandpass_filter
from plot import plot_time_domain,plot_fft

def analyze_and_filter_signal(t,signal,fs):
 #Compute FFT of the original signal
    original_fft=np.fft.fft(signal)
    freqs=np.fft.fftfreq(len(signal),1/fs)
  #------ Apply Filters ------
    low_filtered=apply_lowpass_filter(signal,cutoff=40,fs=fs,order=4)
    high_filtered=apply_highpass_filter(signal,cutoff=10,fs=fs,order=4)
    band_filtered=apply_bandpass_filter(signal,lowcut=10,highcut=40,fs=fs,order=4)

    low_fft=np.fft.fft(low_filtered)
    high_fft=np.fft.fft(high_filtered)
    band_fft=np.fft.fft(band_filtered)
  #-------- Plot Time Domain -------
    plot_time_domain(t,signal,low_filtered,"Low-Pass Filtered Signal")
    plot_time_domain(t,signal,high_filtered,"High-Pass Filtered Signal")
    plot_time_domain(t,signal,band_filtered,"Band-Pass Filtered Signal")

    #-------- Plot Frequency Domain -------
    plot_fft(freqs,original_fft,low_fft,"FFT-Low-Pass Filter")
    plot_fft(freqs,original_fft, high_fft, "High-Pass Filtered Signal")
    plot_fft(freqs,original_fft,band_fft,"FFT-Band-Pass Filter")

    return {
        "lowpass":low_filtered,
        "highpass":high_filtered,
        "Bandpass":band_filtered
    }
#========== Example Test(Temporary) ==========
if  __name__ == "__main__":
    fs=500
    t=np.linspace(0,2,fs*2,endpoint=False)

    # Sythetic test signal
    signal=2*np.sin(2*np.pi*5*t)+np.sin(2*np.pi*50*t)+0.5*np.random.randn(len(t))

    analyze_and_filter_signal(t,signal,fs)
