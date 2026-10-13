# 由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来
def calc(*numbers):
    return sum(*numbers)

def person(name, age, **kw):
    print("name:", name, "age:", age, "other:", kw)

if __name__ == '__main__':
    nums = (1, 2, 3, 4, 5)
    print(calc(nums))

    person('wwj', 28, city='yangzhou')
