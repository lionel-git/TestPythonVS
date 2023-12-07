
import decimal
import matplotlib
import pylab
import numpy as np

from TestMandel import *


print ("Hello world")
print("plotlib infos: ", matplotlib.__version__, matplotlib.__file__)

def check_plot_lib():
    #from pylab import *;
    #pylab.set_loglevel('debug')
    x = np.arange(0,4*np.pi,0.1)   # start,stop,step
    y = np.sin(x)


    pylab.plot(x, y)
    pylab.show()
    return

def main():
    x = 17
    print (add_one(x))
    print (Myiter(complex(1,1)))
    check_plot_lib()
    
if __name__ == "__main__":
    main()
