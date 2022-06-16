class Prof:
    Nom = ""
    heures = 0
    heures_max = 0
    heures_sup = 0

    def __init__(self, _nom, _heures_max):
        self.Nom = _nom
        self.heures_max = _heures_max

    def __repr__(self):
        return self.Nom


class Cls:
    label = ""
    heures_totales = 0
    heures_attribues = 0
    matiere = None
    assignments = {}

    def __init__(self, mat, _label, _heures_totales):
        self.matiere = mat
        self.label = _label
        self.heures_totales = _heures_totales
        self.heures_attribues = 0
        self.assignments = {}

    def __repr__(self):
        return self.label

    def assigner_prof(self, prof, heures):
        self.assignments[prof] = heures
        self.heures_attribues += heures


class Matiere:
    Profs = []
    Classes = {}
    Label = ''

    def __init__(self, label):
        self.Profs = []
        self.Classes = {}
        self.Label = label

    def __repr__(self):
        return self.Label

    def assigner_prof(self, _classe, _prof, _heures):
        # self.Profs[_prof.Nom] = _heures
        # _prof.heures += _heures
        # self.Classes[_classe].heures_attribues += _heures
        pass

    def creer_classe(self, nom, heures_totales):
        cl = Cls(self, nom, heures_totales)
        self.Classes[cl.label] = cl

    def creer_prof(self, nom, heures_max):
        p = Prof(nom, heures_max)
        self.Profs.append(p)


# Attribuer chaque classe

# region L0100_Philosophie

