import numpy as np
import pandas as pd

class Subject:

    profs = []
    label = ""

    def __init__(self, lbl):
        self.label = lbl
        self.profs = []

    def __repr__(self):
        return self.label


class Prof:

    nom = ""
    heures_tot = 0
    heures_sup_autorisees = 0
    heures_sup = 0

    def __init__(self, nom, heures, sup):
        self.nom = nom
        self.heures_tot = heures
        self.heures_sup_autorisees = sup
        self.heures_sup = 0

    def __repr__(self):
        return self.nom


def init():
    subjects = [Subject('Subject 1'),
                Subject('Subject 2'),
                Subject('Subject 3'),
                Subject('Subject 4'),
                Subject('Subject 5'),
                Subject('Subject 6')]

    return subjects


def save(subject):
    Profs = []
    Heures = []
    Sup = []
    for p in subject.profs:
        Profs.append(p.nom)
        Heures.append(p.heures_tot)
        Sup.append(p.heures_sup_autorisees)
    data = {"nom":Profs, "heures":Heures, "Sup":Sup}
    df = pd.DataFrame(data)
    print(df)




def load():
    pass
