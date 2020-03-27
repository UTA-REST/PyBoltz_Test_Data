import numpy as np
import os


def getData():
     gd = np.load(os.path.join(os.path.dirname(os.path.realpath(__file__)),"Tests.npy")).item()
     return gd