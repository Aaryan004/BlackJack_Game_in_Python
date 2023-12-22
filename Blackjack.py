import random
rank=['ACE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING']
value={'ACE': 1, 'TWO': 2, 'THREE': 3, 'FOUR': 4, 'FIVE': 5, 'SIX':6, 'SEVEN': 7, 'EIGHT': 8, 'NINE': 9, 'TEN': 10, 'JACK': 11, 'QUEEN': 12, 'KING': 13}

class Dealer:
    dealer_cards=[]

    def __init__(self):
        pass

class Player():
    player_cards=[]

    def __init__(self, name, amount):
        self.amount=amount
        self.name=name
        pass

    def win(self,win_amount):
        self.amount+=win_amount
        pass
    def lose(self,lose_amount):
        self.amount-=lose_amount
        pass
    pass
print('WELCOME TO THE GAME OF BLACKJACK')
name = input("Enter your name player: ").upper()
money = input("Enter the money you have: ")
total = True
opponent = Dealer()
player = Player(name, int(money))
play_again=True
while play_again==True:
    while total==True:
        print('PLACE THE BETS')
        bet = int(input('Enter the bet amount: '))
        while(bet > player.amount):
            print("SORRY BUT YOU DON'T HAVE THAT MUCH FUND")
            bet = int(input('Enter the bet amount: '))
        for i in range(0,2):
            opponent.dealer_cards.append(random.choice(rank))
            player.player_cards.append(random.choice(rank))
        print(f"DEALER'S CARDS ARE: [] {opponent.dealer_cards[-2]} ")
        print(f"PLAYER'S CARDS ARE: {player.player_cards[-1]} {player.player_cards[-2]} ")
        win=False
        winnings=0
        if ('ACE' in player.player_cards and 'TEN' in player.player_cards):
            print(f"{name} HITS A BLACKJACK")
            player.win(bet + 0.5*bet)
            win=True
            winnings=1.5*bet
            break
            pass
        if(value[player.player_cards[-1]]+value[player.player_cards[-2]] > 21):
            print('BUST')
            player.lose(bet)
            break
            pass
        hit = input('HIT OR STAY: ').upper()
        if (hit=='HIT' or hit=='H'):
            player.player_cards.append(random.choice(rank))
            print(f"DEALER'S CARDS ARE: {opponent.dealer_cards[-1]} {opponent.dealer_cards[-2]} ")
            print(f"PLAYER'S CARDS ARE: {player.player_cards[-3]} {player.player_cards[-2]} {player.player_cards[-1]}")
            if(value[player.player_cards[-1]]+value[player.player_cards[-2]]+value[player.player_cards[-3]] > 21):
                print('BUST')
                player.lose(bet)
                pass
            elif(value[opponent.dealer_cards[-1]] + value[opponent.dealer_cards[-2]] > value[player.player_cards[-1]] + value[
                player.player_cards[-2]] + value[player.player_cards[-3]]):
                print('DEALER WINS')
                player.lose(bet)
                pass
            elif (value[opponent.dealer_cards[-1]] + value[opponent.dealer_cards[-2]] < value[player.player_cards[-1]] + value[player.player_cards[-2]] + value[player.player_cards[-3]]):
                print(f"{name} WINS")
                player.win(bet)
                win=True
                winnings=bet
                pass
            else:
                print("IT IS A DRAW")
                pass
        else:
            print(f"DEALER'S CARDS ARE: {opponent.dealer_cards[-2]} {opponent.dealer_cards[-1]} ")
            print(f"PLAYER'S CARDS ARE: {player.player_cards[-1]} {player.player_cards[-2]} ")
            if(value[opponent.dealer_cards[-1]] + value[opponent.dealer_cards[-2]] > value[player.player_cards[-1]] + value[player.player_cards[-2]]):
                print('DEALER WINS')
                player.lose(bet)
                pass
            elif (value[opponent.dealer_cards[-1]] + value[opponent.dealer_cards[-2]] < value[player.player_cards[-1]] + value[player.player_cards[-2]]):
                print(f"{name} WINS")
                player.win(bet)
                win=True
                winnings=bet
                pass
            else:
                print("IT IS A DRAW")
                pass
            pass
        if (player.amount == 0):
            print(f"YOU HAVE RUN OUT OF FUNDS")
            break
        if win==True:
            print(f"YOU ARE ON A ROLL, YOUR WINNINGS ARE {bet} AND YOUR TOTAL IS {player.amount}")
            break
            pass
        else:
            print(f"BETTER LUCK NEXT TIME.YOUR AMOUNT LEFT IS {player.amount}")
            break
            pass
    if(player.amount==0):
        print("YOU HAVE NO FUNDS LEFT")
        break
    again=input("DO YOU WANT TO GO AGAIN?").upper()
    if(again=="NO" or again=="N"):
        play_again=False
        pass
    else:
        pass
    player.player_cards=[]
    opponent.dealer_cards=[]




