#Получить математический пример с клавиатуры, вычислить
#Не понял как сделать это задание,поэтому потренировал цикл и исключения
print('Решить пример (7+7)*2')
l=input('Ваш ответ') 
try:
    l = int(l)
except ValueError: 
    print('Вы ввели не число')
while type(l) == str or l != 28:
    if l != 28:
        l = input('попробуйте снова.')
    try:
        l = int(l)
    except ValueError:
        print('Вы опять ввели не число')
print('молодец')