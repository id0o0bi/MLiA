def count():
    fs = []
    for i in range(1, 4):
        def prod():
            def power():
                return i * i
            return power
        fs.append(prod)
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()