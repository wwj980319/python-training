class Student(object):
    def __init__(self, name, age, grade):
        # 让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
        # 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        self.__name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.age

    def get_grade(self):
        return self.grade

    def set_name(self, name):
        self.__name = name

    def set_grade(self, grade):
        self.grade = grade

    def set_age(self, age):
        self.age = age

    def get_level(self):
        if self.grade >= 90:
            return 'A'
        elif 60 <= self.grade < 90:
            return 'B'
        else:
            return 'C'