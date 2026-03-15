[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/M_ou-imR)
# Signal Processing and Filtering Project
Group 3 – Final Project (Python)

This project implements a complete digital signal processing workflow, including
signal generation, preprocessing, FFT analysis, filtering (low-pass, high-pass, band-pass),
and visualization in both time and frequency domains. Real-world biomedical (ECG) and
speech signals are also included for analysis.

------------------------------------------------------------
1. Project Features
------------------------------------------------------------

(1) Synthetic Signal Generation
- Generates sine, cosine, or noise signals
- Adjustable frequency, amplitude, duration, and sampling rate
- Includes time-domain plotting

(2) Signal Preprocessing
- Remove mean (zero-mean)
- Normalize signal to [-1, 1]
- Ensures stable FFT and filtering

(3) FFT Analysis
- Computes single-sided magnitude spectrum
- Visualizes frequency components clearly
- Used for synthetic, ECG, and speech signals

(4) Digital Filtering (Butterworth Filters)
- Low-pass filter (LPF)
- High-pass filter (HPF)
- Band-pass filter (BPF)
- Time-domain and frequency-domain plots for comparison

(5) Real-World Data Processing
- ecg_record100.csv (ECG signal, 360 Hz)
- 0_george_10.csv (speech signal, 8000 Hz)
- FFT + filtering applied to both datasets

------------------------------------------------------------
2. Project File Structure
------------------------------------------------------------

generate_signal.py          → Synthetic signal generator  
preprocess_signal.py        → Mean removal + normalization  
fft_analyzer.py             → FFT computation + plots  
filters.py                  → Digital filters (LPF / HPF / BPF)  
plot.py                     → Time-domain plots & FFT comparison  
signal_analyzer.py          → Main workflow (run this file)  
ecg_record100.csv           → ECG dataset  
0_george_10.csv             → Speech dataset  

README.md                   → Documentation

------------------------------------------------------------
3. How to Run the Project
------------------------------------------------------------

Step 1 — Install dependencies  
pip install numpy scipy matplotlib pandas pyyaml

Step 2 — Put all .py files and CSV files in the same folder

Step 3 — Run the main project  
python Final_Project_Group3.py

This will produce:
- Synthetic signal FFT
- Filtered time-domain and frequency-domain plots
- ECG FFT + filtering
- Speech FFT + filtering

------------------------------------------------------------
4. Key Module Descriptions
------------------------------------------------------------

generate_signal.py
- Creates sine, cosine, or noise signals
- Returns time vector t and signal x

preprocess_signal.py
- Zero-mean processing
- Normalization to [-1, 1]

fft_analyzer.py
- compute_fft(): computes one-sided FFT
- plot_frequency_spectrum(): magnitude spectrum
- compare_frequency_response(): FFT comparison plot

filters.py
- apply_lowpass_filter()
- apply_highpass_filter()
- apply_bandpass_filter()
(All based on Butterworth IIR, using scipy.signal)

plot.py
- Time-domain waveform plotting
- FFT overlay and comparison

signal_analyzer.py
- Generates synthetic signals
- Loads ECG and speech CSV files
- Performs FFT + filtering
- Displays all plots

------------------------------------------------------------
5. Output Description
------------------------------------------------------------

Time-domain waveform:
Shows original and filtered signals.

FFT magnitude spectrum:
Shows peak frequencies (e.g., 50 Hz synthetic).

Filtered FFT results:
LPF removes high-frequency noise,
HPF removes baseline drift,
BPF keeps only desired frequency band.

------------------------------------------------------------
6. Notes
------------------------------------------------------------

- Ensure sampling rate matches dataset:
  ECG = 360 Hz, Speech = 8000 Hz
- Requires SciPy for Butterworth filtering

------------------------------------------------------------
7. Authors
------------------------------------------------------------

Group 3:
Jiaying Li  
Yushi Xin  
Junyi Jin

------------------------------------------------------------
8. License
------------------------------------------------------------

This project is for academic use only under course requirements.
