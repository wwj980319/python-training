if __name__ == '__main__':
    a = 'ABC' # 英文str, str是不可变的
    print(a)
    print(a.replace('A', 'a')) # 由于 str 不可变，所以这个操作是将变量 a 指向了 新的字符串 'aBC'

    b = b'ABC' # bytes类型的数据用带b前缀的单引号或双引号
    print(b)

    c = b'ABC'.decode('ascii') # 解码bytes类型，得到str
    print(c)

    d = '中文' # 中文str
    print(d)

    e = '中文'.encode('utf-8') # 中文str，可以用UTF-8编码为bytes
    print(e)

    f = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') #如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
    print(f)

    #
    # f = '中文'.encode('ascii')
    # print(f)