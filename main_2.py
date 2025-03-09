import math


def validate_nums(values: list[int]) -> list[int]:
    if len(values) != 2:
        raise ValueError('Необходимо ввести ровно 2 числа через пробел. Попробуйте еще раз')

    if values[0] == values[1]:
        raise ValueError('Числа должны быть неравными. Попробуйте еще раз.')

    if values[0] < 1 or values[1] < 1:
        raise ValueError('Оба числа должны быть больше 0. Попробуйте еще раз')

    return values


def get_input_range() -> list[int]:
    try:
        data = list(map(int, input('Введите 2 неравных числа через пробел: ').split()))
    except ValueError:
        raise ValueError('Нужно ввести 2 неравных целых числа через пробел!')
    return data


def get_range_two_numbers() -> tuple[int, int]:
    while True:
        try:
            range_nums = get_input_range()
            validate_nums(range_nums)
        except ValueError as err_msg:
            print(err_msg)
        else:
            start: int = min(range_nums)
            end: int = max(range_nums)
            return start, end


def get_max_attempt_count(start_num, end_num) -> int:
    diff = end_num - start_num
    return int(math.log2(diff)) + 1


def game(start: int, end: int, max_attempt: int) -> None:
    attempt: int = 0
    answers: tuple[str, ...] = ("угадал", "больше", "меньше")

    while attempt < max_attempt:
        middle: int = (start + end) // 2
        print(middle)

        ans: str = input()
        while ans not in answers:
            print("Возможные ответы:", answers)
            ans: str = input()

        attempt += 1

        if ans == "угадал":
            print(
                f"Я угадал! Загаданное число {middle}. "
                f"Количество попыток: {attempt}"
            )
            break

        if ans == "больше":
            start = middle + 1
        elif ans == "меньше":
            end = middle - 1

        if start > end:
            print("Ошибка! Похоже, вы дали противоречивые ответы.")
            break


def main() -> None:
    start, end = get_range_two_numbers()
    max_attempt = get_max_attempt_count(start, end)
    game(start, end, max_attempt)


if __name__ == '__main__':
    main()
