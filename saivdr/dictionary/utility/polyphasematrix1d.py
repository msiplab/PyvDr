class PolyPhaseMatrix1d():
    """Poly-Phase Matrix in 1D
    """
    
    def __init__(self,coefs=[]):
        self.__coefs = coefs

    @property
    def coefs(self):
        return self.__coefs
