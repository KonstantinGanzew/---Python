''' Программа принимает на вход три символа через пробел в одну строку. Необходимо вывести код каждого символа при помощи функции ord в определенном формате.'''

a, b, c = map(str, input().split())

print('Simvol code', a, 'is', str(ord(a)) + '.')
print('Simvol code', b, 'is', str(ord(b)) + '.')
print('Simvol code', c, 'is', str(ord(c)) + '.')
