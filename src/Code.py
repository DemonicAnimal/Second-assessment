import time

bool_choice = True
str_userChoice = ""

print("Welcome to my text adventure game!")
time.sleep(2.5)
print("For every decision there will only be ONE correct awnser, choose wisely...")
time.sleep(2.5)
print(
    "If you do make a wrong decision I wont force you to restart im not that mean. (pinky promise)"
)
time.sleep(2.5)
print("To make a decision input either 1,2,3,4, etc.\n")
time.sleep(2.5)

print("You wake up in the forest as the sun rises in the distance.")
time.sleep(2.5)
print("You have no idea how you got here...")
time.sleep(2.5)
print(
    "After taking awhile to think you decide there are four main things you should do.\n"
)
time.sleep(2.5)

print("(1) Search for civilization.")
time.sleep(2.5)
print("(2) Search for food.")
time.sleep(2.5)
print("(3) Search for water.")
time.sleep(2.5)
print("(4) Search for shelter.")
time.sleep(2.5)

while bool_choice is True:

    str_userChoice = input("\nWhat will you do?\n")
    time.sleep(1.0)

    if str_userChoice == "1":
        print(
            "You search for hours trees and bushes begin to blur as you go deeper and deeper into the forest eventually it gets to dark to see. you hear a roar behind you and sprint in the other direction quickly hitting a tree, you pass out instantly and your body is devoured by morning.\nYou died, try again."
        )
        bool_choice = True

    elif str_userChoice == "2":
        print(
            "You see an apple tree nearby you climb it hoping to pick some apples... but sadly when reaching for an apple you slip and land head first on the ground below cracking your skull on a rock.\nYou died, try again."
        )
        bool_choice = True

    elif str_userChoice == "3":
        print(
            "After awhile of walking through trees you find a small lake, fish swim inside causing the water to ripple."
        )
        bool_choice = False

    elif str_userChoice == "4":
        print(
            "After a quick search you find a cave and run inside after a short examination a bear tears you limb from limb.\nYou died, try again."
        )
        bool_choice = True

    else:
        print("Invalid")

pass

time.sleep(2.5)
print("\nYou sit by the lake taking some time to think.")
time.sleep(2.5)
print(
    "As you sit and ponder by the lake time flys by you dont even notice as you sit there from dawn till dusk."
)
time.sleep(2.5)
print(
    "When you finally notice the time you realize you need to find shelter IMMEDIATELY."
)
time.sleep(2.5)
print("After a quick look around your surroundings you see a few possible options.\n")
time.sleep(2.5)

print("(1) A cave not far from the lake.")
time.sleep(2.5)
print("(2) A small ditch covered by the leaves and branches of a fallen tree.")
time.sleep(2.5)
print("(3) A clump of trees shrubs and foliage.")
time.sleep(2.5)

while bool_choice is False:

    str_userChoice = input("\nWhich shelter would be best?\n")
    time.sleep(1.0)

    if str_userChoice == "1":
        print(
            "As you enter the cave you get a strange feeling of deja vu its short lived however as your are quickly torn apart by a bear.\nYou died, try again."
        )
        bool_choice = False

    elif str_userChoice == "2":
        print(
            "You manage to get inside the small ditch its uncomfortable but warm you decide to try get some rest, it would be difficult in the small space if you werent so tired. The next morning you wake uncomfortable and unrested atleast your alive... you crawl out from the ditch and stretch but your whole body starts to cramp in protest, a beautiful morning light glimmers off the water as the sun rises."
        )
        bool_choice = True

    elif str_userChoice == "3":
        print(
            "As you settle inside the clump you quickly fall asleep exhausted... sadly the clump wasnt a good enough shelter and you died from hypothermia in your sleep.\nYou died, try again."
        )
        bool_choice = False

    else:
        print("Invalid")

pass

time.sleep(2.5)
print(
    "Quickly afterwards you realize how thirsty you are... come to think of it you havent eaten anything or drank anything for almost two days."
)
time.sleep(2.5)
print(
    "You walk over to the lake cup your hands and collect some water you then put your face upto your hands and take a sip."
)
time.sleep(2.5)
print(
    "The water is quite refreshing you take a few more sips until your satisfied then you need to solve the food problem..."
)
time.sleep(2.5)
print("After taking a moment to think you come up with a few options.\n")
time.sleep(2.5)

