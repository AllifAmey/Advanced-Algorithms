from random import *
from time import sleep

"""Here I will experiment with classes and objects"""

"""The idea here is to create a CLI game pitting the player against enemy AI.
    Through the use of numbers we will mimic the damage and health of characters."""

#Basics to be expanded upon.

# random name generator.

def random_name():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_capital = alphabet.upper()
    word_length = randint(3,10)
    word = ""

    for iteration in list(range(0, word_length)):
        random_letter = randint(0, len(alphabet)-1)
        letter_shape = randint(0,1)
        if letter_shape == 0:
            word += alphabet[random_letter]
        else:
            word += alphabet_capital[random_letter]

    return word

#calculate dmg using user and enemy's defence.
def calculate_dmg(defence):


#intro
print("In a world where demons and elves reek death and destruction upon the world...")
sleep(1)
print("There can only be one that will arise amidst the choas brewing from the underworld.")
sleep(0.5)
print("""Today is the day. You, champion, shall wreck havoc and despair upon these tormentors of the world.
What shall your hero's name be, wise one?
""")
user_name = input()
enemy_name = random_name()

print("Your first test shall be against this mere "
      + enemy_name
      + "."
      + """\nSlay him and you shall be granted the title.
%s the Great.
""" % (user_name))
#battle
max_hp = 100
user_hp = 100
enemy_hp = 100
user_def = 10
enemy_def = 10
user_dmg = 5
def_enemy = 100
def_player = 100

while not(user_hp <= 0 or enemy_hp <= 0) :
    print("""   %s health: %d
    %s defence: %d
    
    %s health: %d
    %s defence: %d
    """ % (user_name, user_hp, user_name, user_def, enemy_name, enemy_hp, enemy_name, enemy_def))
    while True:
        print("You have 2 options: attack or heal. Type the prefered action.")
        user_action = input()
        if user_action == "attack":
            #attack system.
            enemy_hp -= user_dmg
            if enemy_hp <= 0:
                print("The enemy has been slained. Congratulations, hero.")
                sleep(1)
                print("The world shall perish at the hands of %s the Great\n",
                      "as it is you who will cleanse this world of choas" % (user_name))
            break
        elif user_action == "heal":
            #healing system.
            heal = 5
            if user_hp == 100:
                print("You're already full hp. You have wasted an action.")
            elif user_hp <= 96:
                user_hp = 100
            else:
                user_hp += heal
            break
        else:
            print("Please type the 'attack' or 'heal' to proceed.")
    enemy_dmg = randrange(0, 10)
    user_hp -= enemy_dmg

    print("The enemy STRIKES YOU!")

"""


class enemy():
    \"""Enemy Status: hp,df. Enemy dmg: dmg. Damage system determined by randomisation between 5-10\"""


    def __init__(self,hp,df, dmg):
        self.hp = hp
        self.df = df
        self.dmg = dmg

    def generate_dmg(self):
        self.dmg = random.randrange(5,10)

    def Defence(self):
        pass
"""
