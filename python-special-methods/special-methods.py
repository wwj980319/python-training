class Demo():
    def __init__(self):
        self.name = 'special methods'
        self.data = [1, 2, 3]

    def __str__(self):
        return f'the length of data is {len(self.data)}'

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, n):
        return self.data[n]

    def __getattr__(self, attr):
        if attr == 'data':
            return [1, 2, 3]
        return 'attr is not exist'

    def __call__(self, index):
        return self.data[index] * 2

if __name__ == '__main__':
    d = Demo()

    # str
    print(d)

    # iter
    for i in d:
        print(i)

    # getitem
    print(d[1])

    # getattr
    print(d.data)
    print(d.score)

    # call
    print(d(2))