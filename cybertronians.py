
class Transformer(object):
    def __init__(self, name, vehicle_mode, voice_actor):
        self.vehicle_mode = vehicle_mode
        self.name = name
	self.voice_actor = voice_actor

    def results(self):
        print self.name
        print self.get_team()
        print "{0}\n{1}\n{2}".format(self.vehicle_mode, self.morality, self.voice_actor)

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

bumblebee = Autobot("Bumblebee", "Volkswagon Beetle", "Dan Gilvezan")
starscream = Decepticon("Starscream", "F-15 Eagle", "Christopher Collins")
shockwave = Decepticon("Shockwave", "Mazda RX-8", "Corey Burton")
ratchet = Autobot("Ratchet", "Ambulance", "Don Messick")
brawl = Decepticon("Brawl", "Leopard 1", "Tony St James")
jazz = Autobot("Jazz", "Porsche 935", "Scatman Crothers")
cliffjumper = Autobot("Cliffjumper", "Porsche 924", "Casey Kasem")
bonecrusher = Decepticon("Bonecrusher", "Bulldozer", "Neil Ross")
ironhide = Autobot("Ironhide", "Nissan C20 Vanette", "Peter Cullen")
breakdown = Decepticon("Breakdown", "Lamborghini Countach", "Alan Oppenheimer")

bumblebee.results()
print
starscream.results()
print
shockwave.results()
print
ratchet.results()
print
brawl.results()
print
jazz.results()
print
cliffjumper.results()
print
bonecrusher.results()
print
ironhide.results()
print
breakdown.results()
