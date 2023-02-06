import random
import requests


play_game = True

while play_game:
    user_score = 0
    opponent_score = 0
    game_round = 1


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
        stat_choice = input(f"\nWhich of {user_chosen_pokemon}'s stats do you want to use? "
                            f"\n Attack [a], Defense [d] or Speed [s]: ").lower()
        while True:
            if stat_choice == 'a':
                stat_choice = 'attack'
                return stat_choice

            elif stat_choice == 'd':
                stat_choice = 'defense'
                return stat_choice

            elif stat_choice == 's':
                stat_choice = 'speed'
                return stat_choice

            else:
                stat_choice = input("\nOops, try again! (select a, s or d) "
                                    "\n Attack [a], Defense [d] or Speed [s]: ").lower()


    print(f"\n              Welcome to Pokemon Top Trumps Game!             ")
    print(f"\n ***| How to win: beat Kiwi (computer) and be the first to 3 points! |***")

    user_name = input(f"\nWhat is your name? ").capitalize()

    while user_score < 3 or opponent_score < 3:
        print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~ Round {game_round} ~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print(f"              | {user_name}: {user_score} |  vs  | Kiwi: {opponent_score} |\n")
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        random_pokemon_1 = random_pokemon()
        random_pokemon_2 = random_pokemon()

        pokemon_user_selected = input(
            f"Hey {user_name}, please select your Pokemon! (choose 1 or 2) "
            f"\n{random_pokemon_1['name']} [1] or {random_pokemon_2['name']} [2] : ")

        while True:
            if pokemon_user_selected == '1':
                pokemon_user_selected = random_pokemon_1['name']
                stat_user_selected = pick_stat(pokemon_user_selected)
                stat_user_value = random_pokemon_1[stat_user_selected]
                print(f"\nYou chose {pokemon_user_selected}: {stat_user_selected} = {stat_user_value}")
                break

            elif pokemon_user_selected == '2':
                pokemon_user_selected = random_pokemon_2['name']
                stat_user_selected = pick_stat(pokemon_user_selected)
                stat_user_value = random_pokemon_1[stat_user_selected]
                print(f"\nYou chose {pokemon_user_selected}: {stat_user_selected} = {stat_user_value}")
                break

            else:
                pokemon_user_selected = input(f"\nOops, you selected an invalid pokemon! "
                                          f"\nPlease select either {random_pokemon_1['name']} [1] "
                                          f"or {random_pokemon_2['name']} [2] : ")

        opponent_pokemon = random_pokemon()
        opponent_stat_value = opponent_pokemon[stat_user_selected]
        print(f"Kiwi chose {opponent_pokemon['name']}: {stat_user_selected} = {opponent_stat_value}")


        if stat_user_value > opponent_stat_value:
            print('Result = You Win!')
            user_score += 1
            game_round += 1

        elif stat_user_value < opponent_stat_value:
            print('Result = You Lose!')
            opponent_score += 1
            game_round += 1

        else:
            print('Result = Draw!')
            game_round += 1

        if user_score == 3:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"              | {user_name}: {user_score} |  vs  | Kiwi: {opponent_score} |\n")
            print(f"                THE WINNER IS: {user_name}!  ")
            print("                Congratulations! ")

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            break

        elif opponent_score == 3:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"              | {user_name}: {user_score} |  vs  | Kiwi: {opponent_score} |\n")
            print("                THE WINNER IS: Kiwi! ")
            print("                Better luck next time! ")

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            break

    play_again = input("\nPlay again? (Yes or No): ")
    if play_again.capitalize() != 'Yes':
        play_game = False
        print("Thanks for playing!")
