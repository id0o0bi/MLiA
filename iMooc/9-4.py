d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for k, v in d.iteritems():
    sum = sum + v
    print k + ':' + str(v)
print 'average', ':', sum / len(d)