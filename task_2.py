#Задача 2
#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
#второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

str=[2, 3, 4, 5, 6]
str_2=[]
if len(str)%2==0:
    for i in range (len(str)//2):
        str_2.append(str[i]*str[-i-1])
    print (str_2)
else:
    for i in range (len(str)//2):
        str_2.append(str[i]*str[-i-1])
    str_2.append(str[i+1]*str[i+1])
    print (str_2)
