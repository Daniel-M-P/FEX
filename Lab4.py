import pandas
import numpy as np
import matplotlib.pyplot as plt
from math import floor, log10, pi
from scipy.optimize import curve_fit
import uncertainties as unc # .s std deviation, .n nominal value
import uncertainties.umath as umath

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


R = [0.1, 0.15 ,0.2]
F = [0.85, 0.65, 0.55]
CV = [1.335, 1.318, 1.322, 1.329, 1.34]
CN = [1.024, 1.03, 1.03, 1.012, 1.03]

# MASA CV = 0.5432
# MASA CN = 0.5449

Tr = [f*r for f, r in zip(F,R)]
Torque = unc.ufloat(np.mean(Tr), np.std(Tr))
C = Torque/np.pi
cv = unc.ufloat(np.mean(CV), np.std(CV))
cn = unc.ufloat(np.mean(CN), np.std(CN))

I1 = C*umath.pow(cv/(2*np.pi),2)
I2 = C*umath.pow(cn/(2*np.pi),2)

# diff = ((I2.n - I1.n) / I1.n)*100
# print(f"La diferencia porcentual es: {diff:.2f}%")

# m1 = 543.2
# m2 = 544.9

# diff2 = ((m2 - m1)/ m1)*100
# print(f"La diferencia porcentual es: {diff2:.2f}%")


# print(I1)
# print(I2)


Bs = [1.641, 1.644, 1.635, 1.631, 1.634]
As = [1.534, 1.543, 1.537, 1.553, 1.534]
m = unc.ufloat(0.5251, 0.0001)
L = unc.ufloat(1.007, 0.0005) # centro de masa está al medio
A = unc.ufloat(0.161, 0.0005)
B = unc.ufloat(0.011, 0.0005)
TA = unc.ufloat(np.mean(As), np.std(As))
TB = unc.ufloat(np.mean(Bs), np.std(Bs))
g = unc.ufloat(9.794, 0.001)

HA = L/2 - A
HB = L/2 - B

IA = m*g*HA*umath.pow(TA/(2*np.pi),2)
IB = m*g*HB*umath.pow(TB/(2*np.pi),2)

ICM = (m*umath.pow(L,2))/12

SteinerA = ICM + m*umath.pow(HA, 2)
SteinerB = ICM + m*umath.pow(HB, 2)

TA1 = 2*np.pi*umath.sqrt(SteinerA/(m*g*HA))
TB1 = 2*np.pi*umath.sqrt(SteinerB/(m*g*HB))

print(IA, SteinerA)
print(IB, SteinerB)


IA = sig_figs(IA.n, 3)
SteinerA = sig_figs(SteinerA.n, 3)

IB = sig_figs(IB.n, 3)
SteinerB = sig_figs(SteinerB.n, 3)


print(IA, SteinerA)


diff = ((IA - SteinerA) / SteinerA)*100
print(f"La diferencia porcentual es: {diff:.0f}%")

print(IB, SteinerB)

diff2 = ((IB - SteinerB)/ SteinerB)*100
print(f"La diferencia porcentual es: {diff2:.0f}%")

# # 
# 0.12 0.11
# La diferencia porcentual es: 9%
# 0.15 0.17
# La diferencia porcentual es: -12%