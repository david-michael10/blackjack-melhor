import random
from art import  logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(deck):
    if len(deck) == 2 and sum(deck) == 21:
        return 0

    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)
    return sum(deck)


def compare(user,pc):
    if user == pc:
        return "Draw"
    elif pc == 0:
        return "You lose. Opponent has a Blackjack"
    elif user == 0:
        return "You win. You have a Blackjack"
    elif user > 21:
        return "You lose. You went over"
    elif pc > 21:
        return "You win. Opponent went over"
    elif user > pc:
        return "You win"
    else:
        return "You lose"

def game():
    print(logo)
    user_cards = []
    pc_cards = []
    pc_score = -1
    user_score = -1

    for i in range(0, 2):
        user_cards.append(deal_card())
        pc_cards.append(deal_card())

    over = False
    while not over:
        user_score = calculate_score(user_cards)
        pc_score = calculate_score(pc_cards)

        print(f"Your cards: {user_cards}. Current score = {user_score}")
        print(f"Computer's first card: {pc_cards[0]}")
        print()

        if user_score == 0 or pc_score == 0 or user_score > 21:
            over = True
        else:
            choice = input("Type 'y' to get another card or 'n' to pass: ")
            print()
            if choice == "y":
                user_cards.append(deal_card())
            else:
                over = True

    while pc_score != 0 and pc_score < 17:
        pc_cards.append(deal_card())
        pc_score = calculate_score(pc_cards)

    print("\n" * 20)
    print(f"Your cards: {user_cards}, final score = {user_score}")
    print(f"Computer cards: {pc_cards}, final score = {pc_score}")
    print()
    print(compare(user_score,pc_score))
    print()

while input("Do you want to play? 'y' or 'n': ") == "y":
    print("\n" * 50)
    game()