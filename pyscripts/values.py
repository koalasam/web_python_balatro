class money:
    def __init__ (self, starting_money = 4):
        self.value = starting_money
        self.minimum = 0
    
    def gain_money(self, amount = 0):
        self.value =+ amount

    def lose_money(self, amount, overflow = False):
        if overflow == False and self.value - self.amount < 0: return False
        else: self.value =- amount; return True


class curent_blind:
    def __init__ (self, blind_type = "small"):
        self.blind_type = blind_type
        self.is_boss = False
        self.boss_type = None
