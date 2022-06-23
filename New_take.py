import pandas as pd

# dummy classes
CLASSES = ['2ndGT1', '2ndGT2', '2ndGT3', '2ndGT4', 'TG1', 'TG2', 'TG3', 'TG4']

# dummy subjects
SUBJECTS = ['Maths', 'SVT', 'Philosophie', 'Anglais']


def create_classes_df(_classes, _subjects):
    _data = {}
    for element in _subjects:
        _data[element] = [0 for i in range(len(_classes))]
    return _data


def change_classes_per_subject(classe, subject, value):
    global subjects_df
    subjects_df.at[classe, subject] = value


def create_profs_df():
    data = {'Total_Hours' : [], 'Assigned_Hours': [], 'Sup' : [], 'Subject' : []}
    return data


def add_new_prof( name, hours, sup, subject):
    global profs_df
    profs_df.loc[name] = [hours, 0, sup, subject]


def initialize_assignment():
    global CLASSES
    _data = {}
    for classe in CLASSES:
        _data[classe] = []
    df = pd.DataFrame(_data)
    return df


def add_prof_to_subject(subject, classes, prof):
    subject.loc[prof] = [0 for x in range(len(classes))]


def assign_hour( subject, classe, prof, hours):
    global profs_df
    subject.at[prof, classe] = hours
    profs_df.at[prof, 'Assigned_Hours'] += hours


# initialisation
d = create_classes_df(CLASSES, SUBJECTS)
subjects_df = pd.DataFrame(d, index=CLASSES)

p = create_profs_df()
profs_df = pd.DataFrame(p)

subject = initialize_assignment()

# dummy manipulation

# affect a class to a subject
change_classes_per_subject('2ndGT2', 'Philosophie', 3)

# create a new prof
add_new_prof('Jean', 10, 3, 'SVT')

# assign a prof to a class
add_prof_to_subject(subject, CLASSES, 'Jean')
assign_hour(subject, '2ndGT2', 'Jean', 4)

print(profs_df)
