import random


def deal_card():
    """Returns a random card for the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and get back the score"""

    if sum(cards) == 21 and len(cards) == 0:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw!"
    elif c_score == 0:
        return "Blackjack! House Wins"
    elif u_score == 0:
        return "Blackjack! You Win"
    elif u_score > 21:
        return "Bust! House Wins"
    elif c_score > 21:
        return "House Bust!"
    elif u_score > c_score:
        return "You Win!"
    else:
        return "House Wins"



user_card = []
computer_cards = []
user_score = -1
computer_score = -1
is_game_over = False

for _ in range(2):
    user_card.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:

    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_card}, your score {user_score}")
    print(f"Current computer score: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' tp pass: ")
        if user_should_deal == 'y':
            user_card.append(deal_card())
        else:
            is_game_over = True

while computer_cards != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(f"Your final hand: {user_card}, final score: {user_score}")
print(f"House's final hand {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))



############
"""Play game function below. 
   It is previous code defined as a function"""


def play_game():
    user_card = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_card}, your score {user_score}")
        print(f"Current computer score: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' tp pass: ")
            if user_should_deal == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_cards != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"House's final hand {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Would you like to play a game of Blackjack? Type 'yes' or 'no'").lower() == 'yes':
    print("\n" * 35)
    play_game()