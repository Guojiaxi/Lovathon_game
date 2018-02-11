import globalvars
from math import *

def figure_eight(t):
    a = 10
    return (-a*sin(t), 2*a*cos(2*t))

def circular(t):
    r = 50
    return (round(-r*sin(t)),round(r*cos(t)))