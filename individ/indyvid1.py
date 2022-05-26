#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Вариант 3

if __name__ == '__main__':
    # Ввести кортеж одной строкой.
    A = tuple(map(int, input().split()))

    # Проверить количество элементов кортежа.
    if len(A) != 24:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)

    # Ищем количество элементов равные 5
    print("Количество элементов равных пяти: ", A.count(5))

