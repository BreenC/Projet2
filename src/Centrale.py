from src.Turbine import Turbine

class Centrale:
    def __init__(self):
        self.turbines = []
        self.qtot
        self.elamont

    def get_turbines(self):
        return self.turbines

    def get_elamont(self):
        return self.elamont

    def get_turbine_i(self,i):
        return self.turbines[i]

    def get_qtot(self):
        return self.qtot

    def discretidation(self, val):
        if val%5 < 2.5 :
            val = val + val%5
        else :
            val = val - val%5
        return val