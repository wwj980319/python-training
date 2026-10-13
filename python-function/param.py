# 由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来
def calc(*numbers):
    return sum(*numbers)

def person(name, age, **kw):
    print("name:", name, "age:", age, "other:", kw)

def city(city_list = []):
    city_list.append('default')
    print(city_list)

if __name__ == '__main__':
    # nums = (1, 2, 3, 4, 5)
    # print(calc(nums))
    # person('wwj', 28, city='yangzhou')

    # `[]` 是可变对象（list），定义函数时就创建好了这一个列表，之后每一次不传参调用，都复用**同一个列表对象**，而不是新空列表。
    city()
    city()
