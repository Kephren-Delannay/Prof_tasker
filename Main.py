class Prof:
    Nom = ""
    heures = 0
    heures_max = 0
    heures_sup = 0

    def __init__(self, _nom, _heures_max):
        self.Nom = _nom
        self.heures_max = _heures_max


class Cls:
    label = ""
    heures_totales = 0
    heures_attribues = 0

    def __init__(self, _label, _heures_totales):
        self.label = _label
        self.heures_totales = _heures_totales
        self.heures_attribues = 0


class Matiere:
    Profs = {}
    Classes = {}

    def __init__(self):
        self.Profs = {}
        self.Classes = {}

    def assigner_prof(self, _classe, _prof, _heures):
        self.Profs[_prof.Nom] = _heures
        _prof.heures += _heures
        self.Classes[_classe].heures_attribues += _heures

    def creer_classe(self, nom, heures_totales):
        cl = Cls(nom, heures_totales)
        self.Classes[cl.label] = cl


# SVT = Matiere()
# J = Prof('jeanine', 0, 0)
# SVT.creer_classe('2GT1', 4.5)
# SVT.assigner_prof('2GT1', J, 2)
#
# print(J.heures)
# print(SVT.Classes['2GT1'].heures_attribues)

# Creer chaque matière
L1100_Sc_Eco_Soc = Matiere()
L1300_Math = Matiere()
L1500_Phys_Chim = Matiere()
NSI = Matiere()
L1600_SVT = Matiere()
L1800_Arts_Plastiques = Matiere()
L1900_Eps = Matiere()
L6500_Ens_Arts_et_Arts_App = Matiere()
L7100_Bioc_Genie_Biol = Matiere()
L7300_SC_et_Tech_Medico = Matiere()
L8011_Eco_Gest_AD_Grh = Matiere()
L8012_Eco_Gest_Comp_Fin = Matiere()
L8013_Eco_Gest_Cm = Matiere()
L8014_Communication = Matiere()

# Attribuer chaque classe

# region L0100_Philosophie

L0100_Philosophie = Matiere()
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
L0201_Lett_Class = Matiere()
L0201_Lett_Class.creer_classe('2nd_Options', 3)
L0201_Lett_Class.creer_classe('1ere_Autres', 3)
L0201_Lett_Class.creer_classe('term_Spécialités', 6)
L0201_Lett_Class.creer_classe('AL1', 13)
L0201_Lett_Class.creer_classe('AL2', 12)
# endregion
# region L0202_Lett_Mod
L0202_Lett_Mod = Matiere()
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
L0421_Allemand = Matiere()
L0421_Allemand.creer_classe('1eGT9', 2)
# endregion
# region L0422_Anglais
L0422_Anglais = Matiere()
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
L0426_Espagnol = Matiere()
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
L0449_Creole = Matiere()
L0449_Creole.creer_classe('2nd_Options', 3)
L0449_Creole.creer_classe('1ere_Autres', 3)

# endregion
# region L0433_Portugais
L0433_Portugais = Matiere()
L0433_Portugais.creer_classe('2nd_Options', 3)
L0433_Portugais.creer_classe('1ere_Autres', 3)

# endregion
# region L1000_Hit_Geo
L1000_Hit_Geo = Matiere()
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