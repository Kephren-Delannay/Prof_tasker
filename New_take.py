import pandas as pd
import os.path

# region CONST
# classes
CLASSES = ['2GT1', '2GT2', '2GT3', '2GT4', '2GT5', '2GT6', '2GT7', '2GT8', '2GT9', '2GT10', '2GT11', '2nd_Options', '2nd_Autres',
           '1eGT1', '1eGT2', '1eGT3', '1eGT4', '1eGT5', '1eGT6', '1eGT7', '1eGT8', '1eGT9', '1ere_Spécialirés', '1ere_Autres', '1ere_ST2S', '1ere_STMG',
           'TG1', 'TG2', 'TG3', 'TG4', 'TG5', 'TG6', 'TG7', 'TG8', 'Term_Spécialités', 'Term_Autres', 'TST2S', 'TSTMG',
           'BTS1_COM', 'BTS2_COM', 'BTS1_MCO', 'BTS2_MCO', 'BTS1_SAM', 'BTS2_SAM', 'BTS1_CG', 'BTS2_CG', 'ECG1', 'ECG2', 'AL1', 'AL2']

# subjects
SUBJECTS = ['L0100_PHILOSOPHIE', 'L0201_LETT CLASS', 'L0202_LETT MOD', 'L0421_ALLEMAND', 'L0422_ANGLAIS', 'L0426_ESPAGNOL', 'L0449_CREOLE', 'L0433_PORTUGAIS',
            'L1000_HIT GEO', 'L1100_SC ECO SOC', 'L1300_MATH', 'L1500_PHYS CHIM', 'NSI',
            'L1600_SVT', 'L1800_ARTS PLASTIQUES', 'L6500_ENS ART & ARTS APP', 'L7100_BIOC GENIE BIOL', 'L7300_SC & TECH MEDICO', 'L8012_ECO GEST COMP FIN',
            'L8013_ECO GEST CM', 'L8014_COMMUNICATION']

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


def add_new_prof( name, hours, sup, _subject):
    global PROFS_DF
    PROFS_DF.loc[name] = [hours, 0.0, sup, _subject]


def initialize_assignment():
    global CLASSES
    _data = {}
    for classe in CLASSES:
        _data[classe] = []
    df = pd.DataFrame(_data)
    return df


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
        print('loaded file for profs')
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


L0100_PHILOSOPHIE = initialize_assignment()
L0201_LETT_CLASS = initialize_assignment()
L0202_LETT_MOD = initialize_assignment()
L0421_ALLEMAND = initialize_assignment()
L0422_ANGLAIS = initialize_assignment()
L0426_ESPAGNOL = initialize_assignment()
L0449_CREOLE = initialize_assignment()
L0433_PORTUGAIS = initialize_assignment()
L1000_HIT_GEO = initialize_assignment()
L1100_SC_ECO_SOC = initialize_assignment()
L1300_MATH = initialize_assignment()
L1500_PHYS_CHIM = initialize_assignment()
NSI = initialize_assignment()
L1600_SVT = initialize_assignment()
L1800_ARTS_PLASTIQUES = initialize_assignment()
L6500_ENS_ART_ARTS_APP = initialize_assignment()
L7100_BIOC_GENIE_BIOL = initialize_assignment()
L7300_SC_TECH_MEDICO = initialize_assignment()
L8012_ECO_GEST_COMP_FIN = initialize_assignment()
L8013_ECO_GEST_CM = initialize_assignment()
L8014_COMMUNICATION = initialize_assignment()

# dummy manipulation

# affect a class to a subject
# change_classes_per_subject('2GT2', 'L0100_PHILOSOPHIE', 3)
#
# # create a new prof
add_new_prof('Jean', 10, 3, 'L0100_PHILOSOPHIE')
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
# print(SUBJECTS_DF['L0100_PHILOSOPHIE'])