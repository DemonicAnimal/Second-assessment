import time
bool_choice = True
str_userChoice =''

print('Welcome to my text adventure game!')
time.sleep(1.5)
print('for every decision there will only be ONE correct awnser, choose wisely...')
time.sleep(2.0)
print('If you do make a wrong decision I wont force you to restart im not that mean. (pinky promise)')
time.sleep(3.0)
print('to make a decision input either a,b,c, or d.\n')
time.sleep(2.0)

print('You wake up in the forest as the sun rises in the distance.')
time.sleep(2.0)
print('You have no idea how you got here...')
time.sleep(5.0)
print('After taking awhile to think you decide there are four main things you should do.\n')
time.sleep(3.0)

print('(a) Search for civilization.')
time.sleep(1.0)
print('(b) Search for food.')
time.sleep(1.0)
print('(c) Search for water.')
time.sleep(1.0)
print('(d) Search for shelter')
time.sleep(1.0)

while bool_choice is True:

    str_userChoice = input('What will you do?\n')
    time.sleep(1.0)

    if str_userChoice == 'a':  
        print('You search for hours trees and bushes begin to blur as you go deeper and deeper into the forest eventually it gets to dark to see. you hear a roar behind you and sprint in the other direction quickly hitting a tree, you pass out instantly and your body is devoured by morning.\nYou died Try again.') 
        bool_choice = True 
    
    elif str_userChoice == 'b':
        print('You see an apple tree nearby you climb it hoping to pick some apples... but sadly when reaching for an apple you slip and land head first on the ground below cracking your skull on a rock.\nYou died Try again.') 
        bool_choice = True 
    
    elif str_userChoice == 'c':
        print('After awhile of walking through trees you find a small lake, fish swim inside causing the water to ripple.') 
        bool_choice = False 
    
    elif str_userChoice == 'd':
        print('After a quick search you find a cave and run inside after a short examination a bear tears you limb from limb.\nYou died Try again.') 
        bool_choice = True 
    
    else:
        print(' Invalid ')

pass
