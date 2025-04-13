"""Blackjack
The classic card game known as 21. (This version does not support splitting or insurance)
More info at https://en.wikipedia.org/wiki/Blackjack"""

import random, sys

# Set up constants:
HEARTS = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES = chr(9824) # Character 9824 is '♠'.
CLUBS = chr(9827) # Chacter 9827 is '♣'.
BACKSIDE = 'backside'

def main():
    print('''Blackjack
          
    Rules:
        Try to get as close to 21 as you can without going over.
        Kings, Queens, are worth 10 points.
        Aces are worth 1 point or 11 points.
        Cards 2 through 10 are worth their face value.
          
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
          
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.''')
    
    money = 5000
    while True: # Main game loop.
        # Check if the player has run out of money:
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print("Thanks for playing!")
            sys.exit()

        # Let the player enter their bet for this round:
        print('Money:', money)
        bet = Get_Bet(money)

        # Give the dealer and player two cards from the deck each:
        deck = Get_Deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        # Handle player actions:
        print('Bet:', bet)
        while True: # Keep looping over until the player stands or busts.
            Display_Hands(player_hand, dealer_hand, False)
            print()

            # Check if the player has bust:
            if Get_Hand_Value(player_hand) > 21:
                break

            # Get the players move, either H, S, or, D:
            move = Get_Move(player_hand, money - bet)

            # Handle the player actions:
            if move == 'D':
                # Player is doubling down, they can increase their bet:
                Additional_Bet = Get_Bet(min(bet, (money - bet)))
                bet += Additional_Bet
                print(f'Bet increased to {bet}')
                print('Bet:', bet)

            if move in ('H', 'D'):
                # Hit/doubling down takes another card.
                new_card = deck.pop()
                rank, suit = new_card
                print(f"You drew a {rank} of {suit}")
                player_hand.append(new_card)

                if Get_Hand_Value(player_hand) > 21:
                    # The player is busted:
                    continue

            if move in ('S', 'D'):
                # Stand/doubling down stops the players turn.
                break
            
        # Handle the dealer's actions:
        if Get_Hand_Value(player_hand) <= 21:
            while Get_Hand_Value(dealer_hand) < 17:
                # The dealer hits:
                print('Dealer hits ...')
                dealer_hand.append(deck.pop())
                Display_Hands(player_hand, dealer_hand, False)

                if Get_Hand_Value(dealer_hand) > 21:
                    break # The dealer has busted.
                input('Press Enter to continue...')
                print('\n\n')

        # Show the final hands:
        Display_Hands(player_hand, dealer_hand, True)

        player_value = Get_Hand_Value(player_hand)
        dealer_value = Get_Hand_Value(dealer_hand)
        # Handle whether the player won, lost or tied:
        if dealer_value > 21:
            print(f'Dealer busts! You win ${bet}!')
            money += bet
        elif (player_value > 21) or (player_value < dealer_value)
            print('You lost!')
            money -= bet
        elif player_value > dealer_value:
            print('You won ${bet}!')
            money += bet
        elif player_value == dealer_value:
            print ("It's a tie, the bet is returned you")

        input("Press enter to continue...")
        print('\n\n')

def Get_Bet(max_bet):
    """Ask the player how"""