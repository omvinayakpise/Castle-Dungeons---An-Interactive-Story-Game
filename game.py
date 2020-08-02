from os import system
from random import randint

gameTitle = 'Castle Dungeons - An Interactive Story Game'
system("mode 300, 100")
system("Title "+ gameTitle)

def cls():
    system('cls')

character_name = None
character_race = None
character_class = None
character_strength = None
character_magic = None
character_dexterity = None
character_life = None

cls()
print('Castle Dungeons - An Interactive Story Game')

def Intro():
    print('')
    print('In this Story, you are the Hero!')
    print('Your Choices, Skills, and a bit of Luck, will influence the outcome of the Game')
    print('')
    print('An Evil Sorcerer is holding your fellow adventurers as his prisoners.')
    print('Will you succeed to free your friends from the Evil Sorcerer, or perish trying!!!')
    print('')
    input('Press Enter to start the Game...')

Intro()

def create_character():
    cls()
    global character_name
    character_name = input("""
    Let's Begin by creating your Character.
    Enter the Name of your Character
    > """)

    global character_race
    while character_race is None:
        race_choice = input("""
        Choose your Character's Race from the list below by entering that relevant number:
        1 - Elf (A Supernatural Creature of folk tales, typically represented as a small, delicate, elusive figure in human form with pointed ears, magical powers, and a capricious nature.)

        2 - Dwarf (A Member of a Mythical race of short, stocky humanlike creatures in folklore or fantasy literature who are generally skilled in mining and metalworking.)

        > """)

        if race_choice == '1':
            character_race = 'Elf'
        elif race_choice == '2':
            character_race = 'Dwarf'
        else:
            print("Not a Valid Choice, Please Enter the Number Again!")

    cls()

    global character_class
    while character_class is None:
        class_choice = input("""
        Choose your Character's Class from the list below by entering that relevant number:
        1 - Warrior (A Brave or Experienced soldier or fighter.)

        2 - Wizard (A Man in Legends and Fairy tales who has magical powers.)

        > """)

        if class_choice == '1':
            character_class = 'Warrior'
        elif class_choice == '2':
            character_class = 'Wizard'
        else:
            print("Not a Valid Choice, Please Enter the Number Again!")

create_character()

def create_character_skills_sheet():
    cls()
    global character_name, character_race, character_class, character_strength, character_dexterity, character_magic, character_life
    print("""
    Now Let's determine your Character's Skills which you will use throughout the game.
    Your Character has 4 Skills:

        1) Strength - Which you will use in any Combat or Strength Test.
        2) Dexterity - Which you will use in any Ability Test.
        3) Magic - Which you will use whenever you need to Cast a Spell or Use/Inspect a Magical Item or Place
        4) Life - Which determines your Character's Energy. You will lose points when your Character gets hurt and when your Life reaches 0, Your Character Dies!!

    Depending on the Race and Class you selected in the previous window, you will have a certain point-base already calculated for your Character by the game
    However, you will shortly be able to Increase your Skills by Rolling a 6-Face Dice

    Here is your Base Skill Sheet for your Character:
    """)
    character_strength = 5
    character_magic = 0
    character_dexterity = 3
    character_life = 10

    if character_race == "Elf":
        character_strength += 3
        character_dexterity += 6
        character_magic += 4
        character_life += 2
    elif character_race == "Dwarf":
        character_strength += 5
        character_life += 4

    if character_class == "Warrior":
        character_strength += 3
        character_life += 3
    elif character_class == "Wizard":
        character_magic += 4

    print("""
    Name: """ + character_name +
    """
    Race: """ + character_race +
    """
    Class: """ + character_class +
    """

    Strength: """ + str(character_strength) +
    """
    Dexterity : """ + str(character_dexterity) +
    """
    Magic: """ + str(character_magic) +
    """
    Life: """ + str(character_life) + """

    """)
    input("Press Enter to Go Ahead!")

create_character_skills_sheet()

