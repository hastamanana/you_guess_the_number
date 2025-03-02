import math


# добавил автоматическое определние мин. и макс. значений 
range_nums = list(map(int, input().split()))
start = min(range_nums)
end = max(range_nums)

assert start < end, "Укажите корректный диапазон"

# добавил кол-во попыток в зависимости от диапазона
all_nums_in_range = end - start
max_attempt: int = math.ceil(math.log(all_nums_in_range, 2)) + 1
# вывод кол-ва попыток для указанного диапазона (опционально)
print(max_attempt)

attempt: int = 0
answers: tuple[str, ...] = ("угадал", "больше", "меньше")

while attempt < max_attempt:
    middle: int = (start + end) // 2
    # TODO: надо обработать вывод,
    #  чтобы не выводилось предполагаемое число

    #todo сделал
    print(middle)
    ans: str = None
    while ans not in answers:
        ans: str = input()
        if ans not in answers:
            print("Возможные ответы:", answers)
            continue
    else:
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
