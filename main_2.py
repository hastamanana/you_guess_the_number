import math


def range_2_numbers() -> tuple[int,int]:
    while True:
        try:
            range_nums: list = list(map(int, input('Введите 2 неравных числа через пробел: ').split()))
            
        except ValueError:
            print('Нужно ввести 2 неравных числа через пробел! Попробуйте еще раз')
            continue

        else:

            if len(range_nums) != 2:
                print('Необходимо ввести ровно 2 числа через пробел. Попробуйте еще раз')
                continue
            
            if range_nums[0] == range_nums[1]:
                print('Числа должны быть неравными. Попробуйте еще раз.')
                continue

            if range_nums[0] < 1 or range_nums[1] < 1:
                print("Оба числа должны быть больше 0. Попробуйте еще раз")
                continue
                    
        return min(range_nums), max(range_nums)


def get_max_attempt_count(start_num, end_num) -> int:
    diff = end_num - start_num
    return int(math.log2(diff)) + 1


def game(start, end, max_attempt) -> None:
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
    start, end = range_2_numbers()
    max_attempt = get_max_attempt_count(start, end)
    game(start, end, max_attempt)


if __name__ == '__main__':
    main()