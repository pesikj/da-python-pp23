from itertools import product
import random

def sort_function(value):
    colour = value[0]
    return {"H": 1/10, "T": 1/100, "C": 1/1000, "P": 1/10000}.get(colour) + int(value[1])


for x in range(10):
    colours = ["H", "T", "C", "P"]
    values = [str(i) for i in range(2, 10)]

    # Vytvoříme seznam všech karet
    cards = list(product(colours, values))

    all_players_cards = []

    for i in range(3):
        player_cards = []
        for j in range(5):
            index = random.randrange(len(cards))
            random_value = "".join(cards.pop(index))
            player_cards.append(random_value)
        player_cards = sorted(player_cards, key=sort_function)
        all_players_cards.append("-".join(player_cards))

    print(f'["{",".join(all_players_cards)}"]'.replace(",", '", "'), end=",\n")
