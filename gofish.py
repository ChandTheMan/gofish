class Card_Pack:
    def __init__(self) -> None:
        self.suits = ["C", "S", "H", "D"]
        self.numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]

        self.draw_pack = []
        for suits in self.suits:
            for numbers in self.numbers:
                self.draw_pack.append(Card(suits, numbers))

class Card:
    def __init__(self, suit, number) -> None:
        self.suit = suit
        self.number = number

    def whats_the_card(self):
        print(f"The card is a {self.number} of {self.suit}")
        return

card_pack = Card_Pack()

class Go_Fish:
    def __init__(self) -> None:
        self.round = 0
        self.team_1_fours = []
        self.team_2_fours = []
        self.draw_pack = Card_Pack()
    
    def four_check(self, team_1_hand, team_2_hand):
        hands = [team_1_hand, team_2_hand]
        for players_hands in hands:
            number_tracker = [0,0,0,0,0,0,0,0,0,0,0,0,0]
            for cards in players_hands:
                number_tracker[cards.number-1] += 1
            index_tracker = []
            for cards in len(number_tracker):
                if number_tracker(cards) == 4:
                    index_tracker.append(cards)
    
    

        
class Player:
    def __init__(self, number) -> None:
        self.number = number
        self.hand = [Card("H", 3), Card("C", 3), Card("C", 6)] # made of cards

    def place_fours_down(self, card_suit):
        for cards in self.hand:
            if cards.suit == card_suit:
                self.hand

    def remove_card(self, card_number):
        suits = []
        removed_cards = []
        i = 0
        try:
            while True:
                selected_card = self.hand[i]
                if selected_card.number == card_number:
                    removed_cards.append(self.hand.pop(i))
                    i -= 1
                i += 1
        except IndexError:
            return removed_cards

    def receive_card(self, cards: list):
        self.hand += cards
        return
    
    def print_hand(self):
        for cards in self.hand:
            print(cards.whats_the_card())
        



me = Player(1)
me.print_hand()
me.remove_card(3)
print("hellooo")
me.print_hand()