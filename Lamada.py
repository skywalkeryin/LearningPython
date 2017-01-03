# lambda

list=[]
list.append(1)
list.append(2)
print(list)


def log(func):
    def wrapper(*args,**kw):
        print('call %s():' %func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now():
    print('2015-3-25')
now()