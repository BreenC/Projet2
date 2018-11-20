from src.Turbine import Turbine

class Centrale:
    def __init__(self):
        self.turbines = []
        self.qtot

    def get_turbines(self):
        return self.turbines

    def get_turbine_i(self,i):
        return self.turbines[i]

    def get_qtot(self):
        return self.qtot
