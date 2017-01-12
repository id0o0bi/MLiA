def average(*args):
    cnt = len(args)
    if (cnt == 0):
        return 0.0
    return round(sum(args) / float(cnt), 1)

print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)