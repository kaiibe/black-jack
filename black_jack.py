from main import clear_terminal

class Black_Jack:
    def __init__(self, bet: int, deck: list) -> None:
        self.bet = bet
        self.deck = deck

        self.player_cards = [self.deck[0], self.deck[1]]
        self.player_value = self.calculate_cards_value(self.player_cards)

        self.dealer_cards = [self.deck[2], self.deck[3]]
        self.dealer_value = self.calculate_cards_value(self.dealer_cards)

        self.cards_index = 4
        self.player_number_of_aces = 0
        self.dealer_number_of_aces = 0

    def print_cards(self):
        print(f"\nYour cards: {self.player_cards}")
        print(f"Dealer's cards: {self.dealer_cards[0:1]}")

    def print_final_cards(self):
        print(f"\nYour cards: {self.player_cards}   {self.player_value}")
        print(f"Dealer's cards: {self.dealer_cards}   {self.dealer_value}")

    def check_black_jack(self, player_value:int, dealer_value:int):
        if player_value == 21 and dealer_value == 21:
            print("Tie!")
            self.print_final_cards() 
            return 0
        elif player_value == 21:
            print("You have Black Jack!")
            self.print_final_cards() 
            return self.bet
        elif dealer_value == 21:
            print("Dealer has Black Jack!")
            self.print_final_cards() 
            return self.bet * -1
        return 'No'  

    def player_get_card(self):
        self.player_cards.append(self.deck[self.cards_index])
        self.player_value += self.calculate_cards_value(
            [self.deck[self.cards_index]])
        
        if self.player_value > 21 and 'A' in self.player_cards and self.player_number_of_aces < self.player_cards.count('A'):
            self.player_value -= 10
            self.player_number_of_aces += 1

        self.cards_index += 1

    def dealer_get_card(self):
        while self.dealer_value < 17:
            self.dealer_cards.append(self.deck[self.cards_index])
            self.dealer_value += self.calculate_cards_value(
                [self.deck[self.cards_index]])
            
            if self.dealer_value > 21 and 'A' in self.dealer_cards and self.dealer_number_of_aces < self.dealer_cards.count('A'):
                self.dealer_value -= 10
                self.dealer_number_of_aces += 1

            self.cards_index += 1

    def calculate_cards_value(self, cards: list) -> int:
        value = 0
        for i in cards:
            if i == 'J' or i == "Q" or i == "K":
                value += 10
            elif i == 'A':
                value += 11
            else:
                value += int(i)

        return value

    def end_round(self) -> str:
        clear_terminal()

        if self.player_value > self.dealer_value:
            print("Congrats, you won!")
            self.print_final_cards()
            print()
            return "win"
        elif self.player_value <= 21 and self.dealer_value > 21:
            print("Congrats, you won!")
            self.print_final_cards()
            print()
            return "win"
        elif self.dealer_value > self.player_value:
            print("Unfortunately you lost!")
            self.print_final_cards()
            print()
            return "lose"
        else:
            print("It's a tie")
            self.print_final_cards()
            print()
            return "tie"

    def bust_cards(self):
        clear_terminal()
        print("You Lost!")
        print("Your cards are busted")
        print(f"\nYour final cards: {self.player_cards}")
        print(f"Dealer's final cards: {self.dealer_cards}\n")
