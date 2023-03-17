from math import radians
import numpy as np # installed with matplotlib
import matplotlib.pyplot as plt

def main():
    x = np.arange(0, radians(1000), radians(10))
    plt.plot(x, np.cos(x), 'b')
    
    xpoints = np.array([10, .5])
    ypoints = np.array([0, .75])

    plt.plot(xpoints, ypoints)
    plt.show()

main()
