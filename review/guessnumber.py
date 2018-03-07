
import random

'''方法一 耦合度太高
def guess(number):
    point1 = random.randrange(1,7)
    point2 = random.randrange(1,7)
    point3 = random.randrange(1,7)
    points = point1 + point2 + point3
    state = ''
    if points>=11 and points <=18:
        state = 'Big'
    elif points>=3 and points <= 10:
        state = 'Small'
    if number == state:
        print('The points are [{},{},{}] You Win!'.format(point1,point2,point3))
    else:
        print('The points are [{},{},{}] You Lose!'.format(point1,point2,point3))
print('<<<<< GAME STARTS! >>>>>')

state = input('Big or Small:')

print('<<<<< ROLE THE DICE! >>>>>')
guess(state)
'''

def roll_dice(number=3,points=None):
    print('<<<<< ROLE THE DICE! >>>>>')
    if points is None:
        points = []
    for num in range(number):
        point = random.randrange(1,7)
        points.append(point)
    return points

def roll_result(total):
    isBig = 11 <= total <=18
    isSmall = 3 <= total <=10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'

def start_game():
    bet = 1000
    while bet > 0:
        print('<<<<< GAME STARTS! >>>>>')
        your_choice = input('Big or Small:')
        your_bet = input('How much you wanna bet ? -')
        choices = ['Big','Small']
        if your_choice in choices:
            points = roll_dice()
            total = sum(points)
            if your_choice == roll_result(total):
                print('The points are',points,'You win !')
                bet += int(your_bet)
                print('You gained',your_bet,',you have',bet,'now')
            else:
                print('The points are',points,'You lose !')
                bet -= int(your_bet)
                print('You lost',your_bet,',you have',bet,'now')
        else:
            print('Invalid Words')
            start_game()
    else:
        print('GAME OVER')
start_game()

