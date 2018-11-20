from src.Centrale import Centrale

class Turbine:
    def __init__(self):
        self.numero = 0
        self.debit_turbine = 0
        self.debits = []
        self.puissance = []
        self.debit_rest = Centrale.qtot
        self.borne_sup = 160
        self.borne_inf = 0
        self.perte = []
        self.chute_nette = []
        self.etat = []
        self.is_disponible = True

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

    def contraintes(self):
        if self.debit_turbine <= self.borne_sup & self.debit_turbine >= self.borne_inf :
            return True
        else :
            return False

    def change_borne_sup(self, differance):
        self.borne_sup = self.borne_sup - differance
        return self.borne_sup

    def test_borne_sup(self):
        if self.borne_sup > self.debit_rest :
            return self.debit_rest
        else :
            return  self.borne_sup

    def init_etat(self):
        i = 0
        while i <= self.test_borne_sup() :
            i = i + 5
            self.etat.append(i)
        return self.etat

    def rendre_indisponible(self):
        self.is_disponible = False