L0100_Philosophie = Matiere('L0100_Philosophie')
L0100_Philosophie.creer_classe('1ere_Spécialités', 6)
L0100_Philosophie.creer_classe('TG1', 4)
L0100_Philosophie.creer_classe('TG2', 4)
L0100_Philosophie.creer_classe('TG3', 4)
L0100_Philosophie.creer_classe('TG4', 4)
L0100_Philosophie.creer_classe('TG5', 4)
L0100_Philosophie.creer_classe('TG6', 4)
L0100_Philosophie.creer_classe('TG7', 4)
L0100_Philosophie.creer_classe('TG8', 4)
L0100_Philosophie.creer_classe('Term_Spécialités', 6)
L0100_Philosophie.creer_classe('TST2S', 2)
L0100_Philosophie.creer_classe('TSTMG', 2)
L0100_Philosophie.creer_classe('ECG1', 3)
L0100_Philosophie.creer_classe('ECG2', 3)
L0100_Philosophie.creer_classe('AL1', 4)
L0100_Philosophie.creer_classe('AL2', 6)
# endregion
# region L0201_Lett_Class
L0201_Lett_Class = Matiere('L0201_Lett_Class')
L0201_Lett_Class.creer_classe('2nd_Options', 3)
L0201_Lett_Class.creer_classe('1ere_Autres', 3)
L0201_Lett_Class.creer_classe('term_Spécialités', 6)
L0201_Lett_Class.creer_classe('AL1', 13)
L0201_Lett_Class.creer_classe('AL2', 12)
# endregion
# region L0202_Lett_Mod
L0202_Lett_Mod = Matiere('L0202_Lett_Mod')
L0202_Lett_Mod.creer_classe('2GT1', 5)
L0202_Lett_Mod.creer_classe('2GT2', 5)
L0202_Lett_Mod.creer_classe('2GT3', 5)
L0202_Lett_Mod.creer_classe('2GT4', 5)
L0202_Lett_Mod.creer_classe('2GT5', 5)
L0202_Lett_Mod.creer_classe('2GT6', 5)
L0202_Lett_Mod.creer_classe('2GT7', 5)
L0202_Lett_Mod.creer_classe('2GT8', 5)
L0202_Lett_Mod.creer_classe('2GT9', 5)
L0202_Lett_Mod.creer_classe('2GT10', 5)
L0202_Lett_Mod.creer_classe('2GT11', 5)
L0202_Lett_Mod.creer_classe('2nd_Options', 5)
L0202_Lett_Mod.creer_classe('2nd_Autres', 5)
L0202_Lett_Mod.creer_classe('1eGT1', 5)
L0202_Lett_Mod.creer_classe('1eGT2', 5)
L0202_Lett_Mod.creer_classe('1eGT3', 5)
L0202_Lett_Mod.creer_classe('1eGT4', 5)
L0202_Lett_Mod.creer_classe('1eGT5', 5)
L0202_Lett_Mod.creer_classe('1eGT6', 5)
L0202_Lett_Mod.creer_classe('1eGT7', 5)
L0202_Lett_Mod.creer_classe('1eGT8', 5)
L0202_Lett_Mod.creer_classe('1eGT9', 5)
L0202_Lett_Mod.creer_classe('1ere_Spécialités', 6)
L0202_Lett_Mod.creer_classe('1ere_Autres', 3)
L0202_Lett_Mod.creer_classe('1eST2S', 4)
L0202_Lett_Mod.creer_classe('1eSTMG', 4)
L0202_Lett_Mod.creer_classe('Term_Spécialités', 6)
L0202_Lett_Mod.creer_classe('Term_Autres', 3)
L0202_Lett_Mod.creer_classe('BTS1_COM', 7.5)
L0202_Lett_Mod.creer_classe('BTS2_COM', 7.5)
L0202_Lett_Mod.creer_classe('BTS1_MCO', 3.75)
L0202_Lett_Mod.creer_classe('BTS2_MCO', 3.75)
L0202_Lett_Mod.creer_classe('BTS1_SAM', 8.75)
L0202_Lett_Mod.creer_classe('BTS2_SAM', 8.75)
L0202_Lett_Mod.creer_classe('BTS1_CG', 5)
L0202_Lett_Mod.creer_classe('BTS2_CG', 5)
L0202_Lett_Mod.creer_classe('ECG1', 3)
L0202_Lett_Mod.creer_classe('ECG2', 3)
L0202_Lett_Mod.creer_classe('AL1', 5)
L0202_Lett_Mod.creer_classe('AL2', 5)
# endregion
# region L0421_Allemand
L0421_Allemand = Matiere('L0421_Allemand')
L0421_Allemand.creer_classe('1eGT9', 2)
# endregion
# region L0422_Anglais
L0422_Anglais = Matiere('L0422_Anglais')
L0422_Anglais.creer_classe('2GT1', 9)
L0422_Anglais.creer_classe('2GT2', 9)
L0422_Anglais.creer_classe('2GT3', 9)
L0422_Anglais.creer_classe('2GT4', 9)
L0422_Anglais.creer_classe('2GT5', 9)
L0422_Anglais.creer_classe('2GT6', 9)
L0422_Anglais.creer_classe('2GT7', 9)
L0422_Anglais.creer_classe('2GT8', 9)
L0422_Anglais.creer_classe('2GT9', 9)
L0422_Anglais.creer_classe('2GT10', 9)
L0422_Anglais.creer_classe('2GT11', 9)
L0422_Anglais.creer_classe('2nd_Options', 5)
L0422_Anglais.creer_classe('1eGT1', 7.5)
L0422_Anglais.creer_classe('1eGT2', 7.5)
L0422_Anglais.creer_classe('1eGT3', 7.5)
L0422_Anglais.creer_classe('1eGT4', 7.5)
L0422_Anglais.creer_classe('1eGT5', 7.5)
L0422_Anglais.creer_classe('1eGT6', 7.5)
L0422_Anglais.creer_classe('1eGT7', 7.5)
L0422_Anglais.creer_classe('1eGT8', 7.5)
L0422_Anglais.creer_classe('1eGT9', 5)
L0422_Anglais.creer_classe('1ere_Spécialités', 8)
L0422_Anglais.creer_classe('1ere_Autres', 5)
L0422_Anglais.creer_classe('1eST2S', 4.5)
L0422_Anglais.creer_classe('TG1', 6)
L0422_Anglais.creer_classe('TG2', 6)
L0422_Anglais.creer_classe('TG3', 6)
L0422_Anglais.creer_classe('TG4', 6)
L0422_Anglais.creer_classe('TG5', 6)
L0422_Anglais.creer_classe('TG6', 6)
L0422_Anglais.creer_classe('TG7', 6)
L0422_Anglais.creer_classe('TG8', 6)
L0422_Anglais.creer_classe('Term_Spécialités', 12)
L0422_Anglais.creer_classe('Term_Autres', 5)
L0422_Anglais.creer_classe('TST2S', 4.5)
L0422_Anglais.creer_classe('BTS1_COM', 3.75)
L0422_Anglais.creer_classe('BTS2_COM', 3.75)
L0422_Anglais.creer_classe('BTS1_MCO', 6.25)
L0422_Anglais.creer_classe('BTS2_MCO', 6.25)
L0422_Anglais.creer_classe('BTS1_SAM', 6.25)
L0422_Anglais.creer_classe('BTS2_SAM', 6.25)
L0422_Anglais.creer_classe('BTS1_CG', 3.75)
L0422_Anglais.creer_classe('BTS2_CG', 3.75)
L0422_Anglais.creer_classe('ECG1', 3)
L0422_Anglais.creer_classe('ECG2', 3)
L0422_Anglais.creer_classe('AL1', 4)
L0422_Anglais.creer_classe('AL2', 6)

