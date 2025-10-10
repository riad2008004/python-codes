import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, filtfilt, freqz

# Sampling parameters
fs = 500           # Sampling frequency in Hz
T = 5              # Duration in seconds
t = np.linspace(0, T, int(T*fs), endpoint=False)

# Simulate ECG-like signal (simplified sum of sinusoids)
ecg_signal = 0.6*np.sin(2*np.pi*1.0*t) + 1.0*np.sin(2*np.pi*1.33*t) + 0.4*np.sin(2*np.pi*1.66*t)

# Add noise: baseline wander + powerline + high-frequency Gaussian noise
baseline_wander = 0.5 * np.sin(2*np.pi*0.5*t)
powerline_noise = 0.2 * np.sin(2*np.pi*50*t)
np.random.seed(0)
gaussian_noise = 0.3 * np.random.randn(len(t))

noisy_ecg = ecg_signal + baseline_wander + powerline_noise + gaussian_noise

# Design Hamming window FIR band-pass filter (0.5-40 Hz)
numtaps = 101
low_cutoff = 0.5
high_cutoff = 40
fir_coeff = firwin(numtaps, [low_cutoff, high_cutoff], pass_zero=False, fs=fs, window='hamming')

# Frequency response
w, h = freqz(fir_coeff, worN=8000)
freqs = w * fs / (2 * np.pi)

# Apply filter (zero-phase)
filtered_ecg = filtfilt(fir_coeff, [1.0], noisy_ecg)

# Plot results
plt.figure(figsize=(12, 12))

plt.subplot(5, 1, 1)
plt.plot(t, ecg_signal)
plt.title("Original ECG Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.subplot(5, 1, 2)
plt.plot(t, gaussian_noise, color='orange')
plt.title("High-Frequency Gaussian Noise")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.subplot(5, 1, 3)
plt.plot(t, noisy_ecg)
plt.title("Noisy ECG Signal (Baseline Wander + Powerline + Gaussian Noise)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.subplot(5, 1, 4)
plt.plot(t, filtered_ecg)
plt.title("Filtered ECG Signal using Hamming FIR Band-Pass Filter")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.subplot(5, 1, 5)
plt.plot(freqs, 20*np.log10(np.abs(h)))
plt.title("Hamming Filter Frequency Response")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Gain [dB]")
plt.xlim(0, fs/2)
plt.grid(True)

plt.tight_layout()
plt.show()
