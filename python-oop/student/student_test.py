from student import Student

if __name__ == '__main__':
    wwj = Student('wwj', 28, 100)
    print(wwj.get_name()) # 不能直接用 wwj.name 访问，会报错没有 name 这个属性
    print(wwj.age)
    print(wwj.grade)
    print(wwj.get_level())

    wwj.set_name('wwj1')
    wwj.set_age(29)
    wwj.set_grade(89)
    print(wwj.age)
    print(wwj.grade)
    print(wwj.get_level())


