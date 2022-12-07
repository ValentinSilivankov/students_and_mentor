class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        sum_ratings = 0
        len_ratings = 0
        for course in self.grades.values():
            sum_ratings += sum(course)
            len_ratings += len(course)
        average_rating = round(sum_ratings / len_ratings, 2)
        return average_rating

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Преподователей и студентов между собой не сравнивают!')
            return
        return self.average_grade() < other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        sum_ratings = 0
        len_ratings = 0
        for course in self.grades.values():
            sum_ratings += sum(course)
            len_ratings += len(course)
        average_rating = round(sum_ratings / len_ratings, 2)
        return average_rating    

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating 
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Преподователей и студентов между собой не сравнивают!')
            return
        return self.average_grade() < other.average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res


student_1 = Student('Марк', 'Юрьевич', 'Муж')
student_1.courses_in_progress += ['Python', 'Git', 'Java']
student_1.finished_courses += ['Введение в програмирование', 'Компьютерная грамотность']
student_2 = Student('Ирина', 'Валерьевна', 'Жен')
student_2.courses_in_progress += ['Python', 'Java']
student_2.finished_courses += ['Введение в програмирование']


lecturer_1 = Lecturer('Олег', 'Сергеевич')
lecturer_1.courses_attached += ['Python', 'Java', 'Git']
lecturer_2 = Lecturer('Татьяна', 'Александровна')
lecturer_2.courses_attached += ['Python', 'Git']


reviewer_1 = Reviewer('Сергей', 'Владимирович')
reviewer_1.courses_attached += ['Python', 'Java', 'Git']
reviewer_2 = Reviewer('Ольга', 'Ивановна')
reviewer_2.courses_attached += ['Python', 'Java', 'Git']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 7)

reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 9)

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_1, 'Python', 6)

student_2.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 8)
student_2.rate_lecturer(lecturer_2, 'Python', 6)

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]


def average_rating_for_course(student_list, course):
    sum_rating = 0
    quantity_rating = 0
    for stud in student_list:
        for course in stud.grades:
            stud_sum_rating = stud.av_rating_for_course(course)
            sum_rating += stud_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 2)
    return average_rating


print(reviewer_1)
print(reviewer_2)
print(lecturer_1)
print(lecturer_2)
print(student_1)
print(student_2)


print(average_rating_for_course(student_list, 'Python'))
print(average_rating_for_course(lecturer_list, 'Python'))