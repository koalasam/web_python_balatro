from checkjokers import check_jokers
from values import money

class card:
    def __init__ (self, rank, suit, edition = None, enhancement = None, seal = None):
        self.rank = rank # rank identifier for the card
        self.suit = suit # suit of the card
        self.edition = edition # edition of the card
        self.enhancement = enhancement # enhancement on the card (foil, holo, prismatic, negative)
        self.seal = seal # seal on the card (red, blue, purple, gold)
        if str(rank).lower() not in ["k", "q", "j", "a"]: self.value = int(rank) # if not face card or ace value is rank
        elif rank.lower() in ["k", "q", "j"]: self.value = 10 # if face card value is 10
        elif rank.lower() == "a": self.value = 11 # if ace value is 11
        else: self.value = 0
        if self.edition.lower() == "negative": self.card_slots = 0
        else: self.card_slots = 1
    
    def played_score(self, triggers = 1, chips_score = 0, mult_score = 1):
        if self.seal.lower() == "red": triggers =+ 1
        for i in range(triggers):
            check_jokers.played_card_scale(self)
            chips_score =+ self.value
            if self.seal.lower() == "gold":
                self.gold_seal()

        return chips_score, mult_score
    
    def gold_seal(self):
        money.value =+ 4