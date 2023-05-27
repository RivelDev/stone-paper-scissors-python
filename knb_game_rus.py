#Камень, ножницы, бумага

import time
import random
from getpass import getpass

print('Игра <<Камень ножницы бумага>>!')
time.sleep(2)
print('Правила игры: Только один конечный результат. Камень бьет ножницы, которые бьют бумагу, которая бьет камень. Ни один из предметов не является доминантным над всеми другими. Каждая игра заканчивается явным победителем и проигравшим, а в случае страшной ничьей — мгновенным реваншем.')
time.sleep(5)

start = int(input('Начать игру? [1 - Да|2 - Нет]: '))

if start == 1:
    start_ai_human = int(input('Вы будете играть с другом или с компьютером? [1 - Друг|2 - Компьютер]: '))
    if start_ai_human == 1:
        player1 = int(getpass('Игрок 1 выберает предмет: 1 - Камень, 2 - ножницы, 3 - бумага: '))
        player2 = int(getpass('Игрок 2 выберает предмет: 1 - Камень, 2 - ножницы, 3 - бумага: '))
        time.sleep(3)
        print('Камень!...')
        time.sleep(1)
        print('Ножницы!...')
        time.sleep(1)
        print('Бумага!...')
        time.sleep(1)
        print('Раз!...')
        time.sleep(1)
        print('Два!...')
        time.sleep(1)
        print('Три!')
        time.sleep(0.5)
        print('---------------------------')
        if player1 == 1:
            player1 = 'Камень'
        elif player1 == 2:
            player1 = 'Ножницы'
        elif player1 == 3:
            player1 = 'Бумага'
        if player2 == 1:
            player2 = 'Камень'
        elif player2 == 2:
            player2 = 'Ножницы'
        elif player2 == 3:
            player2 = 'Бумага'
        print(f'Игрок 1 выбрал {player1}')
        print(f'Игрок 2 выбрал {player2}')
        if player1 == 'Ножницы':
            if player2 == 'Бумага':
                print('Игрок 1 победил!')
        elif player1 == 'Бумага':
            if player2 == 'Ножницы':
                print('Игрок 2 победил!')
        elif player1 == 'Камень':
            if player2 == 'Ножницы':
                print('Игрок 1 победил!')
        elif player2 == 'Ножницы':
            if player2 == 'Камень':
                print('Игрок 2 победил!')
        elif player1 == 'Камень':
            if player2 == 'Бумага':
                print('Игрок 2 победил!')
        elif player2 == 'Бумага':
            if player1 == 'Камень':
                print('Игрок 1 победил!')   

#

    elif start_ai_human == 2:
        choice_ai = ['Камень', 'Ножницы', 'Бумага']
        player = int(input('Выберите предмет: 1 - Камень, 2 - ножницы, 3 - бумага: '))
        ai = random.choice(choice_ai)
        time.sleep(3)
        print('Камень!...')
        time.sleep(1)
        print('Ножницы!...')
        time.sleep(1)
        print('Бумага!...')
        time.sleep(1)
        print('Раз!...')
        time.sleep(1)
        print('Два!...')
        time.sleep(1)
        print('Три!')
        time.sleep(0.5)
        print('---------------------------')
        if player == 1:
            player = 'Камень'
        elif player == 2:
            player = 'Ножницы'
        elif player == 3:
            player = 'Бумага'
        print(f'Игрок выбрал {player}')
        print(f'ИИ выбрал {ai}')
        if player == 'Ножницы':
            if ai == 'Бумага':
                print('Игрок победил!')
        elif player == 'Бумага':
            if ai == 'Ножницы':
                print('ИИ победил!')
        elif player == 'Камень':
            if ai == 'Ножницы':
                print('Игрок победил!')
        elif ai == 'Ножницы':
            if ai == 'Камень':
                print('ИИ победил!')
        elif player == 'Камень':
            if ai == 'Бумага':
                print('ИИ победил!')
        elif ai == 'Бумага':
            if player == 'Камень':
                print('Игрок победил!')
        