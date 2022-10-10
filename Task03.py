# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def unique_numbers(numbers):
    unique_list = []
    for i in numbers:
        if numbers.count(i) == 1:
            unique_list.append(i)
    return unique_list

numbers = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
print(unique_numbers(numbers))