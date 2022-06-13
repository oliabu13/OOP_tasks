class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def __str__(self):
        sum_grades = 1
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for key in self.grades:
            sum_grades += len(self.grades[key])
        self.average_rating = sum(map(sum, self.grades.values())) / sum_grades
        return f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_rating}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнение некорректно')
            return
        return self.average_rating < other.average_rating

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):
        grades_count = 0
        for key in self.grades:
            grades_count += len(self.grades[key])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        return f'''Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {self.average_rating}'''

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение некорректно')
            return
        return self.average_rating > other.average_rating

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
      return f'Имя: {self.name}\nФамилия: {self.surname}'

student_1 = Student('Sam', 'Peterson', 'male')
student_1.finished_courses += ['Основы  Python', 'Git']
student_1.courses_in_progress += ['OOP in Python', 'Python Advanced']

student_2 = Student('Lily', 'Collins', 'female')
student_2.finished_courses += ['Основы  Python', 'Git']
student_2.courses_in_progress += ['Python Advanced', 'OOP in Python']

mentor_1 = Mentor('Some', 'Buddy')
mentor_2 = Mentor('Another', 'Buddy')

lecturer_1 = Lecturer('Oleg', 'Buligin')
lecturer_1.courses_attached += ['Основы  Python', 'Python Advanced']
lecturer_2 = Lecturer('Kate', 'Lock')
lecturer_2.courses_attached += ['OOP in Python', 'Git']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Основы  Python']
reviewer_1.courses_attached += ['Python Advanced']
reviewer_2 = Reviewer('Jack', 'Smith')
reviewer_2.courses_attached += ['OOP in Python']
reviewer_2.courses_attached += ['Git']

student_1.rate_hw(lecturer_1, 'Основы  Python', 10)
student_1.rate_hw(lecturer_1, 'Python Advanced', 9)
student_1.rate_hw(lecturer_2, 'OOP in Python', 7)
student_1.rate_hw(lecturer_2, 'Git', 6)

student_2.rate_hw(lecturer_1, 'Основы  Python', 8)
student_2.rate_hw(lecturer_1, 'Python Advanced', 7)
student_2.rate_hw(lecturer_2, 'OOP in Python', 7)
student_2.rate_hw(lecturer_2, 'Git', 5)

reviewer_1.rate_hw(student_1, 'Основы  Python', 8)
reviewer_1.rate_hw(student_1, 'Git', 7)

reviewer_2.rate_hw(student_2, 'Основы  Python', 10)
reviewer_2.rate_hw(student_2, 'Git', 5)

print(f'Список студентов:\n{student_1}\n{student_2}')
print()
print(f'Список лекторов:\n{lecturer_1}\n{lecturer_2}')
print()

print(f''' Результат сравнения студентов:
{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}''')
print()

print(f'''Результат сравнения лекторов:
{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 > lecturer_2}''')
print()

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]

def all_student_average(student_list, course_name):
    sum_all = 0
    count_all = 1
    for student in student_list:
       if student.courses_in_progress == [course_name]:
            sum_all += student.average_rating
            count_all += 1
    average = sum_all / count_all
    return average

def all_lecture_average(lecturer_list, course_name):
    sum_all = 0
    count_all = 1
    for lecture in lecturer_list:
        if lecture.courses_attached == [course_name]:
            sum_all += lecture.average_rating
            count_all += 1
    average= sum_all / count_all
    return average

print(f"""Средняя оценка для студентов по курсу {'Основы  Python'}: 
{all_student_average(student_list, 'Основы  Python')}""")
print()

print(f"Средняя оценка для лекторов по курсу {'Python'}: {all_lecture_average(lecturer_list, 'Python')}")
print()