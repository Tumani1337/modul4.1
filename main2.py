import math

def check_triangle_exists(a:float ,b: float,c: float) -> None:

    if not ((a + b > c) and (a + c > b) and (b + c > a)):
        raise ValueError('Треугольник не существует')

def is_positive(a:float ,b: float,c: float) -> None:

    if not(a > 0 and b > 0 and c > 0):
        raise ValueError('Стороны треугольника должны быть положительными')

def input_data() -> tuple[float,float,float]:

    print("Введите длины сторон треугольника a, b и c:")
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))

    is_positive(a,b,c)
    check_triangle_exists(a, b, c)

    return a,b,c

def calculating_half_meter(a:float ,b: float,c: float) -> float:
    return (a + b + c) / 2
