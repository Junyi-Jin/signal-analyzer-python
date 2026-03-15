# ============================================================
# Imports
# ============================================================
import numpy as np
import matplotlib.pyplot as plt
import yaml

from generate_signal import generate_signal
from preprocess_signal import preprocess_signal

from fft_analyzer import compute_fft, plot_frequency_spectrum, compare_frequency_response

from filters import apply_lowpass_filter,apply_highpass_filter,apply_bandpass_filter
from plot import plot_time_domain,plot_fft

# ============================================================
# TODO 1 — Create Your Classes
# ============================================================
class ExampleModel:
    """
    Small helper class to load project settings from a YAML file.
    """

    def __init__(self, filename=None):
        # meta will store everything loaded from the YAML file
        self.meta = None

        if filename is not None:
            self.load_metadata(filename)

    def load_metadata(self, filename):
        """
        Load configuration from <filename>.yaml and store it in self.meta.
        """
        with open(filename + ".yaml", "r") as f:
            self.meta = yaml.safe_load(f)
        return self.meta

    # The methods below just return different parts of the config.
    # If a section is missing in the YAML, we fall back to an empty dict.
    def get_synthetic_params(self):
        return (self.meta or {}).get("synthetic_signal", {})

    def get_ecg_params(self):
        return (self.meta or {}).get("ecg_signal", {})

    def get_noise_params(self):
        return (self.meta or {}).get("urban_noise", {})

    def get_filter_params(self):
        return (self.meta or {}).get("filters", {})



# ============================================================
# TODO 2 — Add Your Functions
# ============================================================
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


# ============================================================
# TODO 3 — Main Project Workflow
# ============================================================

def run_project():
    print("Running Final Project...")

    # Load configuration from YAML ("project_config.yaml" in this folder)
    model = ExampleModel("project_config")
    syn_cfg = model.get_synthetic_params()

    # Read basic settings for the synthetic sine signal
    duration = syn_cfg.get("duration", 2.0)
    fs_syn   = syn_cfg.get("fs", 500)
    freq     = syn_cfg.get("freq", 50)
    amplitude = syn_cfg.get("amplitude", 1.0)
    phase     = syn_cfg.get("phase", 0.0)
    noise_std = syn_cfg.get("noise_std", 0.3)

    print("Synthetic signal settings from YAML:", syn_cfg)

    # Generate synthetic sine wave
    print("Generating synthetic sine signal...")
    t_syn, x_syn = generate_signal(
        signal_type="sine",
        duration=duration,
        fs=fs_syn,
        freq=freq,
        amplitude=amplitude,
        phase=phase
    )

    # Optionally add white noise to the signal
    if noise_std > 0:
        noise = np.random.normal(0, noise_std, len(x_syn))
        x_syn = x_syn + noise


    # ------- FFT of synthetic signal -------
    print("Computing FFT for synthetic signal...")
    freqs_syn, mag_syn = compute_fft(x_syn, fs=fs_syn)
    plot_frequency_spectrum(freqs_syn, mag_syn, "FFT of Synthetic Signal")

    # ------ Filtering synthetic signal (LPF, HPF, BPF) --------
    print("Filtering synthetic signal...")
    analyze_and_filter_signal(t_syn, x_syn, fs=fs_syn)


# ------- Load ECG signal from CSV -------
    print("Loading ECG signal...")
    import pandas as pd
    ecg_df = pd.read_csv("ecg_record100.csv")
# Extract time and amplitude columns
    t_ecg = ecg_df["time(s)"].values
    x_ecg = ecg_df["ecg(mV)"].values
#--------- Add baseline drift (low-frequency noise)
    drift= 0.3*np.sin(2*np.pi*0.2*t_ecg) #0.2Hz drift
    x_ecg=x_ecg + drift
# ------- FFT of ECG signal --------
    print("Computing FFT for ECG signal...")
    freqs_ecg, mag_ecg = compute_fft(x_ecg, fs=360)  # MIT-BIH sampling rate ~360Hz
    plot_frequency_spectrum(freqs_ecg, mag_ecg,
                            title="FFT of ECG Signal")
# -------- Filtering ECG signal
    print("Filtering ECG signal...")
    analyze_and_filter_signal(t_ecg, x_ecg, fs=360)

# -------- Load Urban Noise Signal ----------
    print("Loading Urban Noise Signal...")
    import librosa
# Load one .wav noise file
    x_noise, fs_noise = librosa.load("urban_sound_data_14113-4-0-0.wav", sr=None)
# Create time axis
    t_noise = np.arange(len(x_noise)) / fs_noise
# -------- FFT of Urban Noise Signal --------
    print("Computing FFT for Urban Noise Signal...")
    freqs_noise, mag_noise = compute_fft(x_noise, fs=fs_noise)
    plot_frequency_spectrum(
    freqs_noise, mag_noise,
    title="FFT of Urban Noise Signal"
    )

# -------- Filtering noise signal --------
    print("Filtering Urban Noise Signal...")
    analyze_and_filter_signal(t_noise, x_noise, fs_noise)



#================================================================
    print("Final Project Completed!")

    # Example of using a class:
    # model = ExampleModel("data/config")
    # print(model.meta)

    # TODO:
    # - Load data
    # - Process data
    # - Perform analysis (FFT, curve fitting, etc.)
    # - Generate plots and save them to results/
    # - Print or save summary outputs


# ============================================================
# Entry Point
# ============================================================
if __name__ == "__main__":
    run_project()