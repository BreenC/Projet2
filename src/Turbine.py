from src.Centrale import Centrale

class Turbine:
    def __init__(self):
        self.numero
        self.debit_turbine
        self.puissance
        self.debit_rest
        self.borne_sup = 160
        self.borne_inf = 0
        self.elav
        self.perte
        self.chute_nette

    def get_numero(self):
        return self.numero

    def get_debit_turbine(self):
        return  self.debit_turbine

    def get_puissance(self):
        return  self.puissance

    def get_debit_rest(self):
        return self.debit_rest

    def get_borne_sup(self):
        return self.borne_sup

    def get_borne_inf(self):
        return  self.borne_inf

    def get_chute_nette(self):
        return  self.chute_nette

    def set_numero(self, val):
        self.numero = val

    def set_debit_turbine(self, val):
        self.debit_turbine = val

    def set_puissance(self, val):
        self.puissance = val

    def set_debit_rest(self, val):
        self.debit_rest  = val

    def calcul_chute_nette(self):
        i = 1
        while i <= 200  :
            tampon = Centrale.elamont[i] - Centrale.elav[i] - self.perte[i]
            i = i + 1
            self.chute_nette.append(tampon)

    def calcul_perte(self):
        i = 1
        while i <= 200:
            tampon = 0.5 * 10^{-5} * self.debit_turbine * self.debit_turbine
            i = i + 1
            self.perte.append(tampon)