# endregion
# region L0426_Espagnol
L0426_Espagnol = Matiere('L0426_Espagnol')
L0426_Espagnol.creer_classe('2GT1', 7.5)
L0426_Espagnol.creer_classe('2GT2', 7.5)
L0426_Espagnol.creer_classe('2GT3', 7.5)
L0426_Espagnol.creer_classe('2GT4', 7.5)
L0426_Espagnol.creer_classe('2GT5', 7.5)
L0426_Espagnol.creer_classe('2GT6', 7.5)
L0426_Espagnol.creer_classe('2GT7', 7.5)
L0426_Espagnol.creer_classe('2GT8', 7.5)
L0426_Espagnol.creer_classe('2GT9', 7.5)
L0426_Espagnol.creer_classe('2GT10', 7.5)
L0426_Espagnol.creer_classe('2GT11', 5)
L0426_Espagnol.creer_classe('2nd_Options', 4)
L0426_Espagnol.creer_classe('2nd_Autres', 1)
L0426_Espagnol.creer_classe('1eGT1', 6)
L0426_Espagnol.creer_classe('1eGT2', 6)
L0426_Espagnol.creer_classe('1eGT3', 6)
L0426_Espagnol.creer_classe('1eGT4', 6)
L0426_Espagnol.creer_classe('1eGT5', 6)
L0426_Espagnol.creer_classe('1eGT6', 6)
L0426_Espagnol.creer_classe('1eGT7', 6)
L0426_Espagnol.creer_classe('1eGT8', 6)
L0426_Espagnol.creer_classe('1eGT9', 4)
L0426_Espagnol.creer_classe('1ere_Spécialités', 4)
L0426_Espagnol.creer_classe('1ere_Autres', 5)
L0426_Espagnol.creer_classe('1eST2S', 4.5)
L0426_Espagnol.creer_classe('1eSTMG', 4.5)
L0426_Espagnol.creer_classe('TG1', 6)
L0426_Espagnol.creer_classe('TG2', 6)
L0426_Espagnol.creer_classe('TG3', 6)
L0426_Espagnol.creer_classe('TG4', 6)
L0426_Espagnol.creer_classe('TG5', 6)
L0426_Espagnol.creer_classe('TG6', 6)
L0426_Espagnol.creer_classe('TG7', 6)
L0426_Espagnol.creer_classe('TG8', 6)
L0426_Espagnol.creer_classe('Term_Spécialités', 6)
L0426_Espagnol.creer_classe('Term_Autres', 5)
L0426_Espagnol.creer_classe('TST2S', 4.5)
L0426_Espagnol.creer_classe('TSTMG', 4.5)
L0426_Espagnol.creer_classe('BTS1_SAM', 6.25)
L0426_Espagnol.creer_classe('BTS2_SAM', 6.25)
L0426_Espagnol.creer_classe('ECG1', 3)
L0426_Espagnol.creer_classe('ECG2', 3)
L0426_Espagnol.creer_classe('AL1', 4)
L0426_Espagnol.creer_classe('AL2', 7)

# endregion
# region L0449_Creole
L0449_Creole = Matiere('L0449_Creole')
L0449_Creole.creer_classe('2nd_Options', 3)
L0449_Creole.creer_classe('1ere_Autres', 3)

# endregion
# region L0433_Portugais
L0433_Portugais = Matiere('L0433_Portugais')
L0433_Portugais.creer_classe('2nd_Options', 3)
L0433_Portugais.creer_classe('1ere_Autres', 3)