print("(1) Set a trap.")
time.sleep(2.5)
print("(2) Try to hunt something.")
time.sleep(2.5)
print("(3) Scavenge for food.")
time.sleep(2.5)
print("(4) Fish in the lake.")
time.sleep(2.5)

while bool_choice is True:

    str_userChoice = input("\nWhat will you do?\n")
    time.sleep(1.0)

    if str_userChoice == "1":
        print(
            "You set out to find something to make a trap with, after searching for awhile you are unable to find anything and head back to the lake.\nTry again."
        )
        bool_choice = True

    elif str_userChoice == "2":
        print(
            "You try to make some kind of makeshift spear using a tough branch a sharpened stone and some flax its flimsy but looks like it will work. You head out into the forest and try to find something after awhile you find a buck you sneak up behind it and stab it through the stomach it goes through but its not quite enough the enraged deer turns to you and gores you before collapsing.\nYou died, try again."
        )
        bool_choice = True

    elif str_userChoice == "3":
        print(
            "After heading out into the forest you quickly find a recently killed doe, the deer looks fresh you would just need to cook it. You grab its leg and start dragging it back to the lake, however the nearby hungry pack of wolves doesnt appreciate you stealing their recent kill three large wolves jump at you and tear you apart.\nYou died, try again."
        )
        bool_choice = True

    elif str_userChoice == "4":
        print(
            "you craft a makeshift spear using a tough branch a sharpened stone and some flax its flimsy but looks like it will work. You sit by the lake and try to stab a fish you fail so you try again and... you fail. After try for a couple hours you finally manage to catch one."
        )
        bool_choice = False

    else:
        print("Invalid")

pass

time.sleep(2.5)
print(
    "You quickly find some leaves and branches and bring them back to the lake. Using a nearby piece of flint and a discarded scrap of steel you start a fire after a couple attempts you manage to start a fire."
)
time.sleep(2.5)
print(
    "Afterwards you find some more sturdy branches and make some kind of spitroast that you spear the fish on."
)
time.sleep(2.5)
print(
    "you sit by the fire waiting for it to cook, after waiting around 20 minutes it looks ready."
)
time.sleep(2.5)
print(
    "You take it off the fire and wait for it to cool down a bit, after another 20ish minutes it feel cool enough to touch. You then debone the fish and eat as much as you can, after you throw the waste in the water."
)
time.sleep(2.5)
print("You decide to try to improve your shelter or maybe find a new one.\n")
time.sleep(2.5)

print("(1) Dig the shelter bigger to improve your breathing room.")
time.sleep(2.5)
print("(2) Check out the cave near the lake.")
time.sleep(2.5)
print("(3) Try to build some kind of cabin.")
time.sleep(2.5)
print("(4) Do a wider search.")
time.sleep(2.5)

while bool_choice is False:

    str_userChoice = input("\nWhat will you do?\n")
    time.sleep(1.0)

    if str_userChoice == "1":
        print(
            "You find a sturdy chunk of bark and use that to dig after alot of effort you manage to dig and toss out alot of dirt leaving you with alot more room."
        )
        bool_choice = True

    elif str_userChoice == "2":
        print(
            "As you enter the cave you get a bad feeling of deja vu, you swallow and go deeper anyway where you are quickly torn apart by a bear\nYou died, try again."
        )
        bool_choice = False

    elif str_userChoice == "3":
        print(
            "You find a sturdy branch and a sharp flat stone you tie them using flax and tree sap you try to chop done a tree the axe breaks after awhile but makes a good effort on the tree. So you repeat the process again, and again, and again, and again... after alot of effort you finally have enough wood! Its getting dark though... you try to make the cabin ASAP but in the process it colapses ontop of you luckily you survive! However the baying wolves smell your blood...\nYou died, try again."
        )
        bool_choice = False

    elif str_userChoice == "4":
        print(
            "After venturing far from the lake you find... absolutely nothing, you head back to the lake but sadly on the way you slip off a cliff\nYou died, try again."
        )
        bool_choice = False

    else:
        print("Invalid")

pass

print("Seeing how late it is you decide to test your improved shelter.")
time.sleep(2.5)
print("The next couple days you just focus on surviving and adapting.")
time.sleep(2.5)
print(
    "Over the next couple days you start to feel more and more confident about what you can and cant do."
)
time.sleep(2.5)
print("But you still need to figure out how to get back to civilization...\n")
time.sleep(2.5)

