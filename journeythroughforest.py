#C:\Users\Developer\Documents\PythonProjects\LPTHW\Ex34-39_Advance\Ex36\
import sys
import random

PROMPT = ">>"
NOT_A_CHOICE = "Thats is NOT a choice. Try Again\n\n"
CHOICE_OPTIONS = "1 2".split(" ")
CHOICE_OPTIONS_TRI = "1 2 3".split(" ")

#=====================================
#               UTILS
#=====================================

def die(reason):
    print "You Died!"
    print reason
    sys.exit(0)

def dottedline():
    print "---------------------------"

def pause():
    print "Press [ENTER] to continue..."
    raw_input()
    dottedline()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





















#=====================================
#               START/END
#=====================================

def intro():
    print "It's summer time. The sun is out. The days are long."
    print "One day you decide to take a trip to one of your favorite places."
    print "The Forest."
    pause()

    print "You decide you want to make this trip special and test your survival skills."
    print "You only take a few things. You take a canister, knife, fishing rod, compass, and watch."
    print "You pack your things in a backpack and head out."
    pause()

    print "You drive towards the forest. Your heart races as you think about the exciting adventure."
    print "You park your car a few feet away from the entrance of the forest."
    print "You get your things and walk to the entrance of the forest."
    print "You take a deep breath. Your journey begins..... "
    pause()

    choiceone_entrance()

def choiceone_entrance():
    choice = ""

    print "You head down the path. You take in the fresh air."
    print "You stop and look up at a tree. The tree makes you seem so small and insignicant."
    print "You spot a bird sitting in the tree. You listen to its beautiful song."
    pause()

    print "You continue down the path. You see many different plants and trees."
    print "You play a game with yourself to try to name the different plants and animals."
    print "A few minutes later you come up on a fork."
    pause()

    while choice not in CHOICE_OPTIONS:
        print "You stop at the fork in the road."
        print "There is a path that leads right and one that leads straight."
        print "You ponder on a choice. Which one do you choose?"

        dottedline()
        print "(1) Go Right"
        print "(2) Keep Straight"
        dottedline()

        choice = raw_input(PROMPT)

        if choice == "1":
            cabin()
        elif choice == "2":
            bear()
        else:
            print NOT_A_CHOICE

def end():
    print "You continue down the path."
    print "The sun begins to set. It looks like the end of your journey"
    print "You stop take in everything. You ponder...."
    print "To be continue..............................................."

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
























#=====================================
#            LEFT OF MAP
#=====================================

def cabin():
    choice = ""

    print "You choose to go right. You hope you picked the right choice. "
    print "Looking around you see alot of trees and foliage. Green is your favorite color."
    print "A few minutes you spot a shape in the distance."
    pause()

    print "You come close to the shape. You see it is a cabin."
    print "The cabin is a small cabin. You slowly walk up to  the window."
    print "You peek inside. Everythings dark. It seems no one is home."
    pause()

    while choice not in CHOICE_OPTIONS:
        print "You check all around the cabin. Everything looks tidy and neat"
        print "You yell out hello. No soul seems to answer."
        print "You think to yourself 'I dont remember this cabin'. Then again you havent been to the forest in a while."
        print "You ponder. What should you do?"


        dottedline()
        print "(1) Go in the cabin"
        print "(2) Leave the cabin. Continue down the path."
        dottedline()

        choice = raw_input(PROMPT)

        if choice == "1":
            inside_cabin()
        elif choice == "2":
            northbeach()
        else:
            print NOT_A_CHOICE

def inside_cabin():
    print "SOON TO BE IMPLEMENTED"
    return

def northbeach():
    choice = ""

    print "You decide to pass on the cabin. You continue the path."
    print "As your walking the air starts to smell and taste salty."
    print "The smell intrigues you. You stop, take in the fresh air."
    pause()

    print "As you continue the smell gets stronger. You start to hear something in the background."
    print "Continuing walking the sound gets louder. Its the sound of waves."
    print "You walk faster, eager to see whats at the end of the path."
    pause()

    print "You slow down and come to a stop. You take off your shoes."
    print "You curl your toes in the sand. The sand feels good on your feet."
    print "You look around. Water for miles. The wind blowing easy on your face."
    print "You walk down to where the tide is rising."
    pause()

    print "The water splashes at your legs. The water is cold."
    print "The salty air is pungent now."
    print "You continue further down the beach"
    pause()

    print "As you walk along the beach you look on it."
    print "The ground is so soft and smooth."
    print "Further in front of you you see an object on the beach. You go close to investigate."
    pause()

    while choice not in CHOICE_OPTIONS:
        print "As you get close you see its a canoe."
        print "'Wow someone left this' you say to yourself."
        print "You examine the canoe. It seems to be in good shape."
        print "You look out into the water and ponder. What do you do?"

        dottedline()
        print "(1) Fish"
        print "(2) Take the canoe into the water"
        dottedline()

        choice = raw_input(PROMPT)

        if choice == "1":
            fish()
            choice = ""
        elif choice == "2":
            southbeach()
        else:
            print NOT_A_CHOICE

