import random

class Card_Pack:
    def __init__(self) -> None:
        self.suits = ["C", "S", "H", "D"]
        self.numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]

        self.draw_pack = []
        for suits in self.suits:
            for numbers in self.numbers:
                self.draw_pack.append(Card(suits, numbers))
    
    def shuffle(self):
        self.staging_pack = []
        end_point = 51 
        while len(self.staging_pack) != 52:
            self.staging_pack.append(self.draw_pack.pop(random.randint(0, end_point)))
            end_point -= 1
        self.draw_pack = self.staging_pack
    

        

class Card:
    def __init__(self, suit, number) -> None:
        self.suit = suit
        self.number = number

    def whats_the_card(self):
        print(f"The card is a {self.number} of {self.suit}")
        return

# card_pack = Card_Pack()

class Go_Fish:
    def __init__(self) -> None:
        self.round = 0
        self.team_1_fours = []
        self.team_2_fours = []
        self.card_pack = Card_Pack()
        self.player_1 = Player(1, "Corey")
        self.player_2 = Player(2, "Courteney")
    
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
    
    def deal(self):
        return

    def give_card(self, target_player):
        target_player.hand.append(self.card_pack.draw_pack.pop(0))
        return
    
    def deal(self, starting_number_of_cards):
        for i in range(starting_number_of_cards):
            self.give_card(self.player_1)
            self.give_card(self.player_2)
        


    def start_the_game(self, starting_hand_count):
        self.card_pack.shuffle()
        self.deal(starting_hand_count)
        # self.give_card(self.player_1)
        self.player_1.print_hand()

        
class Player:
    def __init__(self, number, name) -> None:
        self.number = number
        self.hand = [] # made of cards
        self.name = name

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
            cards.whats_the_card()
    
    def whats_my_name(self):
        print(self.name)



# me = Player(1, "Corey")
# me.print_hand()
# me.remove_card(3)
# print("hellooo")
# me.print_hand()

game = Go_Fish()
game.start_the_game(7)