print("(1) Walk in one direction for long enough and hope for the best.")
time.sleep(2.5)
print("(2) Climb a tall hill to try a good veiw of the surrounding area.")
time.sleep(2.5)
print("(3) Find a river and follow it upwards until you find civilization.")
time.sleep(2.5)
print("(4) Go from place to place and hope to eventually find something.")
time.sleep(2.5)
print("(5) Just continue focusing on survival")
time.sleep(2.5)

while bool_choice is True:

    str_userChoice = input("\nWhat will you do?\n")
    time.sleep(1.0)

    if str_userChoice == "1":
        print(
            "You head what you assume is straight north only diverging from your path to dodge obstacles it starts to get dark you think about stopping but decide not to. after another couple hours of walking it becomes impossible to see soon after you fall off a cliff.\nYou died, try again."
        )
        bool_choice = True

    elif str_userChoice == "2":
        print(
            "You head up the hill after an hour or so you reach the top, you cant seem to see much from the top. You decide to head back to the lake and think of a new plan, After carefully making your way down you return to the lake.\nTry again."
        )
        bool_choice = True

    elif str_userChoice == "3":
        print(
            "After walking for awhile you find a river, you then follow it upwards hoping to find some kind of civilization eventually. Sadly your journey is cut short when an alligator pulls you underwater and tears you apart.\nYou died, try again."
        )
        bool_choice = True

    elif str_userChoice == "4":
        print(
            "You set out on your journey going from place to place trying to make do with whatever shelter and food you can find."
        )
        bool_choice = False

    elif str_userChoice == "5":
        print(
            "You live for a few years before dying to the common cold.\nYou died, try again"
        )
        bool_choice = True

    else:
        print("Invalid")

pass

print("One day as your wandering you get a bad feeling.")
time.sleep(2.5)
print("As night falls you realize why.")
time.sleep(2.5)
print(
    "Its extremely cold! you desperately need a good shelter or somewhere safe to light a fire."
)
time.sleep(2.5)

print("(1) Light a fire out in the open.")
time.sleep(2.5)
print("(2) Go inside a nearby cave and light a fire.")
time.sleep(2.5)
print("(3) Keep going and hope to find something better.")
time.sleep(2.5)
print("(4) A tree with overhanging roots.")
time.sleep(2.5)

while bool_choice is False:

    str_userChoice = input("\nWhat will you do?\n")
    time.sleep(1.0)

    if str_userChoice == "1":
        print(
            "You collect a bunch of sticks logs and other kindling, you then light a fire, after awhile you hear howling.\nYou died, try again."
        )
        bool_choice = False

    elif str_userChoice == "2":
        print(
            "You gather some kindling and head into the cave, you head to the very back and light a fire. You lie down and quickly fall asleep next to the hot fire."
        )
        bool_choice = True

    elif str_userChoice == "3":
        print(
            "After walking for awhile you manage to find a rundown cabin, you head inside and find a warm bed you lie down and go to bed. you fall asleep warm and cozy however the bed is not warm enough and you die from hypothermia as the night gets colder.\nYou died, try again."
        )
        bool_choice = False

    elif str_userChoice == "4":
        print(
            "You quickly find some branches sticks and leaves to make a small hut looking thing that covers the parts the roots dont. You crawl inside in warm enough and cozy so you decide to get some rest, but sadly the night gets alot colder and you dont survive.\nYou died, try again."
        )
        bool_choice = False

    else:
        print("Invalid")

pass

print("After waking up you keep on moving going from place to place.")
time.sleep(2.5)
print("after a few hours you find an abandoned village, it looks ancient...")
time.sleep(2.5)
print(
    "You decide to head into the village, after taking a moment to think you head into the first house along the second row."
)
time.sleep(2.5)
print(
    "Shortly after you find some... canned food? maybe this village isnt as ancient as you thought..."
)
time.sleep(2.5)
print("You head outside and think about what house to head in next.")
time.sleep(2.5)

print("(1)")
time.sleep(2.5)
print("(2)")
time.sleep(2.5)
print("(3)")
time.sleep(2.5)
print("(4)")
time.sleep(2.5)
