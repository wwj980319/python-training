import math
def my_abs(x : int | float):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')

if __name__ == '__main__':
    my_abs(1.23)