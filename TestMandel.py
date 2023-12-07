
import decimal
import matplotlib
import pylab
import numpy as np
import cmath

def add_one(a):
    return a+1

def toto():
    return

def modulus(c):
    return c.real*c.real+c.imag*c.imag

def Myiter(c0):
    z=complex(0,0)
    z=z*z+c0
    z=z*z+c0
    return modulus(z)>5
