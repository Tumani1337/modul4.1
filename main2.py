import math

def check_triangle_exists(a:float ,b: float,c: float) -> None:

    if not ((a + b > c) and (a + c > b) and (b + c > a)):
        raise ValueError('Треугольник не существует')

def is_positive(a:float ,b: float,c: float) -> None:

    if not(a > 0 and b > 0 and c > 0):
        raise ValueError('Стороны треугольника должны быть положительными')
