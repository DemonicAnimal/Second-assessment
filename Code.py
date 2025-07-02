import time
bool_choice = True
str_userChoice =''

print('Welcome to my text adventure game!')
time.sleep(1.5)
print('For every decision there will only be ONE correct awnser, choose wisely...')
time.sleep(2.0)
print('If you do make a wrong decision I wont force you to restart im not that mean. (pinky promise)')
time.sleep(3.0)
print('To make a decision input either 1,2,3,4, etc.\n')
time.sleep(3.0)

print('You wake up in the forest as the sun rises in the distance.')
time.sleep(2.0)
print('You have no idea how you got here...')
time.sleep(5.0)
print('After taking awhile to think you decide there are four main things you should do.\n')
time.sleep(3.0)

print('(1) Search for civilization.')
time.sleep(1.0)
print('(2) Search for food.')
time.sleep(1.0)
print('(3) Search for water.')
time.sleep(1.0)
print('(4) Search for shelter')
time.sleep(1.0)

while bool_choice is True:

    str_userChoice = input('\nWhat will you do?\n')
    time.sleep(1.0)

    if str_userChoice == '1':  
        print('You search for hours trees and bushes begin to blur as you go deeper and deeper into the forest eventually it gets to dark to see. you hear a roar behind you and sprint in the other direction quickly hitting a tree, you pass out instantly and your body is devoured by morning.\nYou died, try again.') 
        bool_choice = True 
    
    elif str_userChoice == '2':
        print('You see an apple tree nearby you climb it hoping to pick some apples... but sadly when reaching for an apple you slip and land head first on the ground below cracking your skull on a rock.\nYou died, try again.') 
        bool_choice = True 
    
    elif str_userChoice == '3':
        print('After awhile of walking through trees you find a small lake, fish swim inside causing the water to ripple.') 
        bool_choice = False 
    
    elif str_userChoice == '4':
        print('After a quick search you find a cave and run inside after a short examination a bear tears you limb from limb.\nYou died, try again.') 
        bool_choice = True 
    
    else:
        print('Invalid')

pass

time.sleep(2.5)
print('\nYou sit by the lake taking some time to think.')
time.sleep(1.5)
print('As you sit and ponder by the lake time flys by you dont even notice as you sit there from dawn till dusk.')
time.sleep(2.5)
print('When you finally notice the time you realize you need to find shelter IMMEDIATELY.')
time.sleep(2.0)
print('After a quick look around your surroundings you see a few possible options\n.')
time.sleep(1.5)

print('(1) A cave not far from the lake.')
time.sleep(1.0)
print('(2) A small ditch covered by the leaves and branches of a fallen tree.')
time.sleep(1.0)
print('(3) A clump of trees shrubs and foliage.')
time.sleep(1.0)

while bool_choice is False:

    str_userChoice = input('\nWhich shelter would be best?\n')
    time.sleep(1.0)

    if str_userChoice == '1':  
        print('As you enter the cave you get a strange feeling of deja vu its short lived however as your are quickly torn apart by a bear.\nYou died, try again.') 
        bool_choice = False
    
    elif str_userChoice == '2':
        print('You manage to get inside the small ditch its uncomfortable but warm you decide to try get some rest, it would be difficult in the small space if you werent so tired. The next morning you wake uncomfortable and unrested atleast your alive... you crawl out from the ditch and stretch but your whole body starts to cramp in protest, a beautiful morning light glimmers off the water as the sun rises.')
        bool_choice = True 
    
    elif str_userChoice == '3':
        print('As you settle inside the clump you quickly fall asleep exhausted... sadly the clump wasnt a good enough shelter and you died from hypothermia in your sleep.\nYou died, try again.') 
        bool_choice = False
    
    else:
        print('Invalid')

pass

time.sleep(5.0)
print('Quickly afterwards you realize how thirsty you are... come to think of it you havent eaten anything or drank anything for almost two days.')
time.sleep(2.0)
print('You walk over to the lake cup your hands and collect some water you then put your face upto your hands and take a sip.')
time.sleep(2.0)
print('The water is quite refreshing you take a few more sips until your satisfied then you need to solve the food problem...')
time.sleep(2.0)
print('After taking a moment to think you come up with a few options.')
time.sleep(1.0)

print('(1) Set a trap')
time.sleep(1.0)
print('(2) Try to hunt something')
time.sleep(1.0)
print('(3) Scavenge for food')
time.sleep(1.0)
print('(4) Fish in the lake')
time.sleep(1.0)

while bool_choice is True:

    str_userChoice = input('\nWhat will you do?\n')
    time.sleep(1.0)

    if str_userChoice == '1':  
        print('You set out to find something to make a trap with, after searching for awhile you are unable to find anything and head back to the lake.\nTry again.') 
        bool_choice = True 
    
    elif str_userChoice == '2':
        print('You try to make some kind of makeshift spear using a tough branch a sharpened stone and some flax its flimsy but looks like it will work. You head out into the forest and try to find something after awhile you find a buck you sneak up behind it and stab it through the stomach it goes through but its not quite enough the enraged deer turns to you and gores you before collapsing.\nYou died, try again.') 
        bool_choice = True 
    
    elif str_userChoice == '3':
        print('After heading out into the forest you quickly find a recently killed doe, the deer looks fresh you would just need to cook it. You grab its leg and start dragging it back to the lake, however the nearby hungry pack of wolves doesnt appreciate you stealing their recent kill three large wolves jump at you and tear you apart.\nYou died, try again.') 
        bool_choice = True 
    
    elif str_userChoice == '4':
        print('you craft a makeshift spear using a tough branch a sharpened stone and some flax its flimsy but looks like it will work. You sit by the lake and try to stab a fish you fail so you try again and... you fail. After try for a couple hours you finally manage to catch one.') 
        bool_choice = False 
    
    else:
        print('Invalid')
