def check_correct_choice(choice: int) -> int:

    while choice not in [1,2]:
        choice = int(input('>>>'))

    return choice
