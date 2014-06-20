class Village(object):

    def __init__(self):
        self._decepticons = []
        self._autobots = []

    def __str__(self):
        return "A Cybertronian Village with {0} Autobot(s) and {1} Decepticon(s).\n".format(len(self._autobots), len(self._decepticons))

    def add(self, cybertronian):
        if cybertronian.get_team() == "Autobot":
          self._autobots.append(cybertronian)

        if cybertronian.get_team() == "Decepticon":
          self._decepticons.append(cybertronian)

    def get_decepticons(self):
        return self._decepticons

    def get_autobots(self):
        return self._autobots

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

village = Village()
village.add(Autobot("Bumblebee", "Volkswagon Beetle", "Dan Gilvezan"))
village.add(Decepticon("Starscream", "F-15 Eagle", "Christopher Collins"))
village.add(Decepticon("Shockwave", "Mazda RX-8", "Corey Burton"))
village.add(Autobot("Ratchet", "Ambulance", "Don Messick"))
village.add(Decepticon("Brawl", "Leopard 1", "Tony St James"))
village.add(Autobot("Jazz", "Porsche 935", "Scatman Crothers"))
village.add(Autobot("Cliffjumper", "Porsche 924", "Casey Kasem"))
village.add(Decepticon("Bonecrusher", "Bulldozer", "Neil Ross"))
village.add(Autobot("Ironhide", "Nissan C20 Vanette", "Peter Cullen"))
village.add(Decepticon("Breakdown", "Lamborghini Countach", "Alan Oppenheimer"))
village.add(Autobot("Optimus Prime", "Kenworth K100 Cabover", "Peter Cullen"))
village.add(Decepticon("Vortex", "Sikorsky UH-60 Black Hawk", "Johnny Haymer"))

print village

print "Autobots:"
for autobot in village.get_autobots():
    print "\t{0:<15} ({1}):\t{2: <16}\t{3}".format(autobot.name,
                                                   autobot.morality,
                                                   autobot.vehicle_mode,
                                                   autobot.voice_actor)

print

print "Decepticons:"
for decepticon in village.get_decepticons():
    print "\t{0:<15} ({1}):\t{2: <16}\t{3}".format(decepticon.name,
                                                   decepticon.morality,
                                                   decepticon.vehicle_mode,
                                                   decepticon.voice_actor)
