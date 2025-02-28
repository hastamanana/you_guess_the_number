import random



user_range = input('Укажите диапазон через пробел: ').split()


try:
    nums = list(map(int, user_range))
    range_start = nums[0]
    range_end = nums[1]
except ValueError:
    print('Нужно ввести 2 числа через пробел')


attempts = 0

while attempts < 7:
    try:
        pc = random.randint(range_start, range_end)
    except ValueError:
        print('Ошибка! Похоже, вы дали противоречивые ответы.')
        break
    print(pc)
    answer = input('Число больше или меньше загаданного? Или число угадано?: ')
    if answer == 'угадал':
        print(f"Комп угадал. Загаданное число {pc}. Количество попыток: {attempts}")
        break
    if answer == 'больше':
        range_start = pc + 1
        attempts += 1
        continue
    if answer == 'меньше':
        range_end = pc - 1
        attempts += 1
        continue
else:
    print('Комп не отгадал число')


def main() -> None:
    pass


if __name__ == '__main__':
    main()