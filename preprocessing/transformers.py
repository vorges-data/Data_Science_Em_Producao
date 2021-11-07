import numpy as np



def sin(x, period):
    return np.sin(x * (2 * np.pi/period))

def cos(x, period):
    return np.cos(x * (2 * np.pi/period))