# Команды
# sort - метод списка
# sorted - встроенная функция
'''
a = [4, -10, 43, -300, 54, 89, -34]          # -> список
b = 'hello word'                             # -> строка
c = ('hi', 'zero', 'abracadabra', 'pikachu') # -> кортеж

a.sort()  # -> [-300, -34, -10, 4, 43, 54, 89]
print(a)  # -> Используем в списке(делает по возрастанию)

b = sorted(b) # -> [' ', 'd', 'e', 'h', 'l', 'l', 'o', 'o', 'r', 'w']
print(b)      
c = sorted(c, reverse=False) # -> ['abracadabra', 'hi', 'pikachu', 'zero']
print(c)                     # -> по возрастанию
c = sorted(c, reverse=True)  # -> ['zero', 'pikachu', 'hi', 'abracadabra']
print(c)                     # -> по убыванию
'''

# intersection - это встроенный метод, используемый для поиска пересечения 
# между заданными множествами.
'''
n = {5, 6, 11, 12, 18, 19}       # [12]
m = {7, 12, 13, 14, 17, 20}   
res = sorted(n.intersection(m))
print(res)
'''

