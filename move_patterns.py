import globalvars,random
from math import *

def figure_eight(t):
    a = 5
    return (-a*sin(t/20), 2*a*cos(2*t/20))

def circular(t):
    r = 5
    return (-r*sin(t/20),r*cos(t/20))