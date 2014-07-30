import csv

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
with open('cybertronians.csv', 'rb') as csvfile:
    roboreader = csv.reader(csvfile)
    for row in roboreader:
        team = row[0]
        name = row[1]
        vehicle_mode = row[2]
        voice_actor = row[3]
        if team == "Autobot":
            village.add(Autobot(name, vehicle_mode, voice_actor))
        if team == "Decepticon":
            village.add(Decepticon(name, vehicle_mode, voice_actor))
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
