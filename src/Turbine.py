from src.Centrale import Centrale

class Turbine:
    def __init__(self):
        self.numero = 0
        self.debit_turbine = 0
        self.debits = []
        self.puissance = []
        self.debit_rest = 0
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

    def calcul_chute_nette(self, centrale):
        i = 0
        while i < len(self.perte)  :
            tampon = float(centrale.elamont[i]) - float(centrale.elav[i]) - float(self.perte[i])
            i = i + 1
            self.chute_nette.append(tampon)

    def calcul_perte(self):
        i = 0
        while i < len(self.etat):
            tampon = 0.5 * 10**(-5) * self.etat[i] * self.etat[i]
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
            self.etat.append(float(i))
        return self.etat

    def rendre_indisponible(self):
        self.is_disponible = False

    def puiss_turbine1(self):
        if self.numero == 1 :
            for chute in self.chute_nette:
                self.puissance = -8.002 + 0.02927 * self.debit_turbine - 0.5131 * chute - 0.0004408 * self.debit_turbine * self.debit_turbine - 0.009321 * chute * self.debit_turbine - 0.008206 * chute * chute
        else :
            return 0

    def puiss_turbine2(self):
        if self.numero == 2 :
            for chute in self.chute_nette:
                self.puissance = 0.6283 + 0.02915 * self.debit_turbine + 0.01924 * chute - 0.0000446 * self.debit_turbine * self.debit_turbine - 0.009324 * chute * self.debit_turbine
        else :
            return 0

    def puiss_turbine3(self):
        if self.numero == 3 :
            for chute in self.chute_nette:
                self.puissance = 47.41 - 0.01254 * self.debit_turbine + 2.857 * chute - 0.0003613 * self.debit_turbine * self.debit_turbine - 0.01044 * chute * self.debit_turbine + 0.04302 * chute**2
        else :
            return 0

    def puiss_turbine4(self):
        if self.numero == 4:
            for chute in self.chute_nette:
                self.puissance = -0.04632 - 0.1905 * self.debit_turbine + 0.001769 * chute  + 0.004951 * chute * self.debit_turbine + 0.003537 * self.debit_turbine**2 + 3.487 * 10**(-5) * chute * self.debit_turbine**2 -1.689 * 10**(-5) * self.debit_turbine**3
        else:
            return 0

    def puiss_turbine5(self):
        if self.numero == 5:
            for chute in self.chute_nette:
                self.puissance = 0.2946 - 0.134 * self.debit_turbine + 0.008074 * chute + 0.00809  * self.debit_turbine * self.debit_turbine + 0.002706  * self.debit_turbine**2 + 1.949 * 10**(-5) * chute * self.debit_turbine**2 - 1.318 * 10**(-5) * self.debit_turbine**3
        else:
            return 0

