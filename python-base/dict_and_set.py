if __name__ == '__main__':
    # dict
    student_scores = {'wwj': 100, 'ysm': 100}

    # 根据key获取value
    wwj_score = student_scores['wwj']
    ysm_score = student_scores.get('ysm') # 如果key不存在，可以返回None
    ysm_score1 = student_scores.get('ysm', -1) # 如果key不存在，可以返回自己指定的value
    print(wwj_score)

    # 添加新key / 更新已有key的值
    student_scores['xff'] = 98
    print(student_scores)

    # 添加新key / 更新已有key的值
    student_scores.update({'wnq': 99})
    print(student_scores)

    # key存在则赋值，key不存在则新建key
    student_scores.setdefault('xxx', 99)
    print(student_scores)

    # 删除key
    student_scores.pop('xxx')
    print(student_scores)

    # 判断 key 是否在 dict 中
    if 'wwj' in student_scores:
        print(student_scores['wwj'])

    # 拿到所有 (key, value) 对，遍历 dict 的标准写法
    print(list(student_scores.items()))
    print(list(student_scores.keys()))
    print(list(student_scores.values()))

    """
    dict 和 list 比较:
        查找和插入的速度极快，不会随着key的增加而变慢；
        需要占用大量的内存，内存浪费多。
    而 list 相反:
        查找和插入的时间随着元素的增加而增加；
        占用空间小，浪费内存很少。
    所以，dict是用空间来换取时间的一种方法，dict可以用在需要高速查找的很多地方
    """

    # set
    courses = {1, 2, 2, 3}
    print(courses) # set 去重，只打印一个 2

    # 判断值是否在set中
    if 2 in courses:
        print('2 is in courses')

    # 去重
    fruits = ['apple', 'apple', 'banana', 'orange']
    print(set(fruits))

    s = set() # 创建空集合，⚠️ {}是空字典不是空集合
    s.add(4)  # 添加单个元素
    s.update([5, 6])  # 批量添加
    s.remove(6)  # 删除元素，不存在会报错
    s.discard(99) # 删除，不存在不报错
    print(s)

    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    print("并集:", set1 & set2)
    print("交集:", set1 | set2)
    print("差集:", set1 - set2)
    print("差集:", set2 - set1)






