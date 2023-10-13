import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
from math import floor, log10, pi

def sig_figs(x: float, precision: int):
    """
    Rounds a number to number of significant figures
    Parameters:
    - x - the number to be rounded
    - precision (integer) - the number of significant figures
    Returns:
    - float
    code from https://mattgosden.medium.com/rounding-to-significant-figures-in-python-2415661b94c3
    """

    x = float(x)
    precision = int(precision)

    return round(x, -int(floor(log10(abs(x)))) + (precision - 1))

amplitudes_maximas = np.array([0.018, 0.017, 0.015, 0.015, 0.015, 0.014, 0.014, 0.013, 0.013, 0.013,
                               0.012, 0.011, 0.011, 0.010, 0.010, 0.009, 0.009, 0.008, 0.008, 0.008,
                               0.007, 0.007, 0.007, 0.006, 0.006, 0.005, 0.005, 0.005, 0.004, 0.004,
                               0.004, 0.003, 0.003, 0.003, 0.002, 0.002, 0.002, 0.001, 0.001, 0.001, 0.001])

tiempos = np.array([0, 1.4, 2.66, 3.76, 5.06, 6.26, 7.4, 8.66, 9.86, 11.06, 12.26, 13.4, 14.56,
                    15.76, 16.96, 18, 18.86, 20.5, 21.76, 22.88, 24.06, 25.2, 26.5, 27.6, 28.84,
                    30, 31.26, 32.4, 33.5, 34.76, 35.96, 37.2, 38.26, 39.47, 40.66, 41.66, 43.06,
                    44.26, 45.26, 46.56, 47.7])

A = amplitudes_maximas[0]
ln_ratio = np.log(amplitudes_maximas / A)
slope, intercept, r_value, p_value, std_err = linregress(tiempos, ln_ratio)
gamma = sig_figs(slope, 2)
error = sig_figs(std_err, 1)

print(f"Factor de amortiguamiento (gamma): {gamma} +/- {error}")

tiempos_regresion = np.linspace(min(tiempos), max(tiempos), 100)
tiempos_regresion2 = np.linspace(min(tiempos), 1.6, 100)
ln_ratio_regresion = gamma * tiempos_regresion + intercept
ln_ratio_regresion2 = -1.96 * tiempos_regresion2 + intercept


plt.scatter(tiempos, ln_ratio, label="Datos", s=50, c='blue', marker='o')
plt.plot(tiempos_regresion2, ln_ratio_regresion2, color='green', label="Modelo 1")
plt.plot(tiempos_regresion, ln_ratio_regresion, color='red', label="Modelo 2")


plt.xlabel("Tiempo (s)")
plt.ylabel("ln(xn/A)")
plt.legend()
plt.title("Pendientes del factor de amortiguamiento")


plt.show()
