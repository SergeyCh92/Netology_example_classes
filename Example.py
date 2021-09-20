class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def evaluation(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and (
                course in self.courses_in_progress or
                self.finished_courses):
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]

    def unpack(self, course):
        list_course = ''
        for num, val in enumerate(course, start=1):
            if num != len(course):
                list_course += val + ', '
            else:
                list_course += val
        return list_course

    def calculating_average(self):
        average_grade = []
        if self.grades:
            for i in self.grades.values():
                average_grade.append(sum(i) / len(i))
            average_grade = sum(average_grade) / len(average_grade)
        else:
            average_grade = 'Студенту пока не выставлено ни одной оценки!'
        return average_grade

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не является студентом!')
            return
        print(self.calculating_average() < other.calculating_average())
        return

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Не является студентом!')
            return
        print(self.calculating_average() == other.calculating_average())
        return

    def __str__(self):
        data = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.calculating_average()}\n'
        data += f'Курсы в процессе изучения: {self.unpack(self.courses_in_progress)}\nЗавершенные курсы: ' \
            f'{self.unpack(self.finished_courses)}'
        return data


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}

    def calculating_average(self):
        average_grade = []
        if self.lecturer_grades:
            for i in self.lecturer_grades.values():
                average_grade.append(sum(i) / len(i))
            average_grade = sum(average_grade) / len(average_grade)
        else:
            average_grade = 'Преподавателю пока не выставлено ни одной оценки!'
        return average_grade

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не является лектором!')
            return
        print(self.calculating_average() < other.calculating_average())
        return

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Не является лектором!')
            return
        print(self.calculating_average() == other.calculating_average())
        return

    def __str__(self):
        data = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.calculating_average()}'
        return data


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress or course in student.finished_courses:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        data = f'Имя: {self.name}\nФамилия: {self.surname}'
        return data

def calc_grades_student (list_student, course):
    grade = []
    val = ''
    for i in list_student:
        if course in i.grades:
            for k in i.grades:
                if k == course:
                    val = sum(i.grades[k]) / len(i.grades[k])
                    grade.append(val)
                    break
        else:
            print(f'Студент {i} пока не имеет ни одной оценки за курс {course}!')
            return
    grade = sum(grade) / len(grade)
    print(f'Средний балл студентов за курс {course} - {grade}!')

def calc_grades_lecturers (list_lecturers, course):
    grade = []
    val = ''
    for i in list_lecturers:
        if course in i.lecturer_grades:
            for k in i.lecturer_grades:
                if k == course:
                    val = sum(i.lecturer_grades[k]) / len(i.lecturer_grades[k])
                    grade.append(val)
                    break
        else:
            print(f'Лектор {i} пока не имеет ни одной оценки за курс {course}!')
            return
    grade = sum(grade) / len(grade)
    print(f'Средний балл лекторов за курс {course} - {grade}!')

olga = Student('olga', 'koroleva', 'w')
semen = Student('semen', 'ivanov', 'm')
igor = Lecturer('igor', 'popov')
olesya = Lecturer('olesya', 'pupkina')
denis = Reviewer('denis', 'gorohov')
anna = Reviewer('anna', 'denisova')

olga.finished_courses.append('основы python')
olga.courses_in_progress.append('git')
semen.courses_in_progress.append('основы python')
semen.finished_courses.append('git')

igor.courses_attached.append('основы python')
igor.courses_attached.append('git')
olesya.courses_attached.append('основы python')
olesya.courses_attached.append('git')

denis.courses_attached.append('основы python')
denis.courses_attached.append('git')
anna.courses_attached.append('основы python')
anna.courses_attached.append('git')

olga.evaluation(igor, 'git', 9)
semen.evaluation(igor, 'git', 9)
semen.evaluation(olesya, 'git', 2)
semen.evaluation(olesya, 'git', 1)

denis.rate_hw(olga, 'git', 7)
denis.rate_hw(olga, 'git', 2)
denis.rate_hw(olga, 'основы python', 6)
denis.rate_hw(semen, 'основы python', 7)
denis.rate_hw(semen, 'основы python', 10)
anna.rate_hw(semen, 'git', 6)

igor > olesya
semen < olga

print(semen)
print(olga)
calc_grades_student([semen, olga], 'основы python')
calc_grades_lecturers([igor, olesya], 'git')