'''Ване на день рождения подарили n кубиков. Он с друзьями решил построить из них пирамиду. Ваня хочет построить пирамиду следующим образом: на верхушке пирамиды должен находиться 1 кубик, на втором уровне — 1 + 2 = 3 кубика, на третьем — 1 + 2 + 3 = 6 кубиков, и так далее. Таким образом, на i-м уровне пирамиды должно располагаться 1 + 2 + ... + (i - 1) + i кубиков.



Ваня хочет узнать, пирамиду какой максимальной высоты он может создать с использованием имеющихся кубиков.'''

a = int(input())
b = 0
c = 0
s = 0
while a > s:
    c += 1
    b += c
    s += b
if a == s:
    print(c)
else:
    print(c-1)
