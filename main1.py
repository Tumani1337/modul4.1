import math

def check_zero_a(a: float) -> float:
   if a == 0:
        raise ZeroDivisionError('Коэфицент "a" не должен быть = 0')
   else:
       return a

def input_data() -> tuple[float,float,float]:
    print('Введите коэфиценты уравнения')
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

def output_data(roots: tuple[float] or float or None) -> None:

    if roots is None:
        print("У уравнения нет корней")

    elif isinstance(roots,tuple) and len(roots) == 2:
        print(f"Корни уравнения: {roots[0]} и {roots[1]}")

    elif isinstance(roots, float):
        print(f"Единственный корень уравнения: {roots}")

roots = calculate_quadratic_equation(*input_data())
output_data(roots)

