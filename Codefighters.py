from sys import exit
from random import randint
from textwrap import dedent

class Power(object):
    life_points = 25
    bison_life_points = 30

    attacks = ['A','B','C']

    codefighter =[
    'Bison couldnt block your attack and takes damage.',
    'Bison thought your attack wouldnt work on him and takes damage.',
    'You added an extra energy pulse to your attack.',
    'You manage to add  an extras few  attack moves on Bison'
    ]

    bison = [
    'Bison blocks your attack and counters it with a right hook.',
    'Bison moves to the side and knees you in the face.',
    'Bison Blocks your attack and does a scissor kick to your head ',
    'Bison teleports behind you and does psycho burst.',
    'Bison doesn\'t feel your attack and head butts you in the fore head.'
    ]

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('winner')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Defeated(object):

    quips = [
        "You been defeated.",
        "You were to weak for Bison.",
        "You have been knocked out.",
        "I expected more from you.",
        "I thought you would be stronger."
        ]

    def enter(self):
        print(Defeated.quips[randint(0, len(self.quips)-1)])
        exit(1)

class FightDecision(object):

    def enter(self):
        print(dedent("""
            Bison has invaded your village and has became its ruler.
            You return home and find that you are the last surviving
            protector that could save the village. The only way you
            can save the village is if you are able to defeat Bison
            in combat to over throw his position in power.

            What do you do when you encounter Bison face to face?
            A. "Request to fight Bison directly in public"
            B. "Attack him directly in public."
            C. "Run away from the town."
            """))

        action = input("> ")

        if action == "A":
            print(dedent("""
                He laughs at you and accepts your request to fight.
                """))
            return 'fight_arena'

        elif action == "B":
            print(dedent("""
                He dodges your attack and counters it with a single
                punch.You fall to the ground unconscious and his
                henchmen carry you to a prison cell,where you will spend
                the rest of your life. He walks away laughing.
                """))
            exit(1)

        elif action == "C":
            print(dedent("""
                You decide you will go back to the village once you are
                strong enough to defeat Bison.Save the fight for another day.
                """))
            exit(1)

        else:
            print("You hesitated with your actions,you take another action.")
            return 'fight_decision'

class FightArena(object):

    def enter(self):
        print(dedent("""
            You have entered the fight arena choose your moves carefully
            when fighting Bison. Your life points is equal to 25 and
            have three major moves.Bison life points is equal 30 and tends
            to counter your attacks with his own.Dont let your let life points
            reach zero or below, are you will be defeated.

            Choose your three major moves
            A.'Power Punch'
            B.'Power kicks'
            C.'Energy power ball'
             """))

        return 'attack'

class Attack(Power):

    def enter(self):
        attack = (Power.attacks[randint(0, len(self.attacks)-1)])

        if Power.bison_life_points <= 0:
            return 'winner'
        elif Power.life_points <= 0:
            return 'defeated'
        else:
            move = input("Action>>:")
            while move != attack and Power.bison_life_points > 0 and Power.life_points > 0:
                print(Power.bison[randint(0, len(self.bison)-1)])
                Power.life_points -= randint(1,9)
                print("My life points:",Power.life_points,"Bison life points",Power.bison_life_points,"\n")
                return 'attack'

            while move == attack and Power.bison_life_points > 0 and Power.life_points > 0:
                print(Power.codefighter[randint(0, len(self.codefighter)-1)])
                Power.bison_life_points -= randint(1,10)
                print("My life points:",Power.life_points,"Bison life points",Power.bison_life_points,"\n")
                return 'attack'

class Winner(object):

    def enter(self):
        print(dedent("""
        You have defeat Bison and saved the villagers.Bison henchmen
        managed to escape with Bison body and bought him to a safer location.
        -------------------------------------------------------------------
        You are assigned as the new leader of the village and formed a new
        alliance with other villages. Bison wont be coming back any time soon
        """))

        return 'winner'

class Map(object):

    scenes = {
        'fight_decision': FightDecision(),
        'fight_arena': FightArena(),
        'attack': Attack(),
        'defeated': Defeated(),
        'winner': Winner(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    # Uses dictionary to call key names to return Classes
    def next_scene(self, scene_name):
        location = Map.scenes.get(scene_name)
        return location

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('fight_decision')
a_game = Engine(a_map)
a_game.play()
