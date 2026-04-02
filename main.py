from itertools import product

print('Вариант 1')

def f1():
    alph = 'ТИМОФЕЙ'
    count = 0;
    combs = list(product(alph, repeat=5))
    for n in combs:
        if (n.count('Й') <= 1) and (n[0] != 'Й') and (n[-1] != 'Й') and (n.count('ИЙ') == 0) and (n.count('ЙИ') == 0):
            count += 1
    return count

print(f'Выполнение 1-ого задания: {f1()}')

def f2():
    x = 4**2020 + 2**2017 - 15
    b = bin(x)[2:]
    return b.count('1')

print(f'Выполнение 2-ого задания: {f2()}')

def get_divisors(n):
    divisors = []
    for i in range(2, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

def f3():
    for n in range(174457, 174506):
        divs = get_divisors(n)
        if len(divs) == 2:
            divs.sort()
            print(f'{divs[0]} {divs[1]}')

print(f'Выполнение 3-ого задания:')
f3()