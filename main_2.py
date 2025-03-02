start, end = map(int, input().split())

assert start < end, "Укажите корректный диапазон"
max_attempt: int = 7

attempt: int = 0
answers: tuple[str, ...] = ("угадал", "больше", "меньше")

while attempt < max_attempt:
    middle: int = (start + end) // 2
    # TODO: надо обработать вывод,
    #  чтобы не выводилось предполагаемое число
    print(middle)

    ans: str = input()
    if ans not in answers:
        print("Возможные ответы,", answers)
        continue

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
