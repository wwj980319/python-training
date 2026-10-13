import logging

def calc1():
    try:
        print('try...')
        r = 10 / 0
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    finally:
        print('finally...')
    print('end')

# 自定义error
class Calc2Error(Exception):
    print('divide by zero')

def calc2(dividend, divisor):
    if divisor == 0:
        raise Calc2Error

    return dividend / divisor

def calc(dividend, divisor):
    try:
        print('start to calculate...')
        r = calc2(dividend, divisor)
        print('result:', r)
    except Exception as e:
        # 打印错误信息日志
        logging.exception(e)
        print('we meet an error:', e)

    # finally 核心场景：资源释放
    #
    # - 打开文件 → 一定要关闭 `file.close()`
    # - 连接数据库 / Redis → 一定要关闭连接
    # - 加锁之后 → 一定要释放锁
    finally:
        print('finally...')

if __name__ == '__main__':
    # calc(10, 0)
    # calc1()
    calc2(10, 0)