def count():
    fs = []
    for i in range(1, 4):
        def prod(j):
            def power():
                return j * j
            return power
        fs.append(prod(i))
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()