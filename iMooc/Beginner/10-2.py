d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    red = score < 60 and ' style="color:red"' or ''
    return '<tr><td>%s</td><td%s>%s</td></tr>' % (name, red, score)

tds = [generate_tr(name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'