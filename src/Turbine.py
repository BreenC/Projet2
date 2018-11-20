class Turbine:
    def __init__(self):
        self.numero
        self.debit_turbine
        self.puissance
        self.debit_rest
        self.borne_sup = 160
        self.borne_inf = 0

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

    def set_numero(self, val):
        self.numero = val

    def set_debit_turbine(self, val):
        self.debit_turbine = val

    def set_puissance(self, val):
        self.puissance = val

    def set_debit_rest(self, val):
        self.debit_rest  = val