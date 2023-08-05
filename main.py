class Name:
    def __init__(self, name):
        self.name = name

a = Name('Bob')
b = Name('Dry')
"""
a = [i for i in zip((a.name,b.name),('bil', 'rob'))]

for i in zip((a,b),('bil','rob')):
    i[0].name = i[1]
"""

lst = [a, b]
name = ['bil', 'rob']
for i, j in zip(lst, name):
    i.name = j

print(b.name)




