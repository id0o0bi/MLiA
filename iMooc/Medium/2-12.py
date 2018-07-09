import time

def performance(f):
    def fn(x):
        t1 = time.time()
        res = f(x)
        t2 = time.time()
        print 'call ' + f.__name__ + '() in ' + str(t2 - t1)
        return res
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)