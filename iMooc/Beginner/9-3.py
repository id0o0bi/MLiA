d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for num in d.itervalues():
    sum += num
print sum / len(d)