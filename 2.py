# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


from random import randint
import random


def enter_candy(amount):
    while True:
        number = input(amount)
        if 0 < int(number) < 29:
            break
        else:
            print('Введены некорректные данные')
    return int(number)


def player_move(name, amount, bot):
    if bot:
        if amount <= 28:
            am = amount
        else:
            am = amount % 29 if amount % 29 != 0 else random.randint(1, 28)
        amount -= am
        print(f'{name} взял {am} конфет')
    else:
        player = int(enter_candy(f'{name}, Ваш ход, сколько будете брать? '))
        amount -= player
    return amount


def game_move(candy_amount, bot):
    name1 = input('Имя первого игрока - ')
    name2 = input('Имя второго игрока - ') if not bot else 'Bot'
    first_step = random.randint(0, 1)
    if first_step == 0:
        print(f'Ходит {name1} ')
        flag = True
    else:
        print(f'Ход игрока {name2} ')
        flag = False
    flag = not flag

    while candy_amount > 0:
        flag = not flag
        candy_amount = player_move(
            name1, candy_amount, False) if flag else player_move(name2, candy_amount, bot)
        print(f'Осталось {candy_amount} конфет') if candy_amount > 0 else print(
            'Конфет не осталось')
    print(f'Победил {name1}!') if flag else print(f'Победил {name2}!')
    return


candy = 200
run = True
while run:
    mode = input('1 - игра с компьютером \n2 - игра в два игрока \n')
    bot = True if mode == '1' else False
    game_move(candy, bot)
    end = input('Еще партию? Y/N ')
    run = True if end.lower() == 'y' else False