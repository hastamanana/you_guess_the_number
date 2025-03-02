# Угадай число (отгадывает компьютер)

---

## Описание проекта:

**Угадай число** - игра, в которой пользователь должен загадать число, а программа угадать за определенное число попыток.

---

## Техническое задание:

1.  Пользователь вводит 2 числа через пробел. 1 число - нижняя граница диапазона, 2 число - верхняя граница диапазона.
2.  Компьютер выводит число.
    Если число больше загаданного, пользователь пишет: `больше`
    Если число меньше загаданного, пользователь пишет: `меньше`
    Если число угадано, пользователь пишет: `угадал`
3.  Максимальное число попыток - 7.
4.  Если программа не угадало число за 7 попыток, выводится сообщение `"Комп не отгадал число"`.
5.  Если пользователь дает неверные подсказки, то выводится сообщение `"Ошибка! Похоже, вы дали противоречивые ответы."`
6.  Если программа угадывает число, выводится сообщение `"Комп угадал. Загаданное число {X}. Количество попыток: {Y}"` (где Х - загаданное число, а Y - кол-во попыток)
7.  Программа должна корректно обрабатывать ввод некоректных данных (ввод строки, вместо 2 чисел)

---

## Автор 

[Telegram](https://t.me/ozornoy_gulyaka)