import math

def check_triangle_exists(a:float ,b: float,c: float) -> None:

    while ((a + b > c) and (a + c > b) and (b + c > a)):
        print('Треугольник не существует')
        a = float(input('a>> '))
        b = float(input('b>> '))
        c = float(input('c>> '))

def is_positive(a:float ,b: float,c: float) -> None:

    while (a > 0 and b > 0 and c > 0):
        print('Стороны треугольника должны быть положительными')
        a = float(input('a>> '))
        b = float(input('b>> '))
        c = float(input('c>> '))

