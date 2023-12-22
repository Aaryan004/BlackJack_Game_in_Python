# BlackJack_Game_in_Python
The goal of Blackjack is to beat the dealer by having a hand value closer to 21 without exceeding it. Each card has a value, and face cards (JACK, QUEEN, KING) are worth 11, 12 and 13 points respectively. An ACE can be worth 1 or 11 points, depending on which value benefits the hand more.

Card Values:

Number cards (TWO through TEN) are worth their face value.
Face cards (JACK, QUEEN, KING) are worth 11,12 and 13 points respectively.
ACE can be worth 1 or 11 points.

Gameplay:

- The game begins with each player (the player and the dealer) being dealt two cards.
- The player's cards are usually dealt face up, while one of the dealer's cards is face up, and the other is face down.
- The player can choose to "HIT" (take another card) or "STAY" (keep the current hand).
- If the total value of the player's hand exceeds 21, it's a "BUST," and the player loses.
- If the player chooses to stay, the dealer reveals their face-down card.
- If the dealer busts, the player wins. If not, the hands are compared, and the one closest to 21 without going over wins.

Special Cases:

- Getting an ACE and a 10-point card initially is a "BLACKJACK" and is a winning hand.
- If both the player and the dealer have the same total, it's a "DRAW."

Explanation of the Code:

Classes:

- Dealer and Player classes are defined to represent the dealer and player, respectively.
- Player class has methods for winning and losing.

Betting:

- The player places bets, and the game checks if the player has enough funds.

Dealing Cards:

- Two cards are dealt to the dealer and the player.
- Initial cards are shown.

Game Logic:

- The player decides to hit or stay.
- If the player chooses to hit, cards are drawn, and the total is checked for bust or win conditions.
- If the player stays, the dealer reveals their cards and plays according to the rules.

Outcome:

- The winner is determined based on the total values of the hands.
- Player's funds are updated accordingly.

Continuation:

- The player can choose to play again.
The game resets, and the loop continues until the player decides to stop or runs out of funds.

Conclusion:

The game provides feedback on each round, indicating whether the player won, lost, or if it's a draw.
The game ends if the player runs out of funds or chooses not to play again
