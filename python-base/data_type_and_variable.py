if __name__ == '__main__':
    print(" I\'m \"OK\" ")
    print("\n 123") # \n 表示换行
    print("123 \t 456")  # \t 表示制表符
    print("789 \t 000")  # \t 表示制表符
    print("\\") # 字符\本身也要转义，所以\\表示的字符就是\
    print("\n")

    a = True

    if a:
        print("True")
    elif not a:
        print("False")