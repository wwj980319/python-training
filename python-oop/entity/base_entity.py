class BaseEntity():
    def __init__(self, height, weight, color):
        self.__height = height
        self.__weight = weight
        self.__color = color

    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__weight

    def get_color(self):
        return self.__color

    def set_height(self, height):
        self.__height = height

    def set_weight(self, weight):
        self.__weight = weight

    def set_color(self, color):
        self.__color = color