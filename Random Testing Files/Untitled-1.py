class create_form:
    pupils = []
    teachers = []
    subjects = []
    number_of_pupils = 0
    number_of_teachers = 0

    def __init__(self, name):
        self.name = name


    @classmethod
    def add_pupil(cls, pupil_name):
        cls.pupils.append(pupil_name)
        cls.number_of_pupils += 1

    @classmethod
    def add_teacher(cls, teacher_name):
        cls.teachers.append(teacher_name)
        cls.number_of_teachers += 1

    @classmethod
    def add_subjects(cls, *args):
        any(cls.subjects.append(x) for x in args)




form1 = create_form("form1")

for i in range(0, 5):
    form1.add_pupil(f"joshua{i}")

form1.add_teacher("smith")
form1.add_teacher("jonas")

form1.add_subjects("maths", "chemistry", "biology", "physics")


print(form1.name, form1.number_of_pupils, form1.number_of_teachers, form1.pupils, form1.teachers, form1.subjects)





    
