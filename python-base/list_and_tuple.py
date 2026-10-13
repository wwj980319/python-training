if __name__ == '__main__':
    numbers = [1,2,3]
    print(len(numbers))
    print(numbers[0])
    print(numbers)

    numbers.append(4)
    print(numbers)

    numbers.insert(4, 5)
    print(numbers)

    numbers.pop()
    print(numbers)

    numbers.pop(3)
    print(numbers)

    numbers.remove(1)
    print(numbers)

    p = ['c', 'c++']
    s = ['python', p, 'java']
    print(s)

    for i, num in enumerate(numbers):
        print(i, num)

    '''------------------------------------------------'''

    names = ('wwj', 'ysm', 'xff') # tuple一旦初始化就不能修改
    print(names)

    t = (1) # 定义的不是tuple，是1这个数！
    print(t)

    q = (1, ) # 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
    print(q)

    letters = ('a', 'b', ['X', 'Y']) #tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变
    letters[2][0] = 'A'
    letters[2][1] = 'B'
    print(letters)

