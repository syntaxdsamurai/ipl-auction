class Player:
    def __init__(self,name, role, country, base_price):
        self.name = name
        self.role = role
        self.country = country
        self.base_price = base_price
        self.is_sold = False
        self.sold_to = None
        self.sold_price = None

    def mark_sold(self,team_name,price):
        self.is_sold = True
        self.sold_to = team_name
        self.sold_price = price

    def __str__(self):
        return f'{self.name} | {self.role} | {self.country} | Base: {self.base_price}Cr'