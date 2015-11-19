from sys import exit
from random import randint

class Scene(object):
     
      def enter(self):
          print "This scene is not yet configured,Subclass it and implement enter()."
              exit(1)

class Engine(object):

      def __init__(self, scene_map):
          self.scene_map = acene_map
          
      def play(self):
          current_scene = self.scene_map.opening_scene()
          
          while True:
              print "\n--------"
              next_scene_name = current_scene.enter()
              
class Death(Scene):
     
      quips = [
         "You died. You kinda suck at this.",
          "Your mom would be proud...if she were smarter.",
          "Such a luser.",
          "I have a small puppy that's better at this."
      ]
      
      def enter(self):
          print Death.quips[randint(0, len(self.quips)-1)]
          exit(1)

class CentralCorridor(Scene):

      def enter(self):
          print ""
          print ""
          print ""
          print ""
          print ""
          print ""
          print ""print ""
          
class LaserWeaponArmory(Scene):
      
      def enter(self):
          pass
          
class TheBrage(Scene):

      def enter(self):
          pass
          
class Map(object):

      def __init__(self, start_scene):
          pass
         
      def next_scene(self, scene_name);
          pass
          
      def opening_scene(self):
          pass
          
a_map = Map('central_corridor') 
a_game = Engine(a_map)
a_game.play()
