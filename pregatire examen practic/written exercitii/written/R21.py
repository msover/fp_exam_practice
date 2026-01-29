a = 1
b = [str(a), 1]
c = {a : a, str(b[1]) : b}
a = ['1', '2']
print(type(a) == type(c[1]))
print(str(a))