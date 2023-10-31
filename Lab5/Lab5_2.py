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

def function(m, L, E, I, x):
    return ((m*g.n*L**3)/(24*E*I))*((x/L)**4 - 4*(x/L)**3 + 6*(x/L)**2)

Lg = unc.ufloat(0.886, 0.0005)
Altura_g = unc.ufloat(0.0035, 0.00005)
Base_g = unc.ufloat(0.0205, 0.00005)
mg = unc.ufloat(0.1617, 0.0001)
hg = 0.037
E_aluminio = 38.2*(10**9)
Ig = Base_g*umath.pow(Altura_g, 3)/12
xg = [i*10**-2 + 0.006 for i in range(1, 81)]

wg = [-function(mg.n, Lg.n, E_aluminio, Ig.n, i) for i in xg]
E1 = (mg*g*Lg**3)/(8*Ig*hg)



archivo = pandas.read_csv(r"Gris.csv")
x1 = archivo["x"]
y1 = archivo["y"]


plt.plot(x1, y1, label="Experimental", color="gray", linestyle="-")
plt.plot(xg, wg, label="Teórica", color="blue")
plt.xlabel("Largo (m)")
plt.ylabel("Flexión (m)")
plt.legend(frameon=False)
plt.title("Curva teórica vs experimental barra gris")
# plt.savefig("Gris.png", dpi=300, bbox_inches='tight')
# plt.show()





Ld = unc.ufloat(0.807, 0.0005)
Altura_d = unc.ufloat(0.003, 0.00005)
Base_d = unc.ufloat(0.02025, 0.00005)
md = unc.ufloat(0.5251, 0.00001)
hd = 0.04
E_cobre = 185*(10**9)
Id = Base_d*umath.pow(Altura_d, 3)/12
xd = [i*10**-2 + 0.007 for i in range(1, 81)]

wd = [-function(md.n, Ld.n, E_cobre, Id.n, i) for i in xd]
E = md*g*Ld**3/(8*Id*hd)



archivo = pandas.read_csv(r"Dorado.csv")
x = archivo["x"]
y = archivo["y"]

color_dorado = (222/255, 182/255, 38/255)



plt.plot(x, y, label="Experimental", color=color_dorado, linestyle="-")
plt.plot(xd, wd, label="Teórica", color="blue")
plt.xlabel("Largo (m)")
plt.ylabel("Flexión (m)")
plt.legend(frameon=False)
plt.title("Curva teórica vs experimental barra dorada")
# plt.savefig("Dorado.png", dpi=300, bbox_inches='tight')
# plt.show()

print(E)
print(E1)








