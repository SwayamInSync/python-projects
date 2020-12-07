import random
usercards=[]
compcards=[]
is_game_over=False

def dealcard():
    """ Return a random card from deck """
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    return (random.choice(cards))

from art import logo
print(logo)

def compare(user_score,comp_score):
    if user_score==comp_score and user_score<=21 and comp_score<=21: # order of giving conditions is important top to bottom
        return "Draw"
    elif user_score==comp_score and user_score>21:
        return "you lost"
    elif comp_score==0:
        return "Comp has win"
    elif user_score==0:
        return "you won"
    elif user_score>21:
        return " you went over you lost"
    elif comp_score>21:
        return "opponent went over you won"
    elif user_score>comp_score:
        return "you win"
    else:
        return "you loose"

for _ in range(2):
    usercards.append(dealcard())
    compcards.append(dealcard())

def calculate_score(cards):
    """ take list of cards and return the score of cards"""
    if 11 in cards and 10 in cards and len(cards)==2:
        return 0 # 0 represent blackjack
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


while not is_game_over: # only responsible for user to keep drawing card
    user_score=calculate_score(usercards) # it could be a 0 (blackjack) or the sum of cards
    comp_score=calculate_score(compcards)
    print(f" your cards are {usercards} and your score is {user_score}")
    print(f"computer cards are {compcards[0]}")

    if user_score==0 or comp_score==0 or user_score>21:
        is_game_over=True
    else:
        user_should_deal=input("type y or another card or n for pass ")
        if user_should_deal=='y':
            usercards.append(dealcard())
        else:
            is_game_over=True


while comp_score!=0 and comp_score<17:
    compcards.append(dealcard())
    comp_score=calculate_score(compcards)

print(f"your final hand is {usercards} and your final score is {user_score} ")
print(f"computer final hand is {compcards} and comp final score is {comp_score}")
print(compare(user_score,comp_score))



   