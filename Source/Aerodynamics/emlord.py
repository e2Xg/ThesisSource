import numpy as np

def emlord(x,S):
    """ Returns D/q (m**2) value of given x (m), S (m**2) distribution 
        Reference: 
            E. Eminton and W. T. Lord - 1956
            Note on the Numerical Evaluation of the Wave Drag of Smooth Slender Bodies Using Optimum Area Distribution for Minimum Wave Drag
    """
    #Transformation Function
    N = S[0]
    B = S[-1]
    n = len(x)
    l = abs(max(x)-min(x))
    if n-2 > 0:
        p = np.zeros((n-2,n-2))
        for i in range(n-2):
            for j in range(0,n-2):
                ki = (i+1)/(n-1)
                kj = (j+1)/(n-1)
                C0 = (ki-kj)**2
                C1 = ki+kj-2.0*ki*kj
                C2 = 2.0*np.sqrt(ki*kj*(1.0-ki)*(1.0-kj))
                if i == j: p[i][j] = C1*C2
                else: p[i][j] = -(1.0/2.0)*C0*np.log((C1+C2)/(C1-C2)) + C1*C2
        f = np.linalg.inv(p)
        sum = 0.0
        for i in range(1,n-1):
            for j in range(1,n-1):
                ki = i/(n-1)
                kj = j/(n-1)
                ui = (1.0/np.pi) * ( np.arccos(1.0-2.0*ki) - 2.0*(1.0 - 2.0*ki) * np.sqrt(ki*(1.0-ki)))
                uj = (1.0/np.pi) * ( np.arccos(1.0-2.0*kj) - 2.0*(1.0 - 2.0*kj) * np.sqrt(kj*(1.0-kj)))
                ci = S[i]-N-(B-N)*ui
                cj = S[j]-N-(B-N)*uj
                sum += ci*cj*f[i-1][j-1]
    else: sum = 0.0
    I = (4.0/np.pi)*((B-N)**2) + np.pi*sum
    return I/(l**2)

if __name__ == "__main__":
    x = np.linspace(0.0,40.0,21)
    l = abs(max(x)-min(x))
    xi = x/l
    S = 10.0*(xi**2)*(400.0*(xi**4)-1176.0*(xi**3)+1257.0*(xi**2)-588.0*xi+108.0)
#    from matplotlib import pyplot as plt
#    plt.figure()
#    plt.plot(x,S,'o')
#    plt.savefig("emlord.png")
    d_on_q = emlord(x,S)
    print("Analytical D/q: ", (1.0/(np.pi*(l**2))*(40200)) )
    print("Emlord I: ",d_on_q)
