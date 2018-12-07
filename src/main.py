"""
    Projet2 - Résolution de problèmes industriels

"""
import argparse
from src.Centrale import Centrale
from src.Parser import Parser

class Main:
    def __init__(self):
        pathqtot = "C:/Users/camil/Documents/Polytech/UQAC/trimestre 1/Optimisation/Projet 2 code/Projet2/data/qtot.txt"
        #pathqtot = "C:/Users/mdaadaa/Desktop/Projet2/data/qtot.txt"
        pathelamont = "C:/Users/camil/Documents/Polytech/UQAC/trimestre 1/Optimisation/Projet 2 code/Projet2/data/elamont.txt"
        #pathelamont = "C:/Users/mdaadaa/Desktop/Projet2/data/elamont.txt"

        centrale = Centrale()

        parser = argparse.ArgumentParser()
        parser.add_argument("-f", "--file", help="Path to the file containing data")
        args = parser.parse_args()
        centrale
       # print("Entrer le chemin du fichier du débit total :")
       # pathqtot = input()
        Parser.parse_qtot(pathqtot, centrale)
        #print("Entrer le chemin du fichier de l'élevation en amont :")
        #pathelamont = input()
        Parser.parse_elamont(pathelamont, centrale)
        #Parser.parse_Pi(pathpuiss)
        Parser.create_turbines(self,centrale)

        param = 1
        while param != 0:
            print("Pour changer un paramètre d'une turbine entrer son numéro (de 1 à 5) sinon entrer 0 :")
            param = int(input())
            if param != 0 :
                print("Pour rendre la turbine indisponible entrer 0 sinon taper 1 :")
                dispo = input()
                if dispo == 0 :
                    for turbine in centrale.turbines:
                        if turbine.numero == param :
                            turbine.rendre_indisponible(turbine)
                print("Pour changer la borne supérieure (initialement de 160) entré la valeur a enlever ( exemple : 30 pour une borne de 130) pour ne rien changer entrer 0 :")
                borne = int(input())
                if borne <= 160 and borne >0 :
                   centrale.get_turbine_i(param).change_borne_sup(borne)

        ind = 100
       # while ind < len(centrale.qtot):
        centrale.run(ind)
            #ind = ind + 1
           # print(centrale.puissance_totale)


if __name__ == '__main__':
    Main()
