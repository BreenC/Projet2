from src.Centrale import Centrale

class Turbine:
    def __init__(self):
        self.numero = 0
        self.debit_turbine = 0
        self.puiss_opt = 0
        self.debits = []
        self.puissance = []
        self.debit_rest = 0
        self.borne_sup = 160
        self.borne_inf = 0
        self.perte = []
        self.chute_nette = []
        self.etats = []
        self.is_disponible = True
        self.f = []


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
        while i < len(self.etats):
            tampon = 0.5 * 10**(-5) * self.etats[i] * self.etats[i]
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

    def init_etats(self, val):
        i = 0
        self.etats.append(float(i))
        while i < val :
            i = i + 5
            self.etats.append(float(i))
        return self.etats

    def rendre_indisponible(self):
        self.is_disponible = False

    def puiss_turbine1(self, debit):
        if self.numero == 1 :
            for chute in self.chute_nette:
                puissance = - 8.002 + 0.02927 * debit - 0.5131 * chute - 0.0004408 * debit * debit - 0.009321 * chute * debit - 0.008206 * chute * chute
                self.puissance.append(puissance)
                self.f.append(puissance)
        else :
            return 0

    def puiss_turbine2(self, debit):
        if self.numero == 2 :
            for chute in self.chute_nette:
                puissance = 0.6283 + 0.02915 * debit + 0.01924 * chute - 0.0000446 * debit * debit - 0.009324 * chute * debit
                self.puissance.append(puissance)
        else :
            return 0

    def puiss_turbine3(self, debit):
        if self.numero == 3 :
            for chute in self.chute_nette:
                puissance = 47.41 - 0.01254 * debit + 2.857 * chute - 0.0003613 * debit * debit - 0.01044 * chute * debit + 0.04302 * chute**2
                self.puissance.append(puissance)
        else :
            return 0

    def puiss_turbine4(self, debit):
        if self.numero == 4:
            for chute in self.chute_nette:
                puissance = -0.04632 - 0.1905 * debit + 0.001769 * chute  + 0.004951 * chute * debit + 0.003537 * debit**2 + 3.487 * 10**(-5) * chute * debit**2 -1.689 * 10**(-5) * debit**3
                self.puissance.append(puissance)
        else:
            return 0

    def puiss_turbine5(self, debit):
        if self.numero == 5:
            for chute in self.chute_nette:
                puissance = 0.2946 - 0.134 * debit + 0.008074 * chute + 0.00809  * debit**2 + 0.002706  * debit**2 + 1.949 * 10**(-5) * chute * debit**2 - 1.318 * 10**(-5) * debit**3
                self.puissance.append(puissance)
                self.f.append(puissance)
        else:
            return 0