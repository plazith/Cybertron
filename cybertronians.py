
class Transformer(object):
    def __init__(self, name, vehicle_mode):
        self.vehicle_mode = vehicle_mode
        self.name = name

    def results(self):
        print self.name
        print self.get_team()
        print "{0}\n{1}".format(self.vehicle_mode, self.morality)

    def get_team(self):
      """Return the name of the instance class

      example:

      >>> from cybertronians import Autobot
      >>> bumblebee = Autobot("Bumblebee", "Volkswagon Beetle")
      >>> print bumblebee.get_team()
      Autobot
      """
      return self.__class__.__name__

class Decepticon(Transformer):
    morality = "evil"


class Autobot(Transformer):
    morality = "good"

bumblebee = Autobot("Bumblebee", "Volkswagon Beetle")
starscream = Decepticon("Starscream", "F-15 Eagle")

bumblebee.results()
print "\n"
starscream.results()
