import pandas
import numpy as np
import matplotlib.pyplot as plt
from math import floor, log10, pi
from scipy.optimize import curve_fit
import uncertainties as unc
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


def funcion(x,a,b):
    return a+b*x
# Si los datos son del mismo tipo
def graf_iguales(popt, title, ylabel, datos, x, xlabel="Casos", error = 0, constantes=None, legend=("Datos", "Error")):
    fig, (ax)=plt.subplots(1,1)
    cantidad = len(datos)
    casos = [i for i in range(1, cantidad +1)]
    if error:
        plt.errorbar(casos, datos, yerr=error, fmt='-k',linestyle='',  capsize=4, label='error')
    ax.plot(x,datos,'.b')

    if constantes:
        for i in constantes:
            x = np.linspace(0, cantidad, 100)  # This generates 100 equally spaced points between 0 and 10
            y = np.full_like(x, i[0]) # Create an array of y values, all equal to the constant_value
            plt.plot(x, y, label=i[1], color='red')

    ax.plot(x, funcion(x, 0.018, -0.05730236036995672),'-',label='Ajuste')
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.legend(fontsize = 8, frameon=False)
    plt.title(title)
    plt.show()





archivo =  pandas.read_csv(r'Datos.csv')


m = unc.ufloat(0.1617, 0.0001)
k = unc.ufloat(5.11, 0.07)
t = unc.ufloat(1.1925, 0.00002625)
exp = (k/m) - umath.pow((2*np.pi)/t, 2)
y1 = umath.sqrt(exp)

print(y1)

amplitud = archivo["Amplitud"]
tiempo = archivo["Tiempo"]




# popt,pcov= curve_fit(funcion, tiempo, amplitud)
# yamortiguacion = 0.05730236036995672
# print(popt)
# print(pcov)
# perr = np.sqrt(np.diag(pcov))#standard deviation (sqrt of variance)
# print(perr)

# T = (2*np.pi)/(umath.pow((k/m)-umath.pow(yamortiguacion, 2), 1/2))
# print(T)

# graf_iguales(popt, "Amortiguamiento Débil", "Amplitud (m)", amplitud, tiempo, "Tiempo (s)")

# PA = archivo["A"]
# PB = archivo["B"]

# TA = unc.ufloat(np.mean(PA), np.std(PA))
# TB = unc.ufloat(np.mean(PB), np.std(PB))

# print(TA, TB)

# A = unc.ufloat(0.118, 0.0001)
# B = unc.ufloat(0.2, 0.0001) # falta sumar la masa del resorte

# def coef(t, m):
#     return ((((2*np.pi)**2))/(umath.pow(t,2)))*m

# KA = coef(TA, A)
# KB = coef(TB, B)

# print(sig_figs(KA.n,3), sig_figs(KA.s, 3))
# print(sig_figs(KB.n,1), sig_figs(KB.s, 1))


# data_dict = {"e_momentum":[], "e_energia":[], "e_coeficiente":[]}
# df = pandas.DataFrame(data_dict)
# df_combinado = pandas.concat([datos_velocidades, df], axis=1)
# df_combinado.to_csv("Velocidades.csv", index=False)
