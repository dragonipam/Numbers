import random
import os
record=10**6
while True:
    if record != 10**6:
        print("Ваш рекорд: " + str(record))
    print("Выберите сложность (Просто введите номер выбранного пункта)")
    print("1 - Легко (от 0 до 10)")
    print("2 - Нормально (от 0 до 100)")
    print("3 - Сложно (от 0 до 1000)")
    print("4 - Хардкор >=) (от 0 до 10000)")
    while True:
        try:
            choice=int(input("Ваш выбор: "))
            break
        except ValueError:
            print("Нужно ввести только НОМЕР выбранного пункта!")
            print("")
    difficult=10
    if choice == 2:
        print("Выбрана сложность - Нормально")
        print("Посмотрим на что ты способен...")
        difficult*=10
    elif choice == 3:
        print("Выбрана сложность - Сложно")
        print("А ты смельчак!) Удачи")
        difficult*=100
    elif choice == 4:
        print("Выбрана сложность - Хардкор")
        print("Моё почтение! Ты достоин уже за то, что решил попробовать!")
        difficult*=1000
    elif choice == 1:
        print("Выбрана сложность - Легко")
        print("Легковато как-то, может возьмешь планку повыше?")
    else:
        print("Вы ввели не существующий пункт... Поэтому мы выбрали за вас сложность: СУПЕРМЕГАХАРДКОР =) Попробуй угадай число от 0 до 1000000)))")
        difficult*=100000
    print("Программа загадала случайное число от 0 до " + str(difficult) + ", сможешь угадать?")
    print("")
    bot_number=random.randint(0, difficult)
    n=1
    while True:
        print("Попытка номер: " + str(n))
        try:
            user_number=int(input("Ваше число: "))
            n+=1
            if bot_number==user_number:
                print("Поздравляю, вы угадали число! Попыток потребовалось: " + str(n))
                break
            elif ((user_number > difficult) or (user_number < 0)):
                print("Необходимо вводить числа от 0 до " + str(difficult) + "!")
            else:
                if user_number > bot_number:
                    print("Число больше, чем загаданное!")
                elif user_number < bot_number:
                    print("Число меньше, чем загаданное!")
            print("")
        except ValueError:
            print("Разрешено вводить только цифры. ТЫ ИГРАЕШЬ В ИГРУ ЧИСЛА, ПРИКИДЫВАЕШЬ?!")
            print("")
    if record > n:
        record = n
        print("")
        print("У вас новый рекорд!")
        print("Ваш рекорд: " + str(record))
    elif n >=10**6:
        print("Ты вышел за установленные рамки рекорда, ты каким образом не угадал это число за миллион попыток???")
    print("")
    print("Хотите повторить? 1-да/2-нет")
    if input()!="1":
        break
    else:
        os.system('cls')
input("Спасибо за игру! Для выхода нажмите Enter...")
