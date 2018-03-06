
import random

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