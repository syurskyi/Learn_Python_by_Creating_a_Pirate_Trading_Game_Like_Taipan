import random


class PirateEncounter(object):
    def __init__(self, game):
        self.game = game
        self.pirate_risk = 80
        self.pirate_strength = 10
        self.change_for_escape = 33
        self.check_for_pirates()

    def check_for_pirates(self):
        result = random.randint(0, 100)
        if result <= self.pirate_risk:
            self.pirate_atack()

    def pirate_atack(self):
        print("**************************************")
        print("PIRATES!!!!!!!!!!!!!!!!!!!")
        print("**************************************")
        self.number_of_pirates = random.randint(1, self.pirate_strength)
        FightingPirates = True
        while FightingPirates:
            print("------------------------------------")
            print("There are %s pirates remaining." % self.number_of_pirates)
            print("You have %s cannons and your ship health is %s" % (self.game.cannons, self.game.ship_health))
            print("")
            attack_input = input("What do you wish to do? R)un or F)ight?")
            if attack_input.upper() == "R":      # True if you got away
                if self.run():
                    FightingPirates = False
            if attack_input.upper() == "F":
                if self.fight():                  # True if the fight is over
                    FightingPirates = False
            self.ship_damage()

            print("Press any key to continue")

    def ship_damage(self):
        damage = random.randint(0, self.number_of_pirates*2)
        self.game.ship_health -= damage
        if damage <= 0:
            print("SHIP DESTROYED!!!")

    def fight(self):
        fight_strengh = 1 if self.game.cannons == 0 else self.cannons + 1
        attack = random.randint(0, fight_strengh+1)
        pirate_killed = attack if self.number_of_pirates >= attack else self.number_of_pirates
        self.number_of_pirates -= pirate_killed
        if self.number_of_pirates <= 0:
            return True
        else:
            return False

    def run(self):
        print("You try to run")
        result = random.randint(0, 100)
        if result <= self.change_for_escape:
            print("You escaped!")
            return True
        else:
            print("You didn't get away")
            return False
        input("continue")