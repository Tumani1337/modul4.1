import math

def check_zero_a(a: float) -> float:
    while a == 0:
        print('Коэфицент а не должен быть = 0')
        a = float(input("a >>"))
    return a

def input_data() -> tuple[float,float,float]:
    a = float(input("a >>"))
    a = check_zero_a(a)
    c = float(input("c >>"))
    b = float(input("b >>"))
    return a,b,c

def calculate_quadratic_equation(a:float,b:float,c:float) -> tuple[float,float] or float or None:
    discriminant = b * b - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2

    elif discriminant == 0:
        root = -b / (2 * a)
        return root

    else:
        return None

