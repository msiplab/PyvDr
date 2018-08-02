import numpy as np
class PolyPhaseMatrix1d():
    """Poly-Phase Matrix in 1D
    """

    def __init__(self,coefs=[]):
        """Constructure"""
        if isinstance(coefs,PolyPhaseMatrix1d):
            self.__coefs = coefs.coefs
        else:
            self.__coefs = coefs

    def __str__(self):
        """To String"""
        nRowsPhs = self.__coefs.shape[0]
        nColsPhs = self.__coefs.shape[1]
        print(nRowsPhs)
        print(nColsPhs)
        value = '[\n'
        for iRow in range(nRowsPhs):
            for iCol in range(nColsPhs):
                value += str(self.__coefs[iRow][iCol])
        value += '\n]'
        return value

    @property
    def coefs(self):
        return self.__coefs
