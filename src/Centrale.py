class Centrale:
    def __init__(self):
        self.turbines = []
        self.qtot = []
        self.elamont = []
        self.elav = []
        self.deverse = 0
        self.puissance_totale = 0
        self.debit_turbine_total = 0

    def get_turbines(self):
        return self.turbines

    def get_elamont(self):
        return self.elamont

    def get_turbine_i(self,i):
        for turbine in self.turbines :
            if turbine.numero == i :
                return turbine

    def get_qtot(self):
        return self.qtot

    def discretidation(self):
        i = 0
        while i < len(self.qtot) :
            self.qtot[i]  = round(self.qtot[i])
            if self.qtot[i] % 5 > 2.5:
                self.qtot[i] = self.qtot[i] + 5 - self.qtot[i] % 5
            else:
                self.qtot[i] = self.qtot[i] - self.qtot[i] % 5
            i = i+1
        return self.qtot

    def calcul_elva(self):
        i = 1
        while i < 200:
            tampon = - 7.014 * 10**(-7) * self.qtot[i] * self.qtot[i] + 0.004107 * self.qtot[i] + 137.2
            i = i + 1
            self.elav.append(tampon)



    def calcul_deverse(self):
        self.deverse = self.qtot - self.debit_turbine_total
        return  self.deverse

    def calc_f(self, val_qtot):
        for turbine in self.turbines :
            if turbine.numero != 5 and turbine.numero != 1 :
                i = 0
                turbine_prec = self.get_turbine_i(turbine.numero + 1)
                turbine.debits = []
                turbine.etats = []
                while i <= val_qtot  :
                    turbine.puiss_turbine2(i)
                    turbine.puiss_turbine3(i)
                    turbine.puiss_turbine4(i)
                    k = 0
                    tampon = []
                    while k <= i and k <= turbine.borne_sup:
                        m = int((i-k)/5)
                        f = turbine.puissance[i] + turbine_prec.f[m]
                        tampon.append(f)
                        k = k + 5
                    val = max(tampon)
                    turbine.f.append(val)
                    turbine.debits.append(tampon.index(max(tampon)) * 5)
                    turbine.etats.append(i)
                    i = i + 5
            elif turbine.numero == 5 :
                i = 0
                while i <= val_qtot :
                    turbine.etats.append(i)
                    if i <= turbine.borne_sup:
                        turbine.debits.append(i)
                        turbine.puiss_turbine5(i)
                    i = i + 5
            elif turbine.numero == 1:
                turbine_prec = self.get_turbine_i(2)
                i = 0
                tampon = []
                while i <= turbine.borne_sup :
                    turbine.puiss_turbine1(i)
                    m = int((val_qtot - i)/5)
                    f = turbine.puissance[i]  + turbine_prec.f[m]
                    i = i + 5
                    tampon.append(f)
                turbine.debits.append(tampon.index(max(tampon))*5)
                turbine.etats.append(val_qtot)
                turbine.f.append(max(tampon))
                turbine.puiss_opt = max(tampon)
                turbine.debit_turbine = tampon.index(max(tampon))*5

    def calc_opt(self, val_qtot):
        i = 1
        r = val_qtot
        puiss = 0
        while i <= 5:
            turbine = self.get_turbine_i(i)
            if i == 1 :
                i = i + 1
            else :
                k = 0
                tampon =[]
                while k * 5 <= r and k*5 <= turbine.borne_sup :
                    tampon.append(turbine.f[k])
                    k = k + 1
                turbine.puiss_opt = max(tampon)
                turbine.debit_turbine = turbine.debits[(tampon.index(max(tampon)))]
                i = i + 1

    #REMETTRE AU PROPRE
          #  if turbine.is_disponible == False:
          #       turbine.debit_turbine = 0
          #  else:
          #       turbine.debit_turbine = max(turbine.debits)
            r = r - turbine.debit_turbine
            puiss = puiss + turbine.puiss_opt
        return r

    def fonction_obj(self):
        for turbine in self.turbines:
            self.puissance_totale = self.puissance_totale + turbine.puiss_opt

    def run(self):
        self.calcul_elva()
        self.discretidation()
        for turbine in self.turbines:
            turbine.init_etats(self.qtot[5])
            turbine.calcul_perte()
            turbine.calcul_chute_nette(self)
        self.calc_f(self.qtot[5])
        r = self.calc_opt(self.qtot[5])
        print(self.qtot[5])
        print(r)
        #for turbine in self.turbines:
         #   print("numéro : ")
          #  print(turbine.numero)
        # print("puissance : ")
         #   print(turbine.puiss_opt)
          #  print("débit : ")
           # print( turbine.debit_turbine)
        return  0