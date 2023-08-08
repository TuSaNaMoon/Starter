from random import *
from prettytable import PrettyTable
from tqdm import trange
from time import sleep
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pygame
from pygame import mixer
mixer.init()


music = pygame.mixer.music.load('D:\Music\Love Suggestions - My Kind of Night (1).mp3')
pygame.mixer.music.play(-1)
def random_question(list_questions: list)-> dict:
    """function for selecting random question"""
    question = choice(questions_list)
    if len(list_questions) == 0:
        print("Це останнє питання")
        return
    else:
        print(question)
        my_list = list(info[question])
        mytable = PrettyTable()
        mytable.add_row(my_list)
        mytable.field_names = ["Варіант А", "Варіант В", "Варіант С", "Варіант D"]
        table = mytable.get_string(fields=["Варіант А", "Варіант В", "Варіант С", "Варіант D"])
        print(table)
        return question



def answer_check(letter: str, question: str, money: int)-> int:
    """function for checking the answer and counting money"""
    for key in correct_answers:
        if key == question:
            answer = correct_answers[question][0]
            if letter == answer:
                money = money + money + 1000
                print("Вітаємо! Це вірна відповідь.")
                print(f'Ваш виграш складає {money} грн.')
                return money
            else:
                print(f'Нажаль, Ви програли. Ваш виграш складає {money} грн.')
                return


def print_clues():
    """function to display clues on the screen"""
    print("Підказки".center(90, "_"))
    clues_table = PrettyTable()
    clues_table.add_row(clues_list)
    clues_table.field_names = ['50/50', 'Дзвінок другу', 'Допомога залу']
    table_clues = clues_table.get_string(fields=['50/50', 'Дзвінок другу', 'Допомога залу'])
    print(table_clues)


def clues(clues_list: list, number_clue: str, counter: int, question: str):
    """function with three functions to call clues"""

    def fifty_fifty():
        nonlocal question
        position_list = []
        j = correct_answers[question][1]
        for i in info[question]:
            if i == j:
                position_list.append(i)
            elif (len(position_list)) < 3:
                i = ' '
                position_list.append(i)
            elif position_list.count(' ') == 2:
                position_list.append(i)
        fifty_fifty_table = PrettyTable()
        fifty_fifty_table.add_row(position_list)
        fifty_fifty_table.field_names = ['Варіант А', 'Варіант В', 'Варіант C', 'Варіант D']
        table_fifty_fifty = fifty_fifty_table.get_string(fields=['Варіант А', 'Варіант В', 'Варіант C', 'Варіант D'])
        print(table_fifty_fifty)
        return

    def call_to_friend():
        my_list = ['A', 'B', 'C', 'D']
        clue = choice(my_list)
        print(f'Ваш друг вважає, що вірна відповідь - це варіант {clue}.')
        return

    def hall_help():
        n = 4
        target = 100
        samples = [randrange(target + 1) for _ in range(n - 1)] + [0, target]
        samples.sort()
        probs_list = [b - a for a, b in zip(samples[:-1], samples[1:])]
        index = np.arange(4)
        plt.bar(index, probs_list)
        plt.xticks(index + 0.1, ['A', 'B', 'C', 'D'])
        plt.show()


    if number_clue:
        if number_clue == '1':
            if counter > 1:
                print("У Вас немає підказки '50/50'.")
            else:
                clues_list[0] = ' '
                fifty_fifty()
        elif number_clue == '2':
            if counter > 1:
                print("У Вас немає підказки 'Дзвінок другу'.")
            else:
                clues_list[1] = ' '
                call_to_friend()
        elif number_clue == '3':
            if counter > 1:
                print("У Вас немає підказки 'Допомога залу'.")
            else:
                clues_list[2] = ' '
                hall_help()