def fish():
    fishcaught = 0
    keepfishing = "y"

    while keepfishing == "y":
        getfish = random.randrange(0, 100)

        if getfish < 100/2:
            fishcaught += 1
            print "You got a fish! Good job!"
        else:
            print "Sorry, You didnt get a fish"

        print "Keep going (y/n)"
        keepfishing = raw_input(PROMPT)

    print "You caught %d fish" % fishcaught
    pause()

def southbeach():
    choice = ""
    print "You take the canoe in the water. Good thing it has a paddle."
    print "As you row you look in the water. It's a nice blue color."
    print "Blue is you second favorite color. You continue rowing."
    pause()

    print "You land ashore another beach. You're glad you made it to land safely."
    print "You pull the canoe on land. And lay down. You feel the soft, warm sand comfort you."
    print "The breeze on your face feels good. It whispers in your ear."
    pause()

    while choice not in CHOICE_OPTIONS:
        print "You get up. look around. You find a path."
        print "You think to yourself. Should I continue or fish?."
        print "You ponder. What are you going to do."

        dottedline()
        print "(1) Fish"
        print "(2) Continue down path"
        dottedline()

        choice = raw_input(PROMPT)

        if choice == "1":
            fish()
            choice = ""
        elif choice == "2":
            end()
        else:
            print NOT_A_CHOICE

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
























#=====================================
#            RIGHT OF MAP
#=====================================

def bear():
    choice = ""

    print "You decide to keep it simple and continue straight."
    print "You observe the surrounding wilderness as you walk. So many plants and animals"
    print "You see birds, deer, beavers,  skunks."
    pause()

    print "You turn a curve and stop to take a rest."
    print "You take out your canister and drink some water."
    print "You find a place near some berry bushes on the side of the road to rest."
    pause()

    print "After a few minutes you hear a sound. An inaudible sound."
    print "You jump up and look around frantically. You see nothing. You laugh at yourself."
    print "You sit back down. again a sound, but louder."
    pause()

    while choice not in CHOICE_OPTIONS_TRI:
        print "You turn around and right there standing 9 feet tall is a Grizzly."
        print "You jump up and rush to the other side of the road scared. The Grizzly enters the dirt stage from behind the bushes"
        print "You breath hysterically. You ponder. What are you gonna do?"


        dottedline()
        print "(1) Run"
        print "(2) Throw berries at bear"
        print "(3) Punch bear"
        dottedline()

        choice = raw_input(PROMPT)

        END_RANGE = 100
        fate = random.randrange(0, END_RANGE)

        if choice == "1":
            print "You run as fast as you can. Actually you run faster than as fast as you can."

            #Less than half means you live. Greater than equal to means you die.
            if fate < END_RANGE/2:
                print "Miraculously, the bear ignores you and you get away safely."
                pause()
                animalstuck()
            else:
                print "The bear engages. You look back and run faster. Your efforts fail."
                die("Eaten by bear!")

        elif choice == "2":
            print "Bears like berries right? You find out. You grab a handful of berries and throw it to the bear."

            #Less than half means you live. Greater than equal to means you die.
            if fate < END_RANGE/2:
                print "The bear takes interest in the berries and starts to eat them. You make your getaway."
                pause()
                animalstuck()
            else:
                print "The bear roars and gets angry. You threatened it. The bear charges at you. You try to run but its too late."
                die("Eaten by bear!")

        elif choice == "3":
            print "You think to yourself 'I ain't scared of no bear. Im a man!'. You roll up your sleeves and fight the bear."

            #Less than half means you live. Greater than equal to means you die.
            if fate < END_RANGE/2:
                print "After an epic duel the bear gives up. You're dirty, tired, but you just won a fight with a bear."
                pause()
                animalstuck()
            else:
                print "You punch and kick the bear but the bear shrugs them off. The bear laughs at you and thinks 'Stupid human'. You realize its over."
                die("Eaten by bear!")

        else:
            print NOT_A_CHOICE

