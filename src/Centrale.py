class Centrale:
    def __init__(self):
        self.turbines = []
        self.qtot = []
        self.elamont = []
        self.elav = []
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
        while i < 200:
            tampon = - 7.014 * 10**(-7) * self.qtot[i] * self.qtot[i] + 0.004107 * self.qtot[i] + 137.2
            i = i + 1
            self.elav.append(tampon)

    def calc(self):
        for turbine in self.turbines :
            if turbine.is_disponible == False :
                turbine.debit_turbine = 0
            else :
                turbine.debit_turbine = max(turbine.debits)

    def calcul_deverse(self):
        self.deverse = self.turbines[4].debit_rest - self.turbines[4].debit_turbine
        return  self.deverse

    def run(self):
        self.calcul_elva()
        for turbine in self.turbines:
            turbine.init_etat()
            turbine.calcul_perte()
            turbine.calcul_chute_nette(self)
            turbine.puiss_turbine1()
            turbine.puiss_turbine2()
            turbine.puiss_turbine3()
            turbine.puiss_turbine4()
            turbine.puiss_turbine5()
            print(turbine.chute_nette)
        return 0