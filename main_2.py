import random


def random_num_from_pc(start, end) -> int:
    if range_two_numbers():
        return random.randint(start, end)
    
    
def range_two_numbers() -> tuple[int, int]:
    while True:
        user_range = input('Укажите диапазон через пробел: ').split()
        try:
            nums = list(map(int, user_range))

            if len(nums) != 2:
                raise ValueError("Должно быть введено 2 числа") 
            
            range_start = nums[0]
            range_end = nums[1]

            if range_start >= range_end:
                raise ValueError('1 число должно быть меньше 2')
            
            return range_start, range_end


        except ValueError as e:
            print(f'Ошибка:{e}')



def game() -> None: 
    attempts = 0
    while attempts < 7:

        try:
            pc = random_num_from_pc()
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
    if range_two_numbers():
        start_num, end_num = range_two_numbers()
        game()




if __name__ == '__main__':
    main()