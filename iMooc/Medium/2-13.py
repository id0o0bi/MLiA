import time

def performance(unit):
    def decorator(f):
        def wrapper(*args, **kw):
            t1 = time.time()
            res = f(*args, **kw)
            t2 = time.time()
            u = unit == 'ms' and 1000 or 1
            print 'call %s() in %f %s' % (f.__name__, (t2 - t1) * u, unit)
            return res
        return wrapper
    return decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)