info = {
'Найдовше місто в Україні?': ['Київ', 'Дніпро', 'Кривий Ріг', 'Рівне'], \
'З якого року День Соборності - державне свято?':['1999', '2000', '1991', '2005'], \
'Запаси якої корисної копалини в Україні найбільші в світі?':['мідь', 'ртуть', 'марганець', 'алюміній'],\
'Яке місце у світі посідає Україна за кількість осіб з вищою освітою?':['28', '4', '20', '12'],\
'Хто був першою олімпійською чемпіонкою незалежної України?' : ['Катерина Серебрянська',\
'Наталія Скакун', 'Оксана Баюл', 'Яна Клочкова'],\
'Хто з Київських князів називався "Тестем Європи"?' : ['Володимир Великий', 'Лев Данилович',\
'Ігор Рюрикович', 'Ярослав Мудрий'],\
'Яка станція метро в столиці України знаходиться на глибині 105 метрів і є найглибшою у світі?' :\
['Хрещатик', 'Арсенальна', 'Театральна', 'Університет']}

correct_answers = { 'Найдовше місто в Україні?' : ['C','Кривий Ріг'],\
    'З якого року День Соборності - державне свято?' : ['A', '1999'],\
    'Запаси якої корисної копалини в Україні найбільші в світі?': ['C', 'марганець'],\
    'Яке місце у світі посідає Україна за кількість осіб з вищою освітою?': ['B', '4'],\
    'Хто був першою олімпійською чемпіонкою незалежної України?' : ['C', 'Оксана Баюл'],\
    'Хто з Київських князів називався "Тестем Європи"?' : ['D', 'Ярослав Мудрий'],\
'Яка станція метро в столиці України знаходиться на глибині 105 метрів і є найглибшою у світі?' :\
['B', 'Арсенальна']}

clues_list = ['1', '2', '3']
your_money = 0
questions_list = list(info.keys())
counter1 = 0
counter2 = 0
counter3 = 0
#while True:
for question in range(len(info)):
    if questions_list != []:
        answer = random_question(questions_list)
        while True:
            your_answer = input("Граємо! Прочитайте питання і варіанти відповіді!"
            '\nВаша відповідь або Ви скористаєтесь підказкою? (відповідь або підказка): ')
            if your_answer not in ['відповідь', 'підказка']:
                print("Ви помилились. Спробуйте ще раз.")
            else:
                break
        if your_answer == 'відповідь':
            while True:
                your_letter = input("Оберіть літеру: ")
                if your_letter in ['A', 'B', 'C', 'D']:
                    money = answer_check(your_letter, answer, your_money)
                    questions_list.remove(answer)
                    if money:
                        your_money = money
                        break
                    else:
                        break
        if your_answer == 'підказка':
            print_clues()
            kind_clue = input("Виберіть підказку: ")
            if kind_clue == '1':
                counter1 += 1
                clues(clues_list, kind_clue, counter1, answer)
                while True:
                    answer_fifty_fifty = input("Оберіть літеру: ")
                    if answer_fifty_fifty in ['A', 'B', 'C', 'D']:
                        money = answer_check(answer_fifty_fifty, answer, your_money)
                        questions_list.remove(answer)
                        if money:
                            your_money = money
                            break
                        else:
                            break
            elif kind_clue == '2':
                counter2 += 1
                clues(clues_list, kind_clue, counter2, answer)
                while True:
                    answer_call_to_friend = input("Оберіть літеру: ")
                    if answer_call_to_friend in ['A', 'B', 'C', 'D']:
                        money = answer_check(answer_call_to_friend, answer, your_money)
                        if money:
                            your_money = money
                            questions_list.remove(answer)
                            break
                        else:
                            break
            elif kind_clue == '3':
                counter3 += 1
                clues(clues_list, kind_clue, counter3, answer)
                while True:
                    answer_hall_help = input("Оберіть літеру: ")
                    if answer_hall_help in ['A', 'B', 'C', 'D']:
                        money = answer_check(answer_hall_help, answer, your_money)
                        if money:
                            your_money = money
                            questions_list.remove(answer)
                            break
                        else:
                            break
    else:
        print(f'Гру закінчено. Ваш виграш склав {money}грн')
        break