def modify_skills():
    cls()
    global character_strength, character_dexterity, character_life
    print("""Now you can Modify your Character's Skills Sheet by rolling a 6-Face Dice for each of your Character's Skills and the game will add your Score to the Relevant Skill.The Higher you Roll, the better stat boost your Character will recieve.""")
    print("May the Luck be with You!!!")
    print("")

    input("Press Enter to Roll your Dice to Boost Your Strength")
    roll = randint(1,6)
    print("Your Character's Strength gets booted by " + str(roll))
    character_strength = character_strength + roll
    print("")

    input("Press Enter to Roll your Dice to Boost Your Dexterity")
    roll = randint(1,6)
    print("Your Character's Dexterity gets booted by " + str(roll))
    character_dexterity = character_dexterity + roll
    print("")

    input("Press Enter to Roll your Dice to Boost Your Life")
    roll = randint(1,6)
    print("Your Character's Life gets booted by " + str(roll))
    character_life = character_life + roll
    print("")

    print("""Congratulations!!!!""")
    print("You have completed your Character Creation!")
    print("Your Character's Updated Skills Sheet:")
    print("""
    Name: """ + character_name +
    """
    Race: """ + character_race +
    """
    Class: """ + character_class +
    """

    Strength: """ + str(character_strength) +
    """
    Dexterity : """ + str(character_dexterity) +
    """
    Magic: """ + str(character_magic) +
    """
    Life: """ + str(character_life) + """

    """)

    print("")
    print("Press Enter to Begin your Adventure, if you Dare!!!!")

modify_skills()

def story_scene_1():
    cls()
    choice = None
    while choice is None:
        user_input = input("""
        You have entered the Castle Dungeons...
        It is dark, thankfully your torch is Lit and you can see upto 20 feet away from you.
        The Stone walls are damp.
        The Smell of Rats and Orcs is Strong!!!!
        You walk down a Narrow Corridor, until you reach a Thick Stone Wall

        The Corridor continues on the Left and on the Right.

        What do you do??

            1) Turn Left
            2) Turn Right

        > """)

        if user_input == '1' or user_input == 'turn left':
            choice = '1'
            story_scene_2()
        elif  user_input == '2' or user_input == 'turn right':
            choice = '2'
            story_scene_3()
        else:
            print("""Not a Valid Choice!! Please Enter the Relevant Number or 'turn left / turn right' """)



def story_scene_2():
    cls()
    choice = None
    while choice is None:
        user_input = input("""
        You Turned Left and continue walking in the Dark Corridor and suddenly you hear a Strange Voice!!!

        What do you do??

            1) Continue Walking
            2) Stop to Listen

        > """)

        if user_input == '1' or user_input == 'continue walking':
            choice = '1'
            combat()
        elif  user_input == '2' or user_input == 'stop to listen':
            choice = '2'
            skill_check()
        else:
            print("""Not a Valid Choice!! Please Enter the Relevant Number or 'continue walking / stop to listen' """)



def story_scene_3():
    cls()
    choice = None
    while choice is None:
        user_input = input("""
        You Turned Right and continue walking in the Dark Corridor but unfortunately you find a Dead End in front of You!!
        You turn back and reach the Corridor junction once again and turn Left. As you continue walking, you suddenly hear a Strange Voice!!!

        What do you do??

            1) Continue Walking
            2) Stop to Listen

        > """)

        if user_input == '1' or user_input == 'continue walking':
            choice = '1'
            combat()
        elif  user_input == '2' or user_input == 'stop to listen':
            choice = '2'
            skill_check()
        else:
            print("""Not a Valid Choice!! Please Enter the Relevant Number or 'continue walking / stop to listen' """)


def skill_check():
    cls()
    print("A Gaint Rock falls from the Ceiling, Roll a Dice to see if you can Dodge the rock??")
    roll = randint(1,6)
    print("You Rolled " + str(roll))
    print("")
    if roll + character_dexterity > 10:
        print("""You Dodge the rock and Survive!! But the Danger is not over yet..
        The Strange Noise continues and it feels alot closer now...""")
        print("")
        input("Press Enter to Continue...")
        combat()
    else:
        print("""You get Smashed by the Rock.
        You Die!!!
        Game Over""")
        print("")
        print("Press Enter to Exit the Game")


def combat():
    cls()
    global character_life
    print("A Horrible Orc Attacks you!!")
    input("Press Enter to Combat!")
    orc_life = randint(12,16)
    orc_strength = randint(12,18)
    while orc_life > 0 and character_life > 0:
        char_roll = randint(1,6)
        print("You Rolled " + str(char_roll))
        orc_roll = randint(1,6)
        if (character_strength + char_roll) > (orc_life + orc_roll):
            print("You Hit the Orc!!!")
            orc_life = orc_life - randint(1,6)
            print("")
        else:
            print("The Orc hits you!!")
            character_life = character_life - randint(1,6)

    if character_life > 0:
        print("You Defeated the Orc and successfully rescued your Friends from the Dungeons..")
        input("Press Enter to Exit the Game")
    else:
        print("The Orc Killed you and your friends are left trapped in the Dungeons")
        input("Press Enter to Exit the Game")


story_scene_1()
