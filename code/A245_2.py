#!usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: smilex
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, h, k):
    return(a*np.sinc(x - h) + k)

def redchi2(f, x, y, y_err, *args):
    sum = 0
    for i in range(len(x)):
        sum += np.square((f(x[i], *args) - y[i])/(y_err[i]))
    dof = len(y) - len(args)
    rc2 = sum/dof
    return rc2

data = np.genfromtxt('data.csv', delimiter = ',')
x_data = data[1:, 0]
y_data = data[1:, 2]
x_data_err = data[1:, 1]
y_data_err = data[1:, 3]

x_model = np.arange(min(x_data), max(x_data), 0.1)

k = y_data.argmax()
p0 = [y_data[k], x_data[k], y_data.mean()]
popt, pcov = curve_fit(func, x_data, y_data, p0=p0)

print(popt)
print(np.sqrt(np.diag(pcov)))

plt.errorbar(x_data, y_data, xerr = x_data_err, yerr = y_data_err, fmt = '.', capsize = 4, label = 'data')
plt.plot(x_model, func(x_model, *popt), color = 'red', label = 'fit')
plt.xlabel('Crystal Temperature - T($^\\circ$C)')
plt.ylabel('Second Harmonic Power - $P_{SH, unatt.}$($\\mu W$)')
plt.legend(loc = 'upper left')
plt.savefig('shpowvstemp.png', dpi = 1200)
plt.show()

print(redchi2(func, x_data, y_data, x_data_err, *popt))