# endregion
# region L1000_Hit_Geo
L1000_Hit_Geo = Matiere('L1000_Hit_Geo')
L1000_Hit_Geo.creer_classe('2GT1', 3.5)
L1000_Hit_Geo.creer_classe('2GT2', 3.5)
L1000_Hit_Geo.creer_classe('2GT3', 3.5)
L1000_Hit_Geo.creer_classe('2GT4', 3.5)
L1000_Hit_Geo.creer_classe('2GT5', 3.5)
L1000_Hit_Geo.creer_classe('2GT6', 3.5)
L1000_Hit_Geo.creer_classe('2GT7', 3.5)
L1000_Hit_Geo.creer_classe('2GT8', 3.5)
L1000_Hit_Geo.creer_classe('2GT9', 3.5)
L1000_Hit_Geo.creer_classe('2GT10', 3.5)
L1000_Hit_Geo.creer_classe('2GT11', 3.5)
L1000_Hit_Geo.creer_classe('2nd_Autres', 8)
L1000_Hit_Geo.creer_classe('1eGT1', 3.5)
L1000_Hit_Geo.creer_classe('1eGT2', 3.5)
L1000_Hit_Geo.creer_classe('1eGT3', 3.5)
L1000_Hit_Geo.creer_classe('1eGT4', 3.5)
L1000_Hit_Geo.creer_classe('1eGT5', 3.5)
L1000_Hit_Geo.creer_classe('1eGT6', 3.5)
L1000_Hit_Geo.creer_classe('1eGT7', 3.5)
L1000_Hit_Geo.creer_classe('1eGT8', 3.5)
L1000_Hit_Geo.creer_classe('1eGT9', 3.5)
L1000_Hit_Geo.creer_classe('1ere_Spécialités', 12)
L1000_Hit_Geo.creer_classe('1ere_Autres', 9)
L1000_Hit_Geo.creer_classe('1eST2S', 2)
L1000_Hit_Geo.creer_classe('1eSTMG', 2)
L1000_Hit_Geo.creer_classe('TG1', 3.5)
L1000_Hit_Geo.creer_classe('TG2', 3.5)
L1000_Hit_Geo.creer_classe('TG3', 3.5)
L1000_Hit_Geo.creer_classe('TG4', 3.5)
L1000_Hit_Geo.creer_classe('TG5', 3.5)
L1000_Hit_Geo.creer_classe('TG6', 3.5)
L1000_Hit_Geo.creer_classe('TG7', 3.5)
L1000_Hit_Geo.creer_classe('TG8', 3.5)
L1000_Hit_Geo.creer_classe('Term_Spécialités', 18)
L1000_Hit_Geo.creer_classe('Term_Autres', 9)
L1000_Hit_Geo.creer_classe('TST2S', 2)
L1000_Hit_Geo.creer_classe('TSTMG', 2)
L1000_Hit_Geo.creer_classe('ECG1', 6)
L1000_Hit_Geo.creer_classe('AL1', 9)
L1000_Hit_Geo.creer_classe('AL2', 13)
# endregion
# region L1100_Sc_Eco_Soc
L1100_Sc_Eco_Soc = Matiere('L1100_Sc_Eco_Soc')
L1100_Sc_Eco_Soc.creer_classe('2GT1', 1.5)
L1100_Sc_Eco_Soc.creer_classe('2GT2', 1.5)
L1100_Sc_Eco_Soc.creer_classe('2GT3', 1.5)
L1100_Sc_Eco_Soc.creer_classe('2GT4', 1.5)
L1100_Sc_Eco_Soc.creer_classe('2GT5', 1.5)
L1100_Sc_Eco_Soc.creer_classe('2GT6', 1.5)
L1100_Sc_Eco_Soc.creer_classe('2GT7', 1.5)
L1100_Sc_Eco_Soc.creer_classe('2GT8', 1.5)
L1100_Sc_Eco_Soc.creer_classe('2GT9', 1.5)
L1100_Sc_Eco_Soc.creer_classe('2GT10', 1.5)
L1100_Sc_Eco_Soc.creer_classe('2GT11', 1.5)
L1100_Sc_Eco_Soc.creer_classe('1ere_Spécialités', 12)
L1100_Sc_Eco_Soc.creer_classe('Term_Spécialités', 18)
L1100_Sc_Eco_Soc.creer_classe('ECG2', 8)
# endregion
# region L1300_Math
L1300_Math = Matiere('L1300_Math')
L1300_Math.creer_classe('2GT1', 5.5)
L1300_Math.creer_classe('2GT2', 5.5)
L1300_Math.creer_classe('2GT3', 5.5)
L1300_Math.creer_classe('2GT4', 5.5)
L1300_Math.creer_classe('2GT5', 5.5)
L1300_Math.creer_classe('2GT6', 5.5)
L1300_Math.creer_classe('2GT7', 5.5)
L1300_Math.creer_classe('2GT8', 5.5)
L1300_Math.creer_classe('2GT9', 5.5)
L1300_Math.creer_classe('2GT10', 5.5)
L1300_Math.creer_classe('2GT11', 5.5)
L1300_Math.creer_classe('2nd_Options', 33)
L1300_Math.creer_classe('2nd_Autres', 1)
L1300_Math.creer_classe('1ere_Spécialités', 20)
L1300_Math.creer_classe('1ere_Autres', 1)
L1300_Math.creer_classe('1eST2S', 4)
L1300_Math.creer_classe('1eSTMG', 4)
L1300_Math.creer_classe('Term_Spécialités', 18)
L1300_Math.creer_classe('Term_Autres', 7)
L1300_Math.creer_classe('TST2S', 3.125)
L1300_Math.creer_classe('TSTMG', 3.125)
L1300_Math.creer_classe('ECG1', 11)
L1300_Math.creer_classe('ECG2', 9)
# endregion
# region L1500_Phys_Chim
L1500_Phys_Chim = Matiere('L1500_Phys_Chim')
L1500_Phys_Chim.creer_classe('2GT1', 9)
L1500_Phys_Chim.creer_classe('2GT2', 9)
L1500_Phys_Chim.creer_classe('2GT3', 9)
L1500_Phys_Chim.creer_classe('2GT4', 9)
L1500_Phys_Chim.creer_classe('2GT5', 9)
L1500_Phys_Chim.creer_classe('2GT6', 9)
L1500_Phys_Chim.creer_classe('2GT7', 9)
L1500_Phys_Chim.creer_classe('2GT8', 9)
L1500_Phys_Chim.creer_classe('2GT9', 9)
L1500_Phys_Chim.creer_classe('2GT10', 9)
L1500_Phys_Chim.creer_classe('2GT11', 6)
L1500_Phys_Chim.creer_classe('2nd_Autres', 3)
L1500_Phys_Chim.creer_classe('1eGT1', 1.5)
L1500_Phys_Chim.creer_classe('1eGT2', 1.5)
L1500_Phys_Chim.creer_classe('1eGT3', 1.5)
L1500_Phys_Chim.creer_classe('1eGT4', 1.5)
L1500_Phys_Chim.creer_classe('1eGT5', 1.5)
L1500_Phys_Chim.creer_classe('1eGT6', 1.5)
L1500_Phys_Chim.creer_classe('1eGT7', 1.5)
L1500_Phys_Chim.creer_classe('1eGT8', 1.5)
L1500_Phys_Chim.creer_classe('1eGT9', 1.5)
L1500_Phys_Chim.creer_classe('1ere_Spécialités', 16)
L1500_Phys_Chim.creer_classe('1eST2S', 4.5)
L1500_Phys_Chim.creer_classe('TG1', 1.5)
L1500_Phys_Chim.creer_classe('TG2', 1.5)
L1500_Phys_Chim.creer_classe('TG3', 1.5)
L1500_Phys_Chim.creer_classe('TG4', 1.5)
L1500_Phys_Chim.creer_classe('TG5', 1.5)
L1500_Phys_Chim.creer_classe('TG6', 1.5)
L1500_Phys_Chim.creer_classe('TG7', 1.5)
L1500_Phys_Chim.creer_classe('TG8', 1.5)
L1500_Phys_Chim.creer_classe('Term_Spécialités', 22)
L1500_Phys_Chim.creer_classe('TST2S', 4)
# endregion
# region NSI
NSI = Matiere('NSI')
NSI.creer_classe('1ere_Spécialités', 4)
NSI.creer_classe('Term_Spécialités', 6)
# endregion
# region L1600_SVT
L1600_SVT = Matiere('L1600_SVT')
L1600_SVT.creer_classe('2GT1', 4.5)
L1600_SVT.creer_classe('2GT2', 4.5)
L1600_SVT.creer_classe('2GT3', 4.5)
L1600_SVT.creer_classe('2GT4', 4.5)
L1600_SVT.creer_classe('2GT5', 4.5)
L1600_SVT.creer_classe('2GT6', 4.5)
L1600_SVT.creer_classe('2GT7', 4.5)
L1600_SVT.creer_classe('2GT8', 4.5)
L1600_SVT.creer_classe('2GT9', 4.5)
L1600_SVT.creer_classe('2GT10', 4.5)
L1600_SVT.creer_classe('2GT11', 3)
L1600_SVT.creer_classe('1eGT1', 3.5)
L1600_SVT.creer_classe('1eGT2', 3.5)
L1600_SVT.creer_classe('1eGT3', 3.5)
L1600_SVT.creer_classe('1eGT4', 3.5)
L1600_SVT.creer_classe('1eGT5', 3.5)
L1600_SVT.creer_classe('1eGT6', 3.5)
L1600_SVT.creer_classe('1eGT7', 3.5)
L1600_SVT.creer_classe('1eGT8', 3.5)
L1600_SVT.creer_classe('1eGT9', 3.5)
L1600_SVT.creer_classe('1ere_Spécialités', 16)
L1600_SVT.creer_classe('TG1', 1.5)
L1600_SVT.creer_classe('TG2', 1.5)
L1600_SVT.creer_classe('TG3', 1.5)
L1600_SVT.creer_classe('TG4', 1.5)
L1600_SVT.creer_classe('TG5', 1.5)
L1600_SVT.creer_classe('TG6', 1.5)
L1600_SVT.creer_classe('TG7', 1.5)
L1600_SVT.creer_classe('TG8', 1.5)
L1600_SVT.creer_classe('Term_Spécialités', 22)
# endregion
# region L1800_Arts_Plastiques
L1800_Arts_Plastiques = Matiere('L1800_Arts_Plastiques')
L1800_Arts_Plastiques.creer_classe('2nd_Options', 3)
L1800_Arts_Plastiques.creer_classe('1ere_Spécialités', 4)
L1800_Arts_Plastiques.creer_classe('1ere_Autres', 3)
L1800_Arts_Plastiques.creer_classe('Term_Spécialités', 6)
L1800_Arts_Plastiques.creer_classe('Term_Autres', 3)
# endregion
# region L1900_Eps
L1900_Eps = Matiere('L1900_Eps')
L1900_Eps.creer_classe('2GT1', 2)
L1900_Eps.creer_classe('2GT2', 2)
L1900_Eps.creer_classe('2GT3', 2)
L1900_Eps.creer_classe('2GT4', 2)
L1900_Eps.creer_classe('2GT5', 2)
L1900_Eps.creer_classe('2GT6', 2)
L1900_Eps.creer_classe('2GT7', 2)
L1900_Eps.creer_classe('2GT8', 2)
L1900_Eps.creer_classe('2GT9', 2)
L1900_Eps.creer_classe('2GT10', 2)
L1900_Eps.creer_classe('2GT11', 2)
L1900_Eps.creer_classe('2nd_Autres', 3)
L1900_Eps.creer_classe('1eGT1', 2)
L1900_Eps.creer_classe('1eGT2', 2)
L1900_Eps.creer_classe('1eGT3', 2)
L1900_Eps.creer_classe('1eGT4', 2)
L1900_Eps.creer_classe('1eGT5', 2)
L1900_Eps.creer_classe('1eGT6', 2)
L1900_Eps.creer_classe('1eGT7', 2)
L1900_Eps.creer_classe('1eGT8', 2)
L1900_Eps.creer_classe('1eGT9', 2)
L1900_Eps.creer_classe('1ere_Spécialités', 4)
L1900_Eps.creer_classe('1ere_Autres', 3)
L1900_Eps.creer_classe('1eST2S', 2)
L1900_Eps.creer_classe('1eSTMG', 2)
L1900_Eps.creer_classe('TG1', 2)
L1900_Eps.creer_classe('TG2', 2)
L1900_Eps.creer_classe('TG3', 2)
L1900_Eps.creer_classe('TG4', 2)
L1900_Eps.creer_classe('TG5', 2)
L1900_Eps.creer_classe('TG6', 2)
L1900_Eps.creer_classe('TG7', 2)
L1900_Eps.creer_classe('TG8', 2)
L1900_Eps.creer_classe('Term_Spécialités', 6)
L1900_Eps.creer_classe('Term_Autres', 3)
L1900_Eps.creer_classe('TST2S', 2)
L1900_Eps.creer_classe('TSTMG', 2)
L1900_Eps.creer_classe('ECG1', 2)
L1900_Eps.creer_classe('ECG2', 2)
L1900_Eps.creer_classe('AL1', 2)
L1900_Eps.creer_classe('AL2', 2)
# endregion
# region L6500_Ens_Arts_et_Arts_App
L6500_Ens_Arts_et_Arts_App = Matiere('L6500_Ens_Arts_et_Arts_App')
L6500_Ens_Arts_et_Arts_App.creer_classe('BTS1_COM', 5)
L6500_Ens_Arts_et_Arts_App.creer_classe('BTS2_COM', 5)
# endregion
# region L7100_Bioc_Genie_Biol
L7100_Bioc_Genie_Biol = Matiere('L7100_Bioc_Genie_Biol')
L7100_Bioc_Genie_Biol.creer_classe('2nd_Autres', 0.75)
L7100_Bioc_Genie_Biol.creer_classe('1eST2S', 7)
L7100_Bioc_Genie_Biol.creer_classe('TST2S', 8)
# endregion
# region L7300_SC_et_Tech_Medico
L7300_SC_et_Tech_Medico = Matiere('L7300_SC_et_Tech_Medico')
L7300_SC_et_Tech_Medico.creer_classe('2nd_Autres', 0.75)
L7300_SC_et_Tech_Medico.creer_classe('1eST2S', 13)
L7300_SC_et_Tech_Medico.creer_classe('TST2S', 13)
# endregion
# region L8011_Eco_Gest_AD_Grh
L8011_Eco_Gest_AD_Grh = Matiere('L8011_Eco_Gest_AD_Grh')
L8011_Eco_Gest_AD_Grh.creer_classe('1eSTMG', 14)
L8011_Eco_Gest_AD_Grh.creer_classe('TSTMG', 14)
L8011_Eco_Gest_AD_Grh.creer_classe('BTS1_SAM', 54.38)
L8011_Eco_Gest_AD_Grh.creer_classe('BTS2_SAM', 54.38)
# endregion
# region L8012_Eco_Gest_Comp_Fin
L8012_Eco_Gest_Comp_Fin = Matiere('L8012_Eco_Gest_Comp_Fin')
L8012_Eco_Gest_Comp_Fin.creer_classe('1eSTMG', 5)
L8012_Eco_Gest_Comp_Fin.creer_classe('TSTMG', 7)
L8012_Eco_Gest_Comp_Fin.creer_classe('BTS1_SAM', 38.75)
L8012_Eco_Gest_Comp_Fin.creer_classe('BTS2_SAM', 38.75)
# endregion
# region L8013_Eco_Gest_Cm
L8013_Eco_Gest_Cm = Matiere('L8013_Eco_Gest_Cm')
L8013_Eco_Gest_Cm.creer_classe('2nd_Autres', 1.5)
L8013_Eco_Gest_Cm.creer_classe('BTS1_MCO', 35)
L8013_Eco_Gest_Cm.creer_classe('BTS2_MCO', 35)
# endregion
# region L8014_Communication
L8014_Communication = Matiere('L8014_Communication')
L8014_Communication.creer_classe('BTS1_COM', 21.3)
L8014_Communication.creer_classe('BTS2_COM', 21.3)
# endregion

# Créer chaque Prof

# J = Prof('Jean', 10)
# L0426_Espagnol.Classes['2GT1'].assigner_prof(J, 2)
# print(L0426_Espagnol.Classes['2GT1'].assignments)
# print(L0426_Espagnol.Classes['2GT1'].heures_attribues)
# print(L0426_Espagnol.Classes['2GT1'].heures_totales)