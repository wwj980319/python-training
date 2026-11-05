from base_entity import BaseEntity

class Animal(BaseEntity):

    def __init__(self, age, birth, height, weight, color):
        super().__init__(height, weight, color)
        self._age = age
        self.birth = birth

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('age must be an integer')
        if value < 0 or value > 200:
            raise TypeError('impossible age')
        self._age = value

    def run(self):
        print('Animal is running...')

if __name__ == '__main__':
    a = Animal(16, 319, 111, 222, 'blue')
    print(a.age)
    a.age = 18
    print(a.age)
    a.age = -1