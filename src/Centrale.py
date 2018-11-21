from src.Turbine import Turbine

class Centrale:
    def __init__(self):
        self.turbines = []
        self.qtot
        self.elamont
        self.elav
        self.deverse = 0

    def get_turbines(self):
        return self.turbines

    def get_elamont(self):
        return self.elamont

    def get_turbine_i(self,i):
        return self.turbines[i]

    def get_qtot(self):
        return self.qtot

    def discretidation(self, val):
        if val%5 > 2.5 :
            val = val + val%5
        else :
            val = val - val%5
        return val

    def calcul_elva(self):
        i = 1
        while i <= 200:
            tampon = - 7.014 * 10^{-7} * self.qtot * self.qtot + 0.004107 * self.qtot + 137.2
            i = i + 1
            self.elav.append(tampon)

    def calc(self):
        for turbine in self.turbines :
            if turbine.is_disponible == False :
                turbine.debit_turbine = 0
            else :
                turbine.debit_turbine = max(turbine.debits)

    def calcul_deverse(self):
        self.deverse = self.turbines[5].debit_rest - self.turbines[5].debit_turbine
        return  self.deverse