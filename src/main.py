"""
    Projet2 - Résolution de problèmes industriels

"""
import argparse


class Main:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-f", "--file", help="Path to the file containing data")
        args = parser.parse_args()


if __name__ == '__main__':
    Main()
