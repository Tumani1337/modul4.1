def check_correct_choice(choice: int) -> int:

    while choice not in [1,2]:
        choice = int(input('>>>'))

    return choice

def input_choice() -> int:

    print("Выберите опцию:")
    print("1. Конвертировать Цельсий в Фаренгейт")
    print("2. Конвертировать Фаренгейт в Цельсий")
    choice = int(input('>>>'))
    choice = check_correct_choice(choice)

    return choice