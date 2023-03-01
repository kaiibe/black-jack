import random
from main import clear_terminal
from black_jack import *


def create_new_deck_of_cards() -> list:
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 'J', 'K', 'Q', 'A'] * 4
    random.shuffle(deck)
    return deck


def launch():

    is_playing_game = True
    choice = input(
        "If you want to take a sit, type 'Yes' or 'No'\n>  ").lower()

    if choice == "no":
        is_playing_game = False

    while is_playing_game:
        try:
            player_balance = int(
                input("For how much money you want to buy chips: $"))
            break
        except:
            print("Invalid input, try again!")

    while is_playing_game:
        clear_terminal()
        print("Welcome to Black Jack!")
        print(f"Your current balance is: ${player_balance}")
        while True:
            while True:
                try:
                    bet = int(input("How much chips you want to bet: $"))
                    break
                except:
                    print("Invalid input, try again!")
            if bet > player_balance:
                print(f"You don't have {bet} ships to bet, try again!")
                continue
            break

        deck = create_new_deck_of_cards()

        round = Black_Jack( player_balance, bet, deck)

        is_black_jack = round.check_black_jack(
            round.player_value, round.dealer_value)

        if is_black_jack != 'No':
            player_balance += is_black_jack
            print(f"Your current balance: {player_balance} \n")

            choice = input(
                "Do you want to play another game? (Yes/No) \n> ").lower()
            if choice == 'no':
                break
            else:
                continue

        round.print_cards()

        while True:
            next_move = round.print_player_moves()

            if next_move == 'stand':
                round.dealer_get_card()
                result = round.end_round()
                if result == 'win':
                    player_balance += bet
                elif result == 'lose':
                    player_balance -= bet
                break

            elif next_move == "hit":
                round.player_get_card()
                if round.player_value > 21:
                    round.bust_cards()
                    player_balance -= bet
                    break 
                elif round.player_value == 21:
                    round.dealer_get_card()
                    result = round.end_round()
                    if result == 'win':
                        player_balance += bet
                    elif result == 'lose':
                        player_balance -= bet
                    break
                round.print_cards()

            elif next_move == "double":
                round.player_get_card()
                if round.player_value > 21:
                    round.bust_cards()
                    player_balance -= bet * 2
                    break

                round.dealer_get_card()
                result = round.end_round()

                if result == 'win':
                    player_balance += bet * 2
                elif result == 'lose':
                    player_balance -= bet * 2
                break
            
            else:
                print("\nInvalid input, try again!\n")

        print(f"Your current balance is: {player_balance}")
        if player_balance == 0:
            deposit_more = input(
                "You are out of money, do you want to deposit some more? (Yes/No) \n> ").lower()
            if deposit_more == 'yes':
                while True:
                    try:
                        player_balance = int(
                            input("For how much money you want to buy chips: $"))
                        clear_terminal()
                        print(f"Your current balance now: ${player_balance}")
                        break
                    except:
                        print("Invalid input, try again!")
            else:
                break

        choice = input(
            "Do you want to play another game? (Yes/No) \n> ").lower()
        if choice == 'no':
            is_playing_game = False
