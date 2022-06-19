class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()
    def __str__(self):
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = round((sum(map(sum, self.grades.values())) / grades_count), 1)
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_rating}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __lt__(self, other):
        """Реализует сравнение через операторы '<,>' студентов между собой по средней оценке за домашние задания"""
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
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
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = round((sum(map(sum, self.grades.values())) / grades_count), 1)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating

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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

student_1 = Student('Sam', 'Peterson')
student_1.courses_in_progress += ['Основы Python']
student_1.finished_courses += ['Введение в программирование']
student_2 = Student('Lily', 'Collins')
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']
student_3 = Student('Chris', 'Frey')
student_3.courses_in_progress += ['Основы Python']
student_3.finished_courses += ['Введение в программирование']

lecturer_1 = Lecturer('Oleg', 'Buligin')
lecturer_1.courses_attached += ['Основы Python']
lecturer_2 = Lecturer('Kate', 'Lock')
lecturer_2.courses_attached += ['Git']
lecturer_3 = Lecturer('Sam', 'Green')
lecturer_3.courses_attached += ['Основы Python']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Основы Python']
reviewer_1.courses_attached += ['Git']
reviewer_2 = Reviewer('Ostap', 'Bender')
reviewer_2.courses_attached += ['Основы Python']
reviewer_2.courses_attached += ['Git']

student_1.rate_hw(lecturer_1, 'Основы Python', 9)
student_1.rate_hw(lecturer_1, 'Основы Python', 10)
student_1.rate_hw(lecturer_1, 'Основы Python', 10)
student_1.rate_hw(lecturer_2, 'Основы Python', 6)
student_1.rate_hw(lecturer_2, 'Основы Python', 8)
student_1.rate_hw(lecturer_2, 'Основы Python', 6)
student_1.rate_hw(lecturer_1, 'Основы Python', 9)
student_1.rate_hw(lecturer_1, 'Основы Python',10)
student_1.rate_hw(lecturer_1, 'Основы Python', 8)
student_2.rate_hw(lecturer_2, 'Git', 7)
student_2.rate_hw(lecturer_2, 'Git', 6)
student_2.rate_hw(lecturer_2, 'Git', 9)
student_3.rate_hw(lecturer_3, 'Основы Python', 8)
student_3.rate_hw(lecturer_3, 'Основы Python', 9)
student_3.rate_hw(lecturer_3, 'Основы Python', 10)

reviewer_1.rate_hw(student_1, 'Основы Python', 10)
reviewer_1.rate_hw(student_1, 'Основы Python', 8)
reviewer_1.rate_hw(student_1, 'Основы Python', 9)
reviewer_2.rate_hw(student_2, 'Git', 6)
reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_3, 'Основы Python', 8)
reviewer_2.rate_hw(student_3, 'Основы Python', 7)
reviewer_2.rate_hw(student_3, 'Основы Python', 9)
reviewer_2.rate_hw(student_3, 'Основы Python', 8)
reviewer_2.rate_hw(student_3, 'Основы Python', 7)
reviewer_2.rate_hw(student_3, 'Основы Python', 9)

print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()

print(f'Перечень лекторов:\n\n{lecturer_1}\n\n{lecturer_2}\n\n{lecturer_3}')
print()

print(f'''Результат сравнения студентов:
{student_1.name} {student_1.surname} и {student_2.name} {student_2.surname} = {student_1 > student_2}
{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}''')
print()

print(f'''Результат сравнения лекторов:
{lecturer_1.name} {lecturer_1.surname} и {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 > lecturer_2}
{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 > lecturer_2}''')
print()

student_list = [student_1, student_2, student_3]
lecturer_list = [lecturer_1, lecturer_2, lecturer_3]

def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for student in student_list:
       if student.courses_in_progress == [course_name]:
            sum_all += student.average_rating
            count_all += 1
    average = round((sum_all / count_all), 1)
    return average

def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lecture in lecturer_list:
        if lecture.courses_attached == [course_name]:
            sum_all += lecture.average_rating
            count_all += 1
    average = round((sum_all / count_all), 1)
    return average

print(f"Средняя оценка для всех студентов по курсу {'Основы Python'}: {student_rating(student_list, 'Основы Python')}")
print()

print(f"Средняя оценка для всех лекторов по курсу {'Основы Python'}: {lecturer_rating(lecturer_list, 'Основы Python')}")
print()