import pandas as pd
import os.path

# region CONST
# classes
CLASSES = ['2GT1', '2GT2', '2GT3', '2GT4', '2GT5', '2GT6', '2GT7', '2GT8', '2GT9', '2GT10', '2GT11', '2nd_Options', '2nd_Autres',
           '1eGT1', '1eGT2', '1eGT3', '1eGT4', '1eGT5', '1eGT6', '1eGT7', '1eGT8', '1eGT9', '1ere_Spécialités', '1ere_Autres', '1ere_ST2S', '1ere_STMG',
           'TG1', 'TG2', 'TG3', 'TG4', 'TG5', 'TG6', 'TG7', 'TG8', 'Term_Spécialités', 'Term_Autres', 'TST2S', 'TSTMG',
           'BTS1_COM', 'BTS2_COM', 'BTS1_MCO', 'BTS2_MCO', 'BTS1_SAM', 'BTS2_SAM', 'BTS1_CG', 'BTS2_CG', 'ECG1', 'ECG2', 'AL1', 'AL2']

# subjects
SUBJECTS = ['L0100_PHILOSOPHIE', 'L0201_LETT_CLASS', 'L0202_LETT_MOD', 'L0421_ALLEMAND', 'L0422_ANGLAIS', 'L0426_ESPAGNOL', 'L0449_CREOLE', 'L0433_PORTUGAIS',
            'L1000_HIT_GEO', 'L1100_SC_ECO_SOC', 'L1300_MATH', 'L1500_PHYS_CHIM', 'NSI',
            'L1600_SVT', 'L1800_ARTS_PLASTIQUES','L1900_EPS', 'L6500_ENS_ART_ARTS_APP', 'L7100_BIOC_GENIE_BIOL', 'L7300_SC_TECH_MEDICO', 'L8011_ECO_GEST_AD_GRH', 'L8012_ECO_GEST_COMP_FIN',
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
    # s = match_names(str(_subject))
    # add_prof_to_subject(_subject, name)


def init_assignments():
    if os.path.exists('Data/Assignments_out.csv'):
        assignments = pd.read_csv('Data/Assignments_out.csv', index_col=[0,1])
        print('Loaded file for assignments')
        # print(assignments)
    else:
        print('init Assignments')
        t = []
        for i in list(PROFS_DF.index):
            _t = (PROFS_DF.loc[i, 'Subject'], i)
            t.append(_t)

        multi = pd.MultiIndex.from_tuples(t)

        _data = {}
        for cl in CLASSES:
            _data[cl] = [0.0 for i in range(len(list(PROFS_DF.index)))]
        assignments = pd.DataFrame(_data, index=multi)

    return assignments


def add_prof_to_subject(_subject, prof):
    global CLASSES, ASSIGNMENTS
    # _subject.loc[prof] = [0.0 for x in range(len(CLASSES))]
    ASSIGNMENTS.loc[(_subject, prof), :] = [0.0 for i in range(50)]
    ASSIGNMENTS = ASSIGNMENTS.sort_index()


def remove_prof(_subject, _prof):
    global ASSIGNMENTS
    ASSIGNMENTS = ASSIGNMENTS.drop((_subject, _prof))



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
        print('loaded for profs')
    else:
        p = create_profs_df()
        file = pd.DataFrame(p)
    return file


def override_profs_df():
    global PROFS_DF
    p = create_profs_df()
    PROFS_DF = pd.DataFrame(p)

def set_hour(prof, amount):
    global PROFS_DF
    v = list(PROFS_DF.loc[prof])
    v[1] = amount
    PROFS_DF.loc[prof] = v

# initialisation
SUBJECTS_DF = init_subjects_df()
PROFS_DF = init_profs_df()
ASSIGNMENTS = init_assignments()

# print(ASSIGNMENTS)
# SUBJECTS_DF.loc['BTS1_COM']['L8013_ECO_GEST_CM'] = 0.0
# SUBJECTS_DF.loc['BTS1_COM']['L8014_COMMUNICATION'] = 21.3
# SUBJECTS_DF.loc['BTS2_COM']['L8013_ECO_GEST_CM'] = 0.0
# SUBJECTS_DF.loc['BTS2_COM']['L8014_COMMUNICATION'] = 21.3
#
# SUBJECTS_DF.loc['BTS1_MCO']['L8013_ECO_GEST_CM'] = 35.0
# SUBJECTS_DF.loc['BTS1_MCO']['L8014_COMMUNICATION'] = 0.0
# SUBJECTS_DF.loc['BTS2_MCO']['L8013_ECO_GEST_CM'] = 35.0
# SUBJECTS_DF.loc['BTS2_MCO']['L8014_COMMUNICATION'] = 0.0
#
# save_to_csv(SUBJECTS_DF, 'Data/Subjects_df_out_b.csv')