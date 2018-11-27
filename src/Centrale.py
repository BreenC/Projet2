class Centrale:
    def __init__(self):
        self.turbines = []
        self.qtot = []
        self.elamont = []
        self.elav = []
        self.deverse = 0
        self.puissance_totale = 0
        self.debit_turbine_total = 0
        self.chute_nette = []
        self.pertes = []

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

    def calcul_chute_nette(self,ind):
        i = 0
        while i < len(self.pertes) :
            tampon = float(self.elamont[ind]) - float(self.elav[ind]) - float(self.pertes[i])
            i = i + 1
            self.chute_nette.append(tampon)

    def calcul_pertes(self,ind):
        i = 0
        while i < self.qtot[ind]:
            tampon = 0.5 * 10**(-5) * i**2
            i = i + 5
            self.pertes.append(tampon)

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

    def calcul_deverse(self, ind):
        self.deverse = self.qtot[ind] - self.debit_turbine_total
        return  self.deverse

    def calc_f(self, ind):
        for turbine in self.turbines :
            if turbine.is_disponible == False:
                turbine.debit_turbine = 0
                turbine.puiss_opt = 0
            else:
                if turbine.numero != 5 and turbine.numero != 1 :
                    i = 0
                    turbine_prec = self.get_turbine_i(turbine.numero + 1)
                    turbine.debits = []
                    turbine.etats = []

                    while i <= self.qtot[ind] and i < len(self.chute_nette)  :
                        tampon = []
                        if i == 0:
                            turbine.f.append(0)
                            turbine.debits.append(0)
                            turbine.etats.append(0)
                            i = i + 5
                        else:
                            turbine.puiss_turbine2(i,self.chute_nette[int(i/5)])
                            turbine.puiss_turbine3(i,self.chute_nette[int(i/5)])
                            turbine.puiss_turbine4(i,self.chute_nette[int(i/5)])
                            k = 0
                            while k <= i and k <= turbine.borne_sup:
                                m = int((i-k)/5)
                                if m >= len(turbine_prec.f):
                                    m = len(turbine_prec.f) - 1
                                f = turbine.puissance + turbine_prec.f[m]
                                tampon.append(f)
                                k = k + 5
                            val = max(tampon)
                            turbine.f.append(val)
                            turbine.debits.append(tampon.index(max(tampon))*5)
                            turbine.etats.append(i)
                            i = i + 5
                elif turbine.numero == 5 :
                    i = 0
                    while i <= self.qtot[ind] :
                        if i == 0:
                            turbine.f.append(0)
                            turbine.debits.append(0)
                            turbine.etats.append(0)
                            i = i + 5
                        else:
                            turbine.etats.append(i)
                            if i <= turbine.borne_sup:
                                turbine.debits.append(i)
                                turbine.puiss_turbine5(i,self.chute_nette[int(i/5)])
                                turbine.f.append(turbine.puissance)
                            i = i + 5
                elif turbine.numero == 1:
                    turbine_prec = self.get_turbine_i(2)
                    i = 0
                    tampon = []
                    while i <= turbine.borne_sup  and i < len(self.chute_nette):
                        if i == 0:
                            turbine.etats.append(0)
                            tampon.append(0)
                            i = i + 5
                        else :
                            turbine.puiss_turbine1(i,self.chute_nette[int(i/5)])
                            m = int((turbine.borne_sup - i)/5)
                            if m >= len(turbine_prec.f):
                                m = len(turbine_prec.f) - 1
                            f = turbine.puissance + turbine_prec.f[m]
                            i = i + 5
                            turbine.etats.append(i)
                            tampon.append(f)
                    turbine.debits.append(tampon.index(max(tampon))*5)
                    turbine.f.append(max(tampon))
                    turbine.puiss_opt = max(tampon)
                    turbine.debit_turbine = tampon.index(max(tampon))*5

    def calc_opt(self, ind):
        i = 1
        r = self.qtot[ind]
        puiss = 0
        while i <= 5:
            turbine = self.get_turbine_i(i)
            if i == 1 :
                i = i + 1
            else :
                k = 0
                tampon =[]
                while k * 5 <= r and k * 5 <= turbine.borne_sup and k < len(turbine.f):
                    tampon.append(turbine.f[k])
                    k = k + 1
                turbine.puiss_opt = max(tampon)
                turbine.debit_turbine = turbine.debits[(tampon.index(max(tampon)))]
                i = i + 1
            r = r - turbine.debit_turbine
            puiss = puiss + turbine.puiss_opt
        return r

    def calc_debit_turb_total(self, ind):
        for turbine in self.turbines :
            self.debit_turbine_total = self.debit_turbine_total + turbine.debit_turbine
        self.deverse = self.qtot[ind] - self.debit_turbine_total

    def fonction_obj(self):
        for turbine in self.turbines:
            self.puissance_totale = self.puissance_totale + turbine.puiss_opt


    def run(self,ind):
        self.calcul_elva()
        self.discretidation()
        self.calcul_pertes(ind)
        self.calcul_chute_nette(ind)
        for turbine in self.turbines:
            turbine.init_etats(self, ind)
            turbine.puiss_turbine1(140,self.chute_nette[int(140/5)])
            print(turbine.puissance)
        self.calc_f(ind)
        self.calc_opt(ind)
        self.calc_debit_turb_total(ind)
        self.fonction_obj()
        print(self.chute_nette[int(140/5)])
        #print(self.debit_turbine_total)
        #print(self.deverse)
        #print("débits")

       #for turbine in self.turbines:
            #print(turbine.borne_sup)
          # print(turbine.debit_turbine)
        return  0