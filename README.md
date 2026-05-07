# IPL Auction Simulator 

A fully interactive IPL auction simulator built in Python using OOP.
Bid on real players, manage team budgets, and generate auction reports.

## How it works

4 IPL teams compete to sign 20 real players in a live bidding system.
Each team starts with a 90 Crore budget. Teams bid in sequence — 
raise the bid or withdraw. Highest remaining bidder wins the player.

## Features

- Real IPL player pool (batsmen, bowlers, allrounders, wicketkeepers)
- Live bidding with budget tracking
- Automatic unsold player detection
- Full auction report saved to txt after every run

## Project Structure

\```
ipl-auction/
│
├── models/
│   ├── player.py       # Player class
│   └── team.py         # Team class
│
├── data/
│   └── players.json    # 20 real IPL players
│
├── reports/
│   └── auction_results.txt
│
├── auction.py          # Auction class — core logic
├── main.py             # Entry point
└── requirements.txt
\```

## How to run

\```bash
python main.py
\```

When prompted — type `y` to bid, `n` to withdraw.

## Sample output

\```
TEAM: Royal Challengers Bangalore
REMAINING BUDGET: 76.0cr
SQUAD:
  - Virat Kohli (3.5Cr)
  - Jos Buttler (6.0Cr)

UNSOLD PLAYERS
  - Rohit Sharma | Batsman
  - Hardik Pandya | AllRounder
\```

## Tech Stack

Python · OOP · JSON · File I/O

## Author

Dhruv | github.com/syntaxdsamurai
