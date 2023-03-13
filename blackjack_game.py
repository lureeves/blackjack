import random
import os

class Deck:
    def __init__(self):
        self.deck = []
        
    def MakeDeck(self):
        # Makes deck, set of 52 strings, ex "6 of Clubs"
        numbers = ['Ace of', '2 of', '3 of', '4 of', '5 of', '6 of', '7 of', '8 of', '9 of', '10 of', 'Jack of', 'Queen of', 'King of']
        suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
        for num in numbers:
            for suit in suits: 
                self.deck.append(f"{num} {suit}")
                
    def Shuffle(self):
        # Shuffles deck
        random.shuffle(self.deck)   
        
    def DealCard(self, human):
        # Gets a random card from deck and returns card
        human.hand.append(self.deck.pop())
        

class Human:
    def __init__(self, hand = [], handTotal = 0):
        self.hand = hand
        self.handTotal = handTotal
        
    def UpdateHandTotal(self):
        word_lookup = {"Ace": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "Jack": 10,
            "Queen": 10,
            "King": 10}
        self.handTotal = 0
        # Uses dict to find value of each hand and return to word_lookup
        for card in self.hand:
            words = card.split()
            self.handTotal += word_lookup[words[0]]
    
class Dealer(Human):
    def __init__(self, hand = [], handTotal = 0):
        super().__init__(hand, handTotal)        
    
class Player(Human):
    def __init__(self, hand = [], handTotal = 0):
        super().__init__(hand, handTotal)
        self.inputChoice = ''

        
def main():

    playAgain = 'y'

    while playAgain == 'y':

        os.system('cls') # Clears the terminal

        # Instantiating deck attribute, making deck and shuffling
        deck = Deck()
        deck.MakeDeck()
        deck.Shuffle()

        # Instantiating dealer and player
        deal_inst = Dealer()
        play_inst = Player()

        # Setting values to 0 in case of replays
        play_inst.handTotal = 0
        deal_inst.handTotal = 0
        play_inst.hand = []
        deal_inst.hand = []

        # Distributing cards to hands
        deck.DealCard(deal_inst)
        deck.DealCard(deal_inst)
        deck.DealCard(play_inst)
        deck.DealCard(play_inst)

        # Add to hand
        deal_inst.UpdateHandTotal()
        play_inst.UpdateHandTotal() 
        
        # play_inst.handTotal = 21
        blackJack = False
        
        if play_inst.handTotal == 21:
            blackJack = True
            print('\nBlackjack!!!')
                
        # Choice acts as a flag and input
        choice = 'h'
        
        # Game Logic for Player
        while play_inst.handTotal != 21:
            if play_inst.handTotal > 21:
                break
            else:
                os.system('cls') # Clears the terminal
                # Print Scores
                print("\nPlayer's Hand:")
                print(play_inst.hand)
                print("Total Hand Value:", play_inst.handTotal)
                print("\nDealer's First Card:")
                print(deal_inst.hand[0])
                choice = input("Do you want to (h)it or (s)tand? ").lower()
                if choice == 'h':
                    deck.DealCard(play_inst)
                    play_inst.UpdateHandTotal()
                elif choice == 's':
                    break


        # Game Logic for Dealer 
        if (deal_inst.handTotal < 21) and (choice == 's'):
            print("in if")
            while deal_inst.handTotal < 17:
                deck.DealCard(deal_inst)
                deal_inst.UpdateHandTotal()
        
        
        if blackJack == False:
            os.system('cls') # Clears the terminal
            
            # Determine Winner
            # If either are over 21
            if deal_inst.handTotal > 21 or play_inst.handTotal > 21:
                if deal_inst.handTotal > 21 and play_inst.handTotal > 21:
                    print("\nNobody Wins")
                elif play_inst.handTotal > 21:
                    print("\nDealer Wins, Player busts")
                elif deal_inst.handTotal > 21:
                    print("\nPlayer Wins, Dealer busts")
            # If not over 21, then choose winner by larger value
            elif deal_inst.handTotal > play_inst.handTotal:
                print('\nDealer Wins')
            elif deal_inst.handTotal < play_inst.handTotal:
                print('\nPlayer Wins')
            else:
                print('\nPush - Dealer and Player had the same score')


        # Print Scores
        print("\nPlayer's Hand:")
        print(play_inst.hand)
        print("Total Hand Value:", play_inst.handTotal)
        print("\nDealers's Hand:")
        print(deal_inst.hand)
        print("Total Hand Value:", deal_inst.handTotal)
        
        # Ask Play Again
        playAgain = input("Play again (y/n)? ").lower()
    
main()      