from random import *
from colorama import *
from tqdm import tqdm
import csv
import chardet
import pyjokes
from prettytable import PrettyTable
import art

init(autoreset=True)


def game_stone():
    """function for game 'rock - scissors - paper'"""

    def random_choose():
        """function to return random value"""
        version = ['rock', 'paper', 'scissors']
        my_version = choice(version)
        return my_version

    my_version1 = random_choose()
    version = ['rock', 'scissors', 'paper']
    while True:
        respons = input(Fore.BLUE + "Let's play! (press 'enter'or write 'no'): ")
        if respons == 'no':
            break
        else:
            while True:
                your_version = input("Write rock, scissors or paper: ").strip()
                if your_version not in version:
                    print(Fore.RED + "You made a mistake, try again!")
                else:
                    break
            print(f'Your choice {your_version}', Fore.RED + 'VS', f"{my_version1}!")
            if (your_version == 'rock' and my_version1 == 'scissors')\
                    or (your_version == 'paper' and my_version1 == 'rock')\
                    or (your_version == 'scissors' and my_version1 == 'paper'):
                Art1 = art.text2art("Congratulations! You win!")
                print(Fore.YELLOW + Art1)
            if (your_version == 'rock' and my_version1 == 'paper')\
                    or (your_version == 'paper' and my_version1 == 'scissors')\
                    or (your_version == 'scissors' and my_version1 == 'rock'):
                Art2 = art.text2art("You lost!")
                print(Fore.YELLOW + Art2)
            if  your_version ==  my_version1:
                Art3 = art.text2art("Draw!")
                print(Fore.YELLOW + Art3)



def movie_recommendation(genre: str) -> list:
    """the function randomly selects 3 films and prints them in table"""
    list_films = []
    recommended_movies = []
    mytable = PrettyTable()
    mytable.field_names = ["Id", "Film (year)", "Genre"]
    with open('movies.csv', mode='rb') as file:
        for a in tqdm(list(file), desc='Loading…  '):
            data = file.read()
            result = chardet.detect(data)
            encoding = result['encoding']
    #print(encoding)
    with open("movies.csv", encoding='utf-8') as file:
        reader = csv.reader(file)
        for line in reader:
            for i in line:
                if i == genre_film:
                    list_films.append(line)
        recommended_movies = choices(list_films, k=3)
        mytable.add_rows(recommended_movies)
        table = mytable.get_string(fields=["Id", "Film (year)", "Genre"])
        print(table)

def music_recommendation(genre: str) -> list:
    """the function randomly selects song and prints it in table"""
    list_music = []
    mytable = PrettyTable()
    mytable.field_names = ["Track name", "Artist name", "Genre"]
    with open("musicset_file.csv", encoding = 'utf-8') as f:
        reader = csv.reader(f)
        for line in reader:
            for r in line:
                if r == genre_music:
                    list_music.append(line)
        recommended_music = choices(list_music)
        mytable.add_rows(recommended_music)
        table = mytable.get_string(fields=["Track name", "Artist name", "Genre"])
        print(table)

def games_recommendation(genre: str) -> list:
    """the function randomly selects 3 games and prints them in table"""
    list_games = []
    recommended_games = []
    mytable = PrettyTable()
    mytable.field_names = ["Name", "Genre", "Year"]
    with open("games_set.csv", encoding = 'utf-8') as f:
        reader = csv.reader(f)
        for line in reader:
            for r in line:
                if r == genre_game:
                    list_games.append(line)
        recommended_games = choices(list_games, k=3)
        mytable.add_rows(recommended_games)
        table = mytable.get_string(fields=["Name", "Genre", "Year"])
        print(table)



while True:
    menu_item = int(input("Hello! I'm Smile_bot! \N{slightly smiling face}I will make you smile.\
        \N{slightly smiling face}\n\t 1. Game.\n\t 2. Movie recommendation.\
        \n\t 3. Music recommendation. \n\t 4. Game recommendation. \n\t 5. Joke.\N{grinning face}\
        \n\t 6. Exit. \n Choose a menu item: "))
    if menu_item == 6:
        break
    elif menu_item == 1:
        game_stone()
    elif menu_item == 2:
        try:
            genre_film = input("Enter genre film (Action, Drama, Thriller, Comedy, Fantasy, Mystery,\
Crime, Romance, Animation, Documentary, Horror): ").capitalize()
            movie_recommendation(genre_film)
            print()
        except IndexError:
            print(Fore.CYAN + 'I do not know such a genre of film.')
    elif menu_item == 3:
        try:
            genre_music = input('Enter music genre:\n\t dance pop\n\t singer-songwriter pop\n\t alt z\
            \n\t orchestral soundtrack\n\t alternative metal\n\t glitchcore\n\t pop\n\t alt hip hop\
            \n\t filmi\n\t classick rock\n\t Your choice: ').lower()
            music_recommendation(genre_music)
            print()
        except IndexError:
            print(Fore.CYAN + 'Sorry, I do not know such a genre of music.')
    elif menu_item == 4:
        try:
            genre_game = input('Enter game genre:\n\t sports\n\t platform\n\t racing\
            \n\t role-playing\n\t puzzle\n\t misc\n\t shooter\n\t simulation\
            \n\t action\n\t fighting\n\t adventure\n\t Your choice: ').title()
            games_recommendation(genre_game)
            print()
        except IndexError:
            print(Fore.CYAN + 'Sorry, I do not know such a genre of game.')
    elif menu_item == 5:
        joke_for_you = pyjokes.get_joke(language='en', category='all')
        print()
        print(Fore.CYAN + joke_for_you)
        print()

