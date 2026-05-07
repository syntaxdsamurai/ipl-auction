class Team:
    def __init__(self,name,budget):
        self.name = name
        self.budget = budget
        self.squad = []

    def can_afford(self,amount):
        return self.budget >= amount

    def add_player(self,player,price):
        self.squad.append(player)
        self.budget -= price

    def __str__(self):
        return f'{self.name} | Budget: {self.budget} | Players: {len(self.squad)}'