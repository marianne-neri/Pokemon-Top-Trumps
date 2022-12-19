import random
import requests

user_score = 0
opponent_score = 0
play_game = True

while play_game:

    def random_pokemon():
        pokemon_number = random.randint(1, 151)
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
        response = requests.get(url)
        pokemon = response.json()
        return {
            'name': pokemon['name'].capitalize(),
            'attack': pokemon['stats'][1]['base_stat'],
            'defense': pokemon['stats'][2]['base_stat'],
            'speed': pokemon['stats'][5]['base_stat'],
        }


    def pick_stat(user_chosen_pokemon):

        user_stat_list = ['attack', 'defense', 'speed']
        stat_choice = input(f"Which of {user_chosen_pokemon}'s stats do you want to use? "
                            f"(Attack, Defense or Speed): ").lower()
        while stat_choice not in user_stat_list:
            stat_choice = input("Oops, you selected an invalid stat! "
                                "Please select either Attack, Defense or Speed: ").lower()
        return stat_choice


    print(f"\n~~~~ Welcome to Pokemon Top Trumps Game! ~~~~")
    user_name = input(f"\nWhat is your name? ").capitalize()

    random_pokemon_1 = random_pokemon()
    random_pokemon_2 = random_pokemon()

    pokemon_user_selected = input(
        f"Hey {user_name}, please select your Pokemon! "
        f"\n{random_pokemon_1['name']} or {random_pokemon_2['name']} : ").capitalize()

    while True:
        if pokemon_user_selected == random_pokemon_1['name']:
            stat_user_selected = pick_stat(pokemon_user_selected)
            user_stat_value = random_pokemon_1[stat_user_selected]
            print(f"You selected {pokemon_user_selected}: {stat_user_selected} = {user_stat_value}")
            break

        elif pokemon_user_selected == random_pokemon_2['name']:
            stat_user_selected = pick_stat(pokemon_user_selected)
            user_stat_value = random_pokemon_2[stat_user_selected]
            print(f"You selected {pokemon_user_selected}: {stat_user_selected} = {user_stat_value}")
            break

        else:
            pokemon_user_selected = input(f"Oops, you selected an invalid pokemon! "
                                      f"Please select either {random_pokemon_1['name']} "
                                      f"or {random_pokemon_2['name']} : ").capitalize()

    opponent_pokemon = random_pokemon()
    opponent_stat_value = opponent_pokemon[stat_user_selected]
    print(f"The opponent chose {opponent_pokemon['name']}: {stat_user_selected} = {opponent_stat_value}")

    if user_stat_value > opponent_stat_value:
        print('You Win!')
    elif user_stat_value < opponent_stat_value:
        print('You Lose!')
    else:
        print('Draw!')

    play_again = input("Play again? (Yes or No): ")
    if play_again.capitalize() != 'Yes':
        play_game = False
        print("Thanks for playing!")
