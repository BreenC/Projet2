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

    def puiss_turbine1(self):
        if self.numero == 1 :
            self.puissance = -8.002 + 0.02927 * self.debit_turbine - 0.5131 * self.chute_nette - 0.0004408 * self.debit_turbine * self.debit_turbine - 0.009321 * self.chute_nette * self.debit_turbine - 0.008206 * self.chute_nette * self.chute_nette
        else :
            return 0

    def puiss_turbine2(self):
        if self.numero == 2 :
            self.puissance = 0.6283 + 0.02915 * self.debit_turbine + 0.01924 * self.chute_nette - 0.0000446 * self.debit_turbine * self.debit_turbine - 0.009324 * self.chute_nette * self.debit_turbine
        else :
            return 0

    def puiss_turbine3(self):
        if self.numero == 3 :
            self.puissance = 47.41 - 0.01254 * self.debit_turbine + 2.857 * self.chute_nette - 0.0003613 * self.debit_turbine * self.debit_turbine - 0.01044 * self.chute_nette * self.debit_turbine + 0.04302 * self.chute_nette * self.chute_nette
        else :
            return 0

    def puiss_turbine4(self):
        if self.numero == 4:
            #a changer la formule est toute fausse c'est celle de la turbine 1 sans changement
            self.puissance = 47.41 - 0.01254 * self.debit_turbine + 2.857 * self.chute_nette - 0.0003613 * self.debit_turbine * self.debit_turbine - 0.01044 * self.chute_nette * self.debit_turbine + 0.04302 * self.chute_nette * self.chute_nette
        else:
            return 0

    def puiss_turbine5(self):
        if self.numero == 5:
            #a changer le chiffre avant x^3
            self.puissance = 5.42 - 0.443 * self.debit_turbine + 0.1635 * self.chute_nette + 0.004277 * self.debit_turbine * self.debit_turbine - 0.01564 * self.chute_nette * self.debit_turbine - 0.39 * 10^{-5} * self.debit_turbine * self.debit_turbine * self.debit_turbine + 2.318 * 10^{-5} * self.debit_turbine * self.debit_turbine * self.chute_nette
        else:
            return 0