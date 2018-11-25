"""
    Projet2 - Résolution de problèmes industriels

"""
import argparse
from src.Centrale import Centrale
from src.Parser import Parser

class Main:
    def __init__(self):
        pathqtot = "C:/Users/camil/Documents/Polytech/UQAC/trimestre 1/Optimisation/Projet 2 code/Projet2/data/qtot.txt"
        pathelamont = "C:/Users/camil/Documents/Polytech/UQAC/trimestre 1/Optimisation/Projet 2 code/Projet2/data/elamont.txt"
        #pathpuiss = "C:\Users\camil\Documents\Polytech\UQAC\trimestre 1\Optimisation\Projet 2 code\Projet2\data\puiss.txt"
        centrale = Centrale()

        parser = argparse.ArgumentParser()
        parser.add_argument("-f", "--file", help="Path to the file containing data")
        args = parser.parse_args()
        centrale
        Parser.parse_qtot(pathqtot, centrale)
        Parser.parse_elamont(pathelamont, centrale)
        #Parser.parse_Pi(pathpuiss)
        Parser.create_turbines(self,centrale)
        for val_qtot in centrale.qtot :
            centrale.run(val_qtot)

if __name__ == '__main__':
    Main()
