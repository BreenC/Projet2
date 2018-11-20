from src.Centrale import Centrale

class Parser:
    def __init__(self):
        self

    @staticmethod
    def parse_qtot(path):
        print("Parsing...")
        file = open(path, 'r')
        for line in file.read().rstrip():
            Centrale.qtot.append(float(line))
        if len(Centrale.qtot) != 200:
            print("Error, Qtot has", len(Centrale.qtot), "cells, should be 200 !")
            raise Exception("Wrong test file format, incorrect number of cells")
        return Centrale.qtot

    @staticmethod
    def parse_elamont(path):
        print("Parsing...")
        file = open(path, 'r')
        for line in file.read().rstrip():
            Centrale.elamont.append(float(line))
        if len(Centrale.elamont) != 200:
            print("Error, elamont has", len(Centrale.elamont), "cells, should be 200 !")
            raise Exception("Wrong elamont file format, incorrect number of cells")
        return Centrale.elamont


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
