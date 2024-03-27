import random
import requests
import time

def rand_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }

def run():
    print('Welcome to Pokemon Top Trumps!')
    time.sleep(1)
    my_pokemon = rand_pokemon()
    print('Your Pokemon: {}'.format(my_pokemon['name']))
    print('id: {}'.format(my_pokemon['id']))
    print('height: {}'.format(my_pokemon['height']))
    print('weight: {}'.format(my_pokemon['weight']))
    yn = input('Would you like to keep this pokemon, yes/no?')
    while yn == 'no':
        my_pokemon = rand_pokemon()
        print('Your Pokemon: {}'.format(my_pokemon['name']))
        print('id: {}'.format(my_pokemon['id']))
        print('height: {}'.format(my_pokemon['height']))
        print('weight: {}'.format(my_pokemon['weight']))
        time.sleep(1)
        yn = input('Would you like to keep this pokemon, yes/no?')
    time.sleep(1)
    stat_choice = input('Which stat do you choose? (id, height, weight) ')
    time.sleep(1)
    opponent_pokemon = rand_pokemon()
    print('Your opponent chose {}'.format(opponent_pokemon['name']))
    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]
    if my_stat > opponent_stat:
        print('Your stat: ', my_stat)
        print("Opponent's stat: ", opponent_stat)
        time.sleep(1)
        print('You Win')
    elif my_stat < opponent_stat:
        print('Your stat: ', my_stat)
        print("Opponent's stat: ", opponent_stat)
        time.sleep(1)
        print('Enemy Wins')
    else:
        print('Your stat: ', my_stat)
        print("Opponent's stat: ", opponent_stat)
        time.sleep(1)
        print("Draw")

run()
time.sleep(1)
play_again = input('Would you like to play again?')
while play_again == 'yes':
    run()
    play_again = input('Would you like to play again?')
print('Thank you for playing!')

