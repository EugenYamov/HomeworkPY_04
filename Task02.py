# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def factorization(n):
    factors = []
    divizor = 2
    while divizor <= n:
        if n % divizor == 0:
            factors.append(divizor)
            n = n / divizor
        else:
            divizor += 1

    print(f'Список множителей вашего числа: {factors}\n')

n = int(input('\nВведите число: '))
factorization(n)