import json
import os
import random

from models.player import Player
from models.team import Team

class Auction :
    def __init__(self):
        self.players = []
        self.teams = []

    def load_players(self,filename):
        with open(filename,'r') as f:
            data = json.load(f)
        for record in data:
            player = Player(record['name'],record['role'],record['country'],record['base_price'])
            self.players.append(player)

    def setup_teams(self):
        self.teams.append(Team('Mumbai Indians',90))
        self.teams.append(Team('Chennai Super Kings',90))
        self.teams.append(Team('Royal Challengers Bangalore',90))
        self.teams.append(Team('Kolkata Knight Riders',90))


    def run(self):
        print("IPL AUCTION STARTED")
        print("=" * 40)

        random.shuffle(self.players)  # randomize player order

        for player in self.players:
            print(f"\nPlayer up for auction: {player}")
            print(f"Base price: {player.base_price} Cr")

            current_bid = player.base_price
            current_winner = None
            active_teams = self.teams.copy()  # all teams start active

            while len(active_teams) > 1:
                still_active = []
                for team in active_teams:
                    if not team.can_afford(current_bid):
                        print(f"{team.name} cannot afford — withdraws")
                        continue

                    bid = input(f"{team.name} (Budget: {team.budget}Cr) — bid {current_bid}Cr? (y/n): ")

                    if bid.lower().strip().startswith('y'):
                        current_winner = team
                        current_bid += 0.5  # raise bid by 0.5 Cr
                        still_active.append(team)
                    else:
                        print(f"{team.name} withdraws")

                active_teams = still_active

            if current_winner:
                current_winner.add_player(player, current_bid)
                player.mark_sold(current_winner.name, current_bid)
                print(f"SOLD! {player.name} to {current_winner.name} for {current_bid} Cr")
            else:
                print(f"UNSOLD — {player.name}")

        print("\n" + "=" * 40)
        print("AUCTION COMPLETE")

    def show_results(self):
        print("\n" + "=" * 40)
        print("FINAL AUCTION RESULTS")
        print("=" * 40)

        for team in self.teams:
            print(f"\n{team.name} | Remaining budget: {team.budget} Cr")
            print("Squad:")
            for player in team.squad:
                print(f'{player.name} purchased for {player.sold_price}Cr')

    def save_results(self,filename):
        os.makedirs('reports',exist_ok=True)
        with open(f'reports/{filename}','w') as f:
            f.write('Auction Result \n\n')
            f.write('')
            for team in self.teams:
                f.write(f"TEAM: {team.name}\n")
                f.write(f"REMAINING BUDGET: {team.budget}cr\n")
                f.write("SQUAD:\n")
                for player in team.squad:
                    f.write(f"  - {player.name} ({player.sold_price}Cr)\n")
                f.write("-" * 30 + "\n\n")
            unsold = [p for p in self.players if not p.is_sold]
            f.write("UNSOLD PLAYERS\n")
            for player in unsold:
                f.write(f"  - {player.name} | {player.role}\n")



auction = Auction()
auction.load_players('data/players.json')
auction.setup_teams()
auction.run()
auction.show_results()
auction.save_results('auction_results.txt')
