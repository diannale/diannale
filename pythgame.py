class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        suit_symbol = self.suit.symbol
        return f"{self.value} of {self.suit.description} {suit_symbol}"

class Suit:
    SYMBOLS = {"Hearts": "♥", "Diamonds": "♦", "Clubs": "♣", "Spades": "♠"}

    def __init__(self, description):
        self._description = description
        self._symbol = Suit.SYMBOLS[description]

    @property
    def description(self):
        return self._description

    @property
    def symbol(self):
        return self._symbol

class Deck:
    def __init__(self):
        self.cards = [Card(Suit(suit), value) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades'] for value in range(2, 15)]
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        card = deck.draw()
        if card:
            self.hand.append(card)

    def play_card(self):
        if len(self.hand) > 0:
            return self.hand.pop()
        else:
            return None

class WarCardGame:
    
    def start_battle(self, cards_from_war=None):
        print("\n== Let's Start the Battle ==\n")

        player_card = self._player.draw_card()
        computer_card = self._computer.draw_card()

        print(f"Your Card:")
        player_card.show()
        print(f"\nComputer Card: ")
        computer_card.show()

        winner = self.get_round_winner(player_card, computer_card)

        if winner == WarCardGame.PLAYER:
            print("\nYou won this round!")
            self._player.add_card(player_card)
            self._player.add_card(computer_card)
        elif winner == WarCardGame.COMPUTER:
            print("\nThe computer won this round.")
            self._computer.add_card(computer_card)
            self._computer.add_card(player_card)
        else: # war
            if self._player.deck.size < 4 or self._computer.deck.size < 4:
                if self._player.deck.size < 4:
                    print(f"\nGame Over. {self._player.name} has less than 4 cards and cannot start a war.")
                else:
                    print(f"\nGame Over. {self._computer.name} has less than 4 cards and cannot start a war.")
                    
                if self._player.deck.size > self._computer.deck.size:
                    print("\nGame Over. You won!")
                else:
                    print("\nGame Over. The computer won.")
                return None
                
            else:
                print("\nIt's a tie. This is war!")
                cards_from_war = [player_card, computer_card]
                for i in range(3):
                    cards_from_war.append(self._player.draw_card())
                    cards_from_war.append(self._computer.draw_card())
                
                self.start_battle(cards_from_war)

def main():
    deck = Deck()
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    for _ in range(len(deck.cards) // 2):
        player1.draw(deck)
        player2.draw(deck)

    while True:
        input("Press Enter to play a round...")

        card1 = player1.play_card()
        card2 = player2.play_card()

        if card1 is None or card2 is None:
            print("Game over! One of the players ran out of cards.")
            break

        print(f"{player1.name} plays {card1}")
        print(f"{player2.name} plays {card2}")

        if card1.value > card2.value:
            print(f"{player1.name} wins this round!")
            player1.hand.extend([card1, card2])
        elif card2.value > card1.value:
            print(f"{player2.name} wins this round!")
            player2.hand.extend([card1, card2])
        else:
            print("It's a tie! Time for a war.")

    # After the card game ends, initialize and play the War card game here
    deck = Deck()
    player = Player("Dianna")
    computer = Player("Computer", is_computer=True)
    war_game = WarCardGame(player, computer, deck)

    while not war_game.check_game_over():
        war_game.start_battle()
        answer = input("\nAre you ready for the next round?\nPress Enter to continue. Enter X to stop.")
        if answer.lower() == "x":
            break

if __name__ == "__main__":
    main()