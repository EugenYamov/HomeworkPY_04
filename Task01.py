# Вычислить число π c заданной точностью d
# 1/(2n+1)*(-1)^n
 
from cmath import pi
import pickle

def calculating_pi(d):
    p = 0
    n = 0
    while abs(((1 / (2 * n + 1) * ((-1)**n))*4)) > d:
        p = (p + (1 / (2 * n + 1) * ((-1)**n)))
        n = n + 1
    
    print(p*4)
        
calculating_pi(0.0001)