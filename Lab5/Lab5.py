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


## Escribir esto como una clase, ir añadiendo cada caso como una función.

# Si los datos son del mismo tipo
def graf_iguales(title, ylabel, datos, error = 0, constantes=None, legend=("Datos", "Error"), xlabel="Casos"):
    fig, (ax)=plt.subplots(1,1)
    cantidad = len(datos)
    casos = [i for i in range(1, cantidad +1)]
    if error:
        plt.errorbar(casos, datos, yerr=error, fmt='-k',linestyle='',  capsize=4, label='error')
    ax.plot(casos,datos,'.b', label= label)

    if constantes:
        for i in constantes:
            x = np.linspace(0, cantidad, 100)  # This generates 100 equally spaced points between 0 and 10
            y = np.full_like(x, i[0]) # Create an array of y values, all equal to the constant_value
            plt.plot(x, y, label=i[1], color='red')

    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.legend(fontsize = 8, frameon=False)
    plt.title(title)
    plt.show()


def graf_iguales(title, ylabel, datos, error = 0, constantes=None, legend=("Datos", "Error"), xlabel="Casos"):
    fig, (ax)=plt.subplots(1,1)
    cantidad = len(datos)
    casos = [i for i in range(1, cantidad +1)]
    if error:
        plt.errorbar(casos, datos, yerr=error, fmt='-k',linestyle='',  capsize=4, label='error')
    ax.plot(casos,datos,'.b', label= label)

    if constantes:
        for i in constantes:
            x = np.linspace(0, cantidad, 100)  # This generates 100 equally spaced points between 0 and 10
            y = np.full_like(x, i[0]) # Create an array of y values, all equal to the constant_value
            plt.plot(x, y, label=i[1], color='red')

    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.legend(fontsize = 8, frameon=False)
    plt.title(title)
    plt.show()



# Si los datos son de distintos tipos de casos pero 
def graf_distintos(title, ylabel, datos_x_tipo, errores = 0, constantes=None, legend=("Datos", "Error"), xlabel="Casos"):
    fig, (ax)=plt.subplots(1,1)
    cantidad = len(datos)
    colores = ("r","g","b")
    total_casos = sum([len(dato) for dato in datos_x_tipo])
    casos = [i for i in range(1, total_casos+1)]


    # escribir algo para los colores y los labels
    comienzo = 0
    for dato, error in zip(datos_x_caso, errores):
        tope = len(dato)-1 + comienzo
        ax.plot(casos[comienzo:tope], dato, f'.{color}', label=f"{label_tipo}")
        plt.errorbar(casos[comienzo:tope], dato, yerr= error, fmt=f'-{color}',linestyle='',  capsize=4)
        comienzo = tope


    if constantes:
        for i in constantes:
            x = np.linspace(1, cantidad, 100)  # This generates 100 equally spaced points between 0 and 10
            y = np.full_like(x, i[0]) # Create an array of y values, all equal to the constant_value
            plt.plot(x, y, label=i[1], color='k')

    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.legend(fontsize = 8, frameon=False)
    plt.title(title)
    plt.show()


# Gravedad San Joaquin
g = unc.ufloat(9.794, 0.001)

d = unc.ufloat(0.0127, 0.00005)
I = np.pi*umath.pow(d,4)/64
m = [0.4989, 0.9989, 1.4989, 1.9983, 2.4997]




L1 = unc.ufloat(0.358, 0.0005)
w1 = [0.000015, 0.000035, 0.000055, 0.000075, 0.000095]

L2 = unc.ufloat(0.404, 0.0005)
w2 = [0.00002, 0.00006, 0.000085, 0.00011, 0.00014]

L3 = unc.ufloat(0.4365, 0.001)
w3 = [0.00003, 0.000059, 0.000085, 0.00012, 0.000155]


def funcion(x,a,b):
    return a + b*x

Elasticos = []

def graficar_pendientes(L, W, nombre):
    popt,pcov= curve_fit(funcion, m, W)
    perr = np.sqrt(np.diag(pcov))#standard deviation (sqrt of variance)

    p = unc.ufloat(popt[1], perr[1])
    print(p)

    E = g*L**3/(48*p*I)
    Elasticos.append(E)

    x = np.linspace(min(m), max(m), 100)
    y = popt[1]*x + popt[0]

    plt.scatter(m, W, label=nombre, s=50, marker='o')
    plt.plot(x, y, '-')


graficar_pendientes(L1, w1, "L1 (0.358 +- 0.0005 m)")
graficar_pendientes(L2, w2, "L2 (0.404 +- 0.0005 m)")
graficar_pendientes(L3, w3, "L3 (0.4365 +- 0.001 m)")

Errores = [i.s for i in Elasticos]

promedio = np.mean([i.n for i in Elasticos])*10**-9
incertidumbre_del_promedio = np.std(Errores, ddof=1) / np.sqrt(len(Errores))*10**-9

print(f"Promedio: {sig_figs(promedio,3)}")
print(f"Incertidumbre del promedio: {sig_figs(incertidumbre_del_promedio,3)}")


plt.xlabel("Masas (kg)")
plt.ylabel("Flexión máxima (m)")
plt.title("Regresión lineal por largo")
plt.legend(frameon=False)
# plt.savefig("Pendientes.png", dpi=300, bbox_inches='tight')
plt.show()

