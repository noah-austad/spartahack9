import math
from scipy.stats import norm

def blackscholes(callput, S, K, T=.25, r=0.05, sigma=.2):
    S=float(S)
    K=float(K)
    d1 = (math.log(S/K) + (r + sigma**2/2)*T) / (sigma*math.sqrt(T))
    d2 = d1 - sigma*math.sqrt(T)
    if callput == 'call':
        return S*norm.cdf(d1) - K*math.exp(-r*T)*norm.cdf(d2)
    elif callput == 'put':
        return K*math.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)
def bullspread(e1,e2,S):
    cost_e1=blackscholes('call',S,e1)
    cost_e2=blackscholes('call',S,e2)
    return round(cost_e2-cost_e1,2)
def bearspread(e1,e2,S):
    cost_e1=blackscholes('put',S,e1)
    cost_e2=blackscholes('put',S,e2)
    return round(cost_e1-cost_e2,2)
def butterflyspread(e1,e2,S):
    e1=float(e1)
    e2=float(e2)
    e3=(e1+e2)/2
    cost_e1=blackscholes('call',S,e1)
    cost_e2=blackscholes('call',S,e2)
    cost_e3=blackscholes('call',S,e3)
    return round(2*cost_e3-cost_e1-cost_e2,2)
