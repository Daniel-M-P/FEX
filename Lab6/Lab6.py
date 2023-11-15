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



### Trayectoria Parabólica
# archivo = pandas.read_csv(r"Datos.csv")
# x = archivo["x"]
# y = archivo["y"]

# h1 = 0.115
# y0 = 0.16
# Vx = 2*g.n*h1


# def alturas(x):
#      return y0 - 0.5*(g.n/Vx)*(x)**2

# x_vals = np.linspace(0, 0.195, 1000)
# y_vals = alturas(x_vals)

### Ondas gravitacionales

archivo = pandas.read_csv(r"Arriba.csv")
x = archivo["x"]
y = archivo["y"]

you = 0.49
w = np.sqrt(2*np.pi*g.n/you)
Vph = np.sqrt((g.n*you)/(2*np.pi))
r = 0.01

def pos_x(t):
    return r * (w * t - np.sin(w * t)) + Vph * t -0.3

def pos_y(t):
    return r * np.cos(w * t)


tiempo = np.linspace(0.3, 0.8, 1000)

x_vals = pos_x(tiempo)
y_vals = pos_y(tiempo)

plt.plot(x, y, label="Experimental", linestyle="-")
plt.plot(x_vals, y_vals, label="Teórica", linestyle="-")
plt.xlabel("Largo (m)")
plt.ylabel("Altura (m)")
plt.legend(frameon=False)
plt.title("Curva teórica vs experimental de ondas gravitacionales")
plt.savefig("Gravitacional.png", dpi=300, bbox_inches='tight')
plt.show()