def animalstuck():
    choice = ""

    print "You feel invincible escaping from the bear attack."
    print "You stroll along with a big smile on your face."
    print "Now you can tell all your friends you survived a bear attack."
    pause()

    print "As you go along the path you hear another noise."
    print "'Not another bear' you cry out. You look around."
    print "The sound comes again. Its more higher pitched. more like a whimper."
    pause()

    while choice not in CHOICE_OPTIONS:
        print "The sound comes louder this time. clear as day. You stop"
        print "You look up and see a fox trapped in a net. It squels in pain."
        print "You ponder. Do you feel like a hero today? What do you do?"

        dottedline()
        print "(1) Cut down the trap"
        print "(2) Ignore the fox"
        dottedline()

        choice = raw_input(PROMPT)

        if choice == "1":
            print "You get your knife out. You climb the tree and cut the fox down."
            print "The fox lays there for a second still. You hope it isnt hurt."

            foxhurt = random.randrange(0, 100)

            #If less than 50 you saved the fox.
            if foxhurt < 100/2:
                print "10 minutes go by. The fox begins to move."
                print "The fox looks up at you and licks your face in gratitude."
                print "The fox gets up. walks away. It doesn't look to be hurt. You saved it."
                pause()

                robbed(True)
            else:
                print "10 minute go by. Then 20. Then 30"
                print "You try to wake the fox up but he does awake."
                print "You were too late. You failed. The fox is dead."
                pause()

                robbed(False)
        elif choice == "2":
            print "You arent feeling heroic today. You dont want to get in trouble with a hunter either."
            print "You sigh and continue on your way."
            pause()

            robbed(False)
        else:
            print NOT_A_CHOICE

def robbed(savedAnimal):
    choice = ""

    if savedAnimal == True:
        print "You just saved an animal and survived a bear attack. You're feellin pretty good about yourself."
        print "This adventure has been very exciting so far."
    else:
        print "You got attacked by a bear and you failed to save an animal. You aren't feeling too happy."
        print "This adventure has been hectic so far."

    print "You contiue walking down the path."
    pause()

    while choice not in CHOICE_OPTIONS:
        print "As your strolling along you here russling of leaves. 'What now!?!?' you tell yourself"
        print "Suddenly a man jumps out from the bushes and yells 'Don't scream. Gimme all yer stuff or I'll shootcha."
        print "He points an old revolver at ya. You ponder. What do you do?"

        dottedline()
        print "(1) Disarm man. Attack man."
        print "(2) Give him your stuff."
        dottedline()

        choice = raw_input(PROMPT)

        survivedrobbing = random.randrange(0, 100)

        if choice == "1":
            print "You survived a bear attack, surely you can survive being robbed."
            print "You charge at the man. Grab his gun."
            pause()

            #If less than 50 you survived
            if survivedrobbing < 100/2:
                print "You disarm him. and wreslt him to the ground."
                print "You hit him in the head with the gun and he falls unconcious."
                print "You rob him of his things and run away."
                pause()
            else:
                print "You struggle to disarm him. You fight and fight but he is too strong."
                print "Guess you can't survive a robbing. The man pushes you off him and takes aim."
                die("Shot by robber")

        elif choice == "2":
            print "You tell him you dont want any trounble. You hand him everything you have"
            print "He checks your things. He stops, smiles and looks at you."
            print "'You got some pretty good stuff here' the man says"
            pause()

            #If less than 50 you survived
            if survivedrobbing < 100/2:
                print "he continues, 'Today's your lucky day. Ill let you live. Go! Get outta here!'"
                print "You dont waste one minute. You scram."
                pause()
            else:
                print "he continues, 'Cant have you coming after me now.'"
                print "He takes aim at you. You try to run but its too late. "
                die("Shot by robber")
        else:
            print NOT_A_CHOICE

        print "You run down the path. You dont want any more trouble."
        print "This was the biggest adventure you've ever had."
        pause()

        end()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~






























##########################################################################################################################
intro()
##########################################################################################################################
