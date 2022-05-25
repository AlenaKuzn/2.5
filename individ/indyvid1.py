#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Вариант 3

if __name__ == '__main__':
    # Ввести кортеж одной строкой.
    A = tuple(map(int, input().split()))
    col = 0
    # Проверить количество элементов кортежа.
    if len(A) != 25:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)

    # Ищем количество элементов равные 5
    for i in A:
        if abs(i) == 5:
            col += 1

    print(col)
