def toUppers(L):
    return [i.upper() for i in L if isinstance(i, str)]

print toUppers(['Hello', 'world', 101])