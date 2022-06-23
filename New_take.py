import pandas as pd

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
        _data[element] = [0 for i in range(len(_classes))]
    return _data


def change_classes_per_subject(_classe, _subject, value):
    global subjects_df
    subjects_df.at[_classe, _subject] = value


def create_profs_df():
    data = {'Total_Hours': [], 'Assigned_Hours': [], 'Sup': [], 'Subject': []}
    return data


def add_new_prof( name, hours, sup, _subject):
    global profs_df
    profs_df.loc[name] = [hours, 0, sup, _subject]


def initialize_assignment():
    global CLASSES
    _data = {}
    for classe in CLASSES:
        _data[classe] = []
    df = pd.DataFrame(_data)
    return df


def add_prof_to_subject(_subject, prof):
    global CLASSES
    _subject.loc[prof] = [0 for x in range(len(CLASSES))]


def assign_hour(_subject, classe, prof, hours):
    global profs_df
    _subject.at[prof, classe] = hours
    profs_df.at[prof, 'Assigned_Hours'] += hours


# initialisation
d = create_classes_df(CLASSES, SUBJECTS)
subjects_df = pd.DataFrame(d, index=CLASSES)

p = create_profs_df()
profs_df = pd.DataFrame(p)

subject = initialize_assignment()

# dummy manipulation

# affect a class to a subject
change_classes_per_subject('2GT2', 'L0100_PHILOSOPHIE', 3)

# create a new prof
add_new_prof('Jean', 10, 3, 'L0100_PHILOSOPHIE')

# assign a prof to a class
add_prof_to_subject(subject, 'Jean')
assign_hour(subject, '2GT2', 'Jean', 4)

print(subject)
