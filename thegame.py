import random
import string

CAPITALS = {
    "Ukraine": "Kyiv",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "USA": "Washington",
    "Canada": "Ottawa",
    "Switzerland": "Bern",
    "Austria": "Vienna",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Denmark": "Copenhagen",
    "Finland": "Helsinki",
    "Poland": "Warsaw",
    "Romania": "Bucharest",
    "Bulgaria": "Sofia",
    "Greece": "Athens",
}

ctr_caps = list(CAPITALS.items())


def print_intro(lifes):
    print(" THE GAME ".center(50, "*"))
    print('"Try To Guess The Capital Of The Country!"'.center(50))
    print(50 * "*")
    print("If you want to quit the game, please enter 'exit'")
    print(f"Lifes: {lifes}")


def ask_usr(country):
    usr_data = input(f"What is a capital of {country}: ")
    return remove_symbols(usr_data)


def if_wrong(lifes, score, country, capital):
    try:
        letter = 1
        lifes -= 1
        while lifes != 0:
            print(f"Wrong! {letter} letter is '{capital[:letter]}'")
            display_lifes_left(lifes)
            letter += 1
            data = ask_usr(country)
            if data == "Exit":
                lifes = 0
                return lifes, score
            if data == capital:
                score += 1
                return lifes, score
            lifes -= 1
        print("No more lifes left!")
        return lifes, score
    except Exception as e:
        print(e)


def display_lifes_left(lifes):
    print(f"Lifes left: {lifes}")


def main(lifes, score, countries):
    while lifes != 0:
        pair = randomizer(countries)
        if not pair:
            return score
        ctr, caps = pair[0], pair[1]
        try:
            data = ask_usr(ctr)
            if data == "Exit":
                return score
            if data == caps:
                score += 1
            else:
                lifes, score = if_wrong(lifes, score, ctr, caps)
                if lifes == 0:
                    return score
            display_score(score)
        except Exception as e:
            print(e)
    return score


def randomizer(capitals_items: list) -> tuple:
    try:
        if not capitals_items:
            print("No capitals left!")
            return []
        country_capital = random.choice(capitals_items)
        capitals_items.remove(country_capital)
        return country_capital
    except UnboundLocalError as e:
        print(e)


def remove_symbols(usr_data):
    try:
        if not usr_data.isalpha():
            sumbols = string.punctuation, string.whitespace, string.digits
            symbols = str(sumbols)
            for symbol in symbols:
                usr_data = usr_data.replace(symbol, "")
        return usr_data.capitalize()
    except Exception as e:
        print(e)


def display_score(score):
    print(f"You are right! Current score: {score}")


start_lifes = 3
start_score = 0

print_intro(start_lifes)
final_score = main(start_lifes, start_score, ctr_caps)
print(f"Final score: {final_score}\nGame over!")
