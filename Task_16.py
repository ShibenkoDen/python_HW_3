"""
Задача 16. Требуется вычислить, сколько раз встречается некоторое число Х в массиве A[1...N].
Пользователь в первой строке вводит натуральное число N - количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
"""

N = int(input("Введите количество элементов в массиве: "))
list_1 = [i for i in range(1,N+1)]
find_number = int(input("Введите искомое число: "))
count = 0
for j in range(0, N): 
    if list_1[j] == find_number:
        count += 1
print (list_1)
print (f'' "искомое число ", find_number)
print (f'' "встречается ", count, " раз")
