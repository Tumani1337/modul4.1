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



