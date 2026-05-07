from auction import Auction

def main():
    auction = Auction()
    auction.load_players('data/players.json')
    auction.setup_teams()
    auction.run()
    auction.show_results()
    auction.save_results('auction_results.txt')

if __name__ == '__main__':
    main()