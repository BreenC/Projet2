from src.Centrale import Centrale
from src.Turbine import Turbine


class Parser:
    def __init__(self):
        self

    @staticmethod
    def parse_qtot(path, centrale):
        print("Parsing...")
        file = open(path, 'r')
        qtot = []
        for line in file.readlines():
            qtot.append(float(line))
        if len(qtot) != 200:
            print("Error, Qtot has", len(qtot), "cells, should be 200 !")
            raise Exception("Wrong test file format, incorrect number of cells")
        centrale.qtot = qtot
        return qtot

    @staticmethod
    def parse_elamont(path, centrale):
        print("Parsing...")
        file = open(path, 'r')
        for line in file.readlines():
            centrale.elamont.append((line))
        if len(centrale.elamont) != 200:
            print("Error, elamont has", len(centrale.elamont), "cells, should be 200 !")
            raise Exception("Wrong elamont file format, incorrect number of cells")
        return centrale.elamont


    @staticmethod
    def parse_Pi(path):
        print("Parsing...")
        file = open(path, 'r')
        puissances = []
        for line in file.read().rstrip():
            i = 1
            for nb in line.strip():
                puissances[i].append(float(nb))
                i = i + 1
            if i != 5:
                print("Error, le nombre de turbine est", i, "valeurs, cela devrait être 5 !")
                raise Exception("Wrong Puissance file format, incorrect number of cells")
        if len(puissances) != 200:
            print("Error, Puissance des turbines est", len(puissances), "valeurs, cela devrait être 200 !")
            raise Exception("Wrong Puissance file format, incorrect number of cells")
        i = 1
        for turbine in Centrale.turbines :
            turbine.numero = 6 - i
            turbine.puissance = puissances[6 - i]
            i = i + 1
        if i != 5:
            print("Error, le nombre de turbine est", i, "valeurs, cela devrait être 5 !")
            raise Exception("Wrong Puissance file format, incorrect number of cells")
        return puissances

    def create_turbines(self, centrale):
        i = 5
        if i >0:
            turbine = Turbine()
            turbine.numero = i
            centrale.turbines.append(turbine)
            i = i - 1
        if i != 5:
            print("Error, le nombre de turbine est", i, "valeurs, cela devrait être 5 !")
            raise Exception("Wrong Puissance file format, incorrect number of cells")