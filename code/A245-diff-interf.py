#!usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: smilex
"""

import numpy as np

#data - non-zero order diffraction
fun = np.array([137.8])
sh = np.array([66., 137.8, 246.4])

#distance of the screen
w = 173.
#constant delta for all length measurements
delta_len = 0.5

#constants for the set-up
d = 1/600E3
alpha = np.pi/4

#extract order from the data
ord_fun = np.where(np.full(len(fun), True))[0] + 1
ord_sh = np.where(np.full(len(sh), True))[0] + 1

#calculate wavelength
theta_fun = np.arctan(fun/w)
theta_sh = np.arctan(sh/w)

beta_fun = np.pi/2 - alpha - theta_fun
beta_sh = np.pi/2 - alpha - theta_sh

s_fun = np.sin(alpha) - np.sin(beta_fun)
s_sh = np.sin(alpha) - np.sin(beta_sh)

wlength_fun = s_fun*d / ord_fun
wlength_sh = s_sh * d / ord_sh

#delta wavelength calculations
delta_theta_fun = (1/(fun**2 + w**2)) * np.sqrt((fun*delta_len)**2 + (w*delta_len)**2)
delta_wlength_fun = np.cos(np.pi/4 - theta_fun) * delta_theta_fun * d / ord_fun

delta_theta_sh = (1/(sh**2 + w**2)) * np.sqrt((sh*delta_len)**2 + (w*delta_len)**2)
delta_wlength_sh = np.cos(np.pi/4 - theta_sh) * delta_theta_sh * d / ord_sh

#mean wavelength for second harmonic
wlength_sh_mean = np.average(wlength_sh, weights = 1/delta_wlength_sh**2)
delta_wlength_sh_mean = np.sqrt(1/np.average(1/delta_wlength_sh)**2)

#ratio
wlength_ratio = wlength_fun/wlength_sh_mean
delta_wlength_ratio = np.sqrt((delta_wlength_fun/wlength_sh_mean)**2 + (wlength_fun * delta_wlength_sh_mean / wlength_sh_mean)**2)

#resolution
res_fun = wlength_fun/delta_wlength_fun
res_sh = wlength_sh/delta_wlength_sh

#print results
print("Fundamental Harmonic:\n", wlength_fun, "+-", delta_wlength_fun)
print("Second Harmonic:\n", wlength_sh, "+-", delta_wlength_sh)
print("Second Harmonic Mean:\n", wlength_sh_mean, "+-", delta_wlength_sh_mean)
print("Ratio:\n", wlength_ratio, "+-", delta_wlength_ratio)
print("Resolution - FH:", res_fun)
print("Resolution - SH:", res_sh)