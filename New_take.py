import pandas as pd
import os.path

# region CONST
# classes
CLASSES = ['2GT1', '2GT2', '2GT3', '2GT4', '2GT5', '2GT6', '2GT7', '2GT8', '2GT9', '2GT10', '2GT11', '2nd_Options', '2nd_Autres',
           '1eGT1', '1eGT2', '1eGT3', '1eGT4', '1eGT5', '1eGT6', '1eGT7', '1eGT8', '1eGT9', '1ere_Spécialirés', '1ere_Autres', '1ere_ST2S', '1ere_STMG',
           'TG1', 'TG2', 'TG3', 'TG4', 'TG5', 'TG6', 'TG7', 'TG8', 'Term_Spécialités', 'Term_Autres', 'TST2S', 'TSTMG',
           'BTS1_COM', 'BTS2_COM', 'BTS1_MCO', 'BTS2_MCO', 'BTS1_SAM', 'BTS2_SAM', 'BTS1_CG', 'BTS2_CG', 'ECG1', 'ECG2', 'AL1', 'AL2']

# subjects
SUBJECTS = ['L0100_PHILOSOPHIE', 'L0201_LETT_CLASS', 'L0202_LETT_MOD', 'L0421_ALLEMAND', 'L0422_ANGLAIS', 'L0426_ESPAGNOL', 'L0449_CREOLE', 'L0433_PORTUGAIS',
            'L1000_HIT_GEO', 'L1100_SC_ECO_SOC', 'L1300_MATH', 'L1500_PHYS_CHIM', 'NSI',
            'L1600_SVT', 'L1800_ARTS_PLASTIQUES', 'L6500_ENS_ART_ARTS_APP', 'L7100_BIOC_GENIE_BIOL', 'L7300_SC_TECH_MEDICO', 'L8012_ECO_GEST_COMP_FIN',
            'L8013_ECO_GEST_CM', 'L8014_COMMUNICATION']

# endregion


def create_classes_df(_classes, _subjects):
    _data = {}
    for element in _subjects:
        _data[element] = [0.0 for i in range(len(_classes))]
    return _data


def change_classes_per_subject(_classe, _subject, value):
    global SUBJECTS_DF
    SUBJECTS_DF.at[_classe, _subject] = value


def create_profs_df():
    data = {'Total_Hours': [], 'Assigned_Hours': [], 'Sup': [], 'Subject': []}
    return data


def add_new_prof(name, hours, sup, _subject):
    global PROFS_DF
    PROFS_DF.loc[name] = [hours, 0.0, sup, _subject]
    s = match_names(str(_subject))
    add_prof_to_subject(s, name)


def initialize_assignment(_name):
    global CLASSES, subjects
    _file = 'Data/{}_out.csv'.format(str(_name))

    if os.path.exists(_file):
        file = pd.read_csv(_file, index_col=0)

    else:
        _data = {}

        for classe in CLASSES:
            _data[classe] = []
        file = pd.DataFrame(_data)
        subjects[_name] = file

    return file



def add_prof_to_subject(_subject, prof):
    global CLASSES
    _subject.loc[prof] = [0.0 for x in range(len(CLASSES))]


def assign_hour(_subject, classe, prof, hours):
    global PROFS_DF
    _subject.at[prof, classe] = hours
    PROFS_DF.at[prof, 'Assigned_Hours'] += hours


def save_to_csv(_data, _filename):
    _data.to_csv(_filename, index=True)
    print('successfully saved to ' + _filename)


def load_from_csv(_filename):
    _data = pd.read_csv(_filename, index_col=0)
    return _data


def init_subjects_df():
    if os.path.exists('Data/subjects_df_out.csv'):
        file = pd.read_csv('Data/subjects_df_out.csv', index_col=0)
    else:
        d = create_classes_df(CLASSES, SUBJECTS)
        file = pd.DataFrame(d, index=CLASSES)
    return file


def init_profs_df():
    if os.path.exists('Data/profs_df_out.csv'):
        file = pd.read_csv('Data/profs_df_out.csv', index_col=0)
    else:
        p = create_profs_df()
        file = pd.DataFrame(p)
    return file


def override_profs_df():
    global PROFS_DF
    p = create_profs_df()
    PROFS_DF = pd.DataFrame(p)


# initialisation
SUBJECTS_DF = init_subjects_df()
PROFS_DF = init_profs_df()


subjects = {}
L0100_PHILOSOPHIE = initialize_assignment('L0100_PHILOSOPHIE')
L0201_LETT_CLASS = initialize_assignment('L0201_LETT_CLASS')
L0202_LETT_MOD = initialize_assignment('L0202_LETT_MOD')
L0421_ALLEMAND = initialize_assignment('L0421_ALLEMAND')
L0422_ANGLAIS = initialize_assignment('L0422_ANGLAIS')
L0426_ESPAGNOL = initialize_assignment('L0426_ESPAGNOL')
L0449_CREOLE = initialize_assignment('L0449_CREOLE')
L0433_PORTUGAIS = initialize_assignment('L0433_PORTUGAIS')
L1000_HIT_GEO = initialize_assignment('L1000_HIT_GEO')
L1100_SC_ECO_SOC = initialize_assignment('L1100_SC_ECO_SOC')
L1300_MATH = initialize_assignment('L1300_MATH')
L1500_PHYS_CHIM = initialize_assignment('L1500_PHYS_CHIM')
NSI = initialize_assignment('NSI')
L1600_SVT = initialize_assignment('L1600_SVT')
L1800_ARTS_PLASTIQUES = initialize_assignment('L1800_ARTS_PLASTIQUES')
L6500_ENS_ART_ARTS_APP = initialize_assignment('L6500_ENS_ART_ARTS_APP')
L7100_BIOC_GENIE_BIOL = initialize_assignment('L7100_BIOC_GENIE_BIOL')
L7300_SC_TECH_MEDICO = initialize_assignment('L7300_SC_TECH_MEDICO')
L8012_ECO_GEST_COMP_FIN = initialize_assignment('L8012_ECO_GEST_COMP_FIN')
L8013_ECO_GEST_CM = initialize_assignment('L8013_ECO_GEST_CM')
L8014_COMMUNICATION = initialize_assignment('L8014_COMMUNICATION')


def match_names(_subject_name):
    global L0100_PHILOSOPHIE, L0201_LETT_CLASS, L0202_LETT_MOD, L0421_ALLEMAND, L0422_ANGLAIS, L0426_ESPAGNOL, L0449_CREOLE
    global L0433_PORTUGAIS, L1000_HIT_GEO, L1100_SC_ECO_SOC, L1300_MATH, L1500_PHYS_CHIM, NSI, L1600_SVT, L1800_ARTS_PLASTIQUES
    global L6500_ENS_ART_ARTS_APP, L7100_BIOC_GENIE_BIOL, L7300_SC_TECH_MEDICO, L8012_ECO_GEST_COMP_FIN, L8013_ECO_GEST_CM, L8014_COMMUNICATION

    if(_subject_name == 'L0100_PHILOSOPHIE'):
        return L0100_PHILOSOPHIE
    elif(_subject_name == 'L0201_LETT_CLASS'):
        return L0201_LETT_CLASS
    elif (_subject_name == 'L0202_LETT_MOD'):
        return L0202_LETT_MOD
    elif (_subject_name == 'L0421_ALLEMAND'):
        return L0421_ALLEMAND
    elif (_subject_name == 'L0422_ANGLAIS'):
        return L0422_ANGLAIS
    elif (_subject_name == 'L0426_ESPAGNOL'):
        return L0426_ESPAGNOL
    elif (_subject_name == 'L0449_CREOLE'):
        return L0449_CREOLE
    elif (_subject_name == 'L0433_PORTUGAIS'):
        return L0433_PORTUGAIS
    elif (_subject_name == 'L1000_HIT_GEO'):
        return L1000_HIT_GEO
    elif (_subject_name == 'L1100_SC_ECO_SOC'):
        return L1100_SC_ECO_SOC
    elif (_subject_name == 'L1300_MATH'):
        return L1300_MATH
    elif (_subject_name == 'L1500_PHYS_CHIM'):
        return L1500_PHYS_CHIM
    elif (_subject_name == 'NSI'):
        return NSI
    elif (_subject_name == 'L1600_SVT'):
        return L1600_SVT
    elif (_subject_name == 'L1800_ARTS_PLASTIQUES'):
        return L1800_ARTS_PLASTIQUES
    elif (_subject_name == 'L6500_ENS_ART_ARTS_APP'):
        return L6500_ENS_ART_ARTS_APP
    elif (_subject_name == 'L7100_BIOC_GENIE_BIOL'):
        return L7100_BIOC_GENIE_BIOL
    elif (_subject_name == 'L7300_SC_TECH_MEDICO'):
        return L7300_SC_TECH_MEDICO
    elif (_subject_name == 'L8012_ECO_GEST_COMP_FIN'):
        return L8012_ECO_GEST_COMP_FIN
    elif (_subject_name == 'L8013_ECO_GEST_CM'):
        return L8013_ECO_GEST_CM
    elif (_subject_name == 'L8014_COMMUNICATION'):
        return L8014_COMMUNICATION


def save_all_subjects():
    global subjects
    for element in subjects:
        save_to_csv(subjects[element], 'Data/{}_out.csv'.format(str(element)))




# dummy manipulation

# affect a class to a subject
# change_classes_per_subject('2GT2', 'L0100_PHILOSOPHIE', 3)
#
# # create a new prof
# add_new_prof('Jean', 10, 3, 'L0100_PHILOSOPHIE')
#
# # assign a prof to a class
# add_prof_to_subject(L0100_PHILOSOPHIE, 'Jean')
# assign_hour(L0100_PHILOSOPHIE, '2GT2', 'Jean', 3)
#

# save_to_csv(profs_df, 'Data/profs_df_out.csv')

# print(SUBJECTS_DF)
# SUBJECTS_DF.iloc[0, 20] = 1
# print(L0421_ALLEMAND)
# print(SUBJECTS_DF.iloc[0])
# print(SUBJECTS_DF['L0100_PHILOSOPHIE'].where(SUBJECTS_DF['L0100_PHILOSOPHIE'] > 0).dropna())
# print(SUBJECTS_DF['L0100_PHILOSOPHIE'].iloc[0])
# print(PROFS_DF.where(PROFS_DF['Subject'] == 'L0100_PHILOSOPHIE'))
# print(L0100_PHILOSOPHIE.at['Jean', '2GT1'])
# print(L0100_PHILOSOPHIE.iloc[0,0])

# add_new_prof('Jean',10,0,'NSI')


# print(NSI.head())
# a = {'NSI' : L0201_LETT_CLASS}
# keys = [k for k, v in subjects.items() if v is L0201_LETT_CLASS]
# print(keys)
# for k, v in a.items():
#     print(k)
# print(subjects)
# for element in subjects:
#     print(subjects[element])
# save_all_subjects()
