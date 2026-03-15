import numpy as np

def preprocess_signal(
    x: np.ndarray,
    remove_mean: bool = True,
    normalize: bool = True,
) -> np.ndarray:
    """
    Basic preprocessing for a 1-D signal.

    Operations
    ----------
    1) Remove mean (zero-mean).
    2) Normalize to [-1, 1] based on max absolute value.

    Parameters
    ----------
    x : np.ndarray
        Input 1-D signal.
    remove_mean : bool, optional
        If True, subtract the mean from the signal.
    normalize : bool, optional
        If True, divide by the max absolute value.

    Returns
    -------
    x_out : np.ndarray
        Preprocessed signal.
    """
    x_out = np.asarray(x, dtype=float)

    if remove_mean:
        x_out = x_out - np.mean(x_out)

    if normalize:
        max_abs = np.max(np.abs(x_out))
        if max_abs > 0:
            x_out = x_out / max_abs

    return x_out

