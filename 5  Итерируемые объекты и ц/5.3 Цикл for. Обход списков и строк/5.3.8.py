'''Напишите программу, которая находит рекордное количество вхождений (не обязательно подряд) символа в строку.'''

x=list(input().lower()) 
y=[]                     
for i in x:              
    y.append(x.count(i)) 
print(max(y))        
