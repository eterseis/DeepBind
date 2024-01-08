def decorator(func):
    def wrapper():
        print('-' * 10)
        func()
        print('-' * 10)

    return wrapper()


@decorator
def oi():
    print('oi')
oi()

