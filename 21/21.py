from Deck import Deck
from Hand import Hand


def new_game():
    d = Deck()
    player_hand = Hand("Player")
    dealer_hand = Hand("Dealer")
    player_hand.add_card(d.deal_card())
    player_hand.add_card(d.deal_card())
    dealer_hand.add_card(d.deal_card())
    print(dealer_hand)
    print("=" * 20)
    print (player_hand)
    in_game = True
    while player_hand.get_value() < 21:
        ans = input("Hit or stand? (h/s) ")
        if ans == "h":
            player_hand.add_card(d.deal_card())
            print (player_hand)
            if player_hand.get_value() > 21:
                print ("You lose")
                in_game = False
        else:
            print ("You stand!")
            break
    print ("=" * 20)
    if in_game:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(d.deal_card())
            print (dealer_hand)
            if dealer_hand.get_value() > 21:
                print ("Dealer bust")
                in_game = False
    if in_game:
        if player_hand.get_value() > dealer_hand.get_value():
            print ("You win")
        else:
            print ("Dealer win")
