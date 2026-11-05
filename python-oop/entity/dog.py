from animal import Animal
from cat import Cat

class Dog(Animal):

    __slots__ = ('height', 'weight', 'color','breed') #不想让别人随意给实例加属性

    def __init__(self, height, weight, color, breed):
        super().__init__(height, weight, color)
        self.breed = breed

    def bark(self, breed):
        print(f'A {breed} is barking...')

if __name__ == '__main__':
    dogs_breed = 'matipool'
    dog = Dog(10, 10, 'white', dogs_breed)
    dog.bark(dog.breed)
    print(dir(dog))
    print('dog是否属于Dog类', isinstance(dog, Dog))
    print('dog是否属于Animal类', isinstance(dog, Animal))
    print('dog是否属于Cat类', isinstance(dog, Cat))
    print('dog是否有breed属性:', hasattr(dog, 'breed'))

    print('dog的breed属性是什么:' + dog.breed)
    print('dog的breed属性是什么:', getattr(dog, 'breed'))
