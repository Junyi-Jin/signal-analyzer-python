from scipy.signal import butter, filtfilt
def apply_lowpass_filter(signal,cutoff,fs,order=4):
    nyquist=0.5*fs
    norm_cut=cutoff/nyquist
    b,a=butter(order,norm_cut,btype='low')
    return filtfilt(b,a,signal)

def apply_highpass_filter(signal,cutoff,fs,order=4):
    nyquist=0.5*fs
    norm_cut=cutoff/nyquist
    b,a=butter(order,norm_cut,btype='high')
    return filtfilt(b,a,signal)

def apply_bandpass_filter(signal,lowcut,highcut,fs,order=4):
    nyquist=0.5*fs
    low=lowcut/nyquist
    high=highcut/nyquist
    b,a=butter(order,[low,high],btype='band')
    return filtfilt(b,a,signal)
    