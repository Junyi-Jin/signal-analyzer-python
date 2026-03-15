import os
from typing import Tuple, Optional
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generate_signal(
    signal_type: str,
    duration: float,
    fs: float,
    freq: float = 1.0,
    amplitude: float = 1.0,
    phase: float = 0.0,
    noise_std: float = 1.0,
    random_seed: Optional[int] = None,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate a synthetic signal.

    Parameters
    ----------
    signal_type : str
        Type of signal: "sine", "cosine", or "noise".
    duration : float
        Signal duration in seconds.
    fs : float
        Sampling frequency in Hz.
    freq : float, optional
        Fundamental frequency of sine/cosine in Hz. Ignored for "noise".
    amplitude : float, optional
        Amplitude of the signal.
    phase : float, optional
        Phase of sine/cosine in radians.
    noise_std : float, optional
        Standard deviation of the noise (for "noise" type).
    random_seed : int, optional
        Random seed for reproducibility (for "noise" type).

    Returns
    -------
    t : np.ndarray
        Time vector (seconds).
    x : np.ndarray
        Generated signal samples.
    """
    # Create time vector from 0 to duration with step 1/fs
    t = np.arange(0, duration, 1.0 / fs)

    signal_type = signal_type.lower()

    if signal_type == "sine":
        x = amplitude * np.sin(2 * np.pi * freq * t + phase)
    elif signal_type == "cosine":
        x = amplitude * np.cos(2 * np.pi * freq * t + phase)
    elif signal_type == "noise":
        if random_seed is not None:
            np.random.seed(random_seed)
        x = amplitude * np.random.normal(loc=0.0, scale=noise_std, size=t.shape)
    else:
        raise ValueError(
            f"Unsupported signal_type '{signal_type}'. "
            f"Use 'sine', 'cosine', or 'noise'."
        )

    return t, x


def plot_time_domain(
    t: np.ndarray,
    x: np.ndarray,
    title: str = "Time-Domain Signal",
    xlabel: str = "Time (s)",
    ylabel: str = "Amplitude",
    show: bool = True,
    save_path: Optional[str] = None,
) -> None:
    """
    Plot a time-domain waveform.

    Parameters
    ----------
    t : np.ndarray
        Time vector.
    x : np.ndarray
        Signal samples.
    title : str, optional
        Plot title.
    xlabel : str, optional
        Label for x-axis.
    ylabel : str, optional
        Label for y-axis.
    show : bool, optional
        If True, call plt.show().
    save_path : str, optional
        If not None, save the figure to this path.
    """
    plt.figure()
    plt.plot(t, x)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()

    if save_path is not None:
        plt.savefig(save_path, dpi=300)

    if show:
        plt.show()


if __name__ == "__main__":
    # Generate a sine wave and plot it
    fs = 1000.0  # Hz
    duration = 1.0  # seconds
    freq = 5.0  # Hz

    t_sine, x_sine = generate_signal(
        signal_type="sine",
        duration=duration,
        fs=fs,
        freq=freq,
        amplitude=1.0,
        phase=0.0,
    )
    plot_time_domain(t_sine, x_sine, title="Synthetic Sine Wave")
