from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print "This scene does not exist."
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
    
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        
        current_scene.enter()


class Death(Scene):
 
    stuff = ['Well, it was fun',
        "You don't have to go home, but....",
        "Goodbye",
        "GTFOH"]
    
    def enter(self):
        print Death.stuff[randint(0, len(self.stuff)-1)]
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print "This game is pretty lame but not easy (for me) to code"
        action = raw_input("shoot!, dodge!, or tell a joke: ")
	
	if action == "shoot!":
            print "He's too fast for you, sorry."
            return 'death'
        elif action == "dodge!":
            print "Again, he's just too fast for your."
            return 'death'
        elif action == "tell a joke":
            print "aliens with a sense of humor."
            return 'laser_weapon_armory'
        else:
            print "That was not an option, back to the beginning."
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print "Congrats, you've made it to the next stage."
        print "Now you've got to guess the correct password"
        code = "%d" % randint(1, 9)
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 15:
            print "Bzzed"
            guesses += 1
            guess = raw_input("[keypad]> ")
                
        if guess == code:
            return 'the_bridge'
        else:
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print "How are you going to put the bomb down?"
        action = raw_input("Bomb placing method: ")

        if action == "throw the bomb":
            return 'death'
        elif action == "slowly place the bomb":
            return 'escape_pod'
        else:
            print "not quite, starting this level over again."
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print "You have to guess the right pod."
        good_pod = randint(1, 3)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            return 'death'
        else:
            return 'finished'


class Finished(Scene):
    
    def enter(self):
        print "You win."
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
