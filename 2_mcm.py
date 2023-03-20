'''
2. Escribir una función que calcule el mínimo común múltiplo entre dos números
'''

def mcm(a, b):
    if a > b:
        a, b = b, a
    multiplo_a = 1
    multiplo_b = 1
    while True:
        if a * multiplo_a < b * multiplo_b:
            multiplo_a += 1
            continue
        if a * multiplo_a == b * multiplo_b:
            break
        multiplo_b += 1
    return a * multiplo_a


if __name__ == '__main__':
    print('\n2. MCM')
    print(f'4 y 3: {mcm(2, 3)}')
    print(f'4 y 3: {mcm(4, 30)}')
