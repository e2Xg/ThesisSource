# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

def standard_atmosphere(H, R = 8.31432*10**3, m0 = 28.96442):
    """ Standard atmosphere calculations based on ESDU 77021 """
    data = {
            'Hi' : [0, 11*10**3, 20*10**3, 32*10**3, 47*10**3, 51*10**3, 71*10**3, 80*10**3],
            'Ti' : [288.15, 216.65, 216.65, 228.65, 270.65, 270.65, 214.65, 196.65],
            'Li' : [-6.5*10**-3, 0, 10**-3, 2.8*10**-3, 0, -2.8*10**-3, -2.0*10**-3, np.nan],
            'pi' : [1.01325*10**5, 1.263204*10**4, 5.474879*10**3, 8.68016*10**2, 1.109058*10**2, 6.693853*10, 3.956392, 8.862722*10**-1],
            'gmRLi' : [-5.25588, np.nan, 34.16322, 12.20115, np.nan, -12.20115, -17.08161, np.nan],
            'gmRTi' : [ np.nan, 1.576885*10**-4, np.nan, np.nan, 1.262266*10**-4, np.nan, np.nan, np.nan]
            }
    datatable = pd.DataFrame(data=data)
    #Check Data is Within Limits
    i = None
    for k in range(len(datatable.index)-1):
        Hi = datatable.loc[k,'Hi'].item()
        Hip1 = datatable.loc[k+1,'Hi'].item()
        if Hi <= H and H < Hip1: i = k
    if H < datatable.loc[0,'Hi'].item(): i = 0
    if i == None: return None
    #Get All Items From Table
    switch = False
    Hi = datatable.loc[i,'Hi'].item()
    Ti = datatable.loc[i,'Ti'].item()
    Li = datatable.loc[i,'Li'].item()
    if Li == 0.0: switch = True
    pi = datatable.loc[i,'pi'].item()
    gmRLi = datatable.loc[i,'gmRLi'].item()
    gmRTi = datatable.loc[i,'gmRTi'].item()
    #Eq A2.1
    T = Ti + Li*(H-Hi)
    #Eq A2.2 or A2.3 depending on Li = 0.0 (switch)
    if switch == False: p = ((Ti/T)**gmRLi)*pi
    else: p = (np.exp(gmRTi*(H-Hi)))*pi
    a = np.sqrt(1.4*R*T/m0)
    rho = p*m0/(R*T)
    mu = (1.458*(10**-6)*(T**(3.0/2.0)))/(T+110.4)
    return a, rho, mu

if __name__ == "__main__":
    print(standard_atmosphere(0))