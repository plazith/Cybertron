"""I am creating a Cybertronian village populated by cybertronians.csv"""
import csv

class Village(object):
    """I am defining a class to represent the village and assigning it atributes"""

    def __init__(self):
        self._decepticons = []
        self._autobots = []

    def __str__(self):
        return "A Cybertronian Village with {0} Autobot(s) and {1} Decepticon(s).\n".format(len(self._autobots), len(self._decepticons))

    def add(self, cybertronian):
        """This splits the Cybertronians into two groups based on alignment"""
        if cybertronian.get_team() == "Autobot":
            self._autobots.append(cybertronian)

        if cybertronian.get_team() == "Decepticon":
            self._decepticons.append(cybertronian)

    def get_decepticons(self):
        """This returns the Decepticon group"""
        return self._decepticons

    def get_autobots(self):
        """This returns the Autobot group"""
        return self._autobots

class Transformer(object):
    """This class represents individual Cybertronians and their unique characteristics"""
    def __init__(self, name, alternate_mode, voice_actor):
        self.alternate_mode = alternate_mode
        self.name = name
        self.voice_actor = voice_actor

    def results(self):
        """This will print all the information about the Cybertronians"""
        print self.name
        print self.get_team()
        print "{0}\n{1}\n{2}".format(self.alternate_mode, self.morality, self.voice_actor)

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
    """This is a class representing the entire group of Decepticons and their shared characteristics"""
    morality = "evil"


class Autobot(Transformer):
    """This is a class representing the entire group of Autobots and their shared characteristics"""
    morality = "good"

village = Village()
with open('cybertronians.csv', 'rb') as csvfile:
    roboreader = csv.reader(csvfile)
    for row in roboreader:
        team = row[0]
        name = row[1]
        alternate_mode = row[2]
        voice_actor = row[3]
        if team == "Autobot":
            village.add(Autobot(name, alternate_mode, voice_actor))
        if team == "Decepticon":
            village.add(Decepticon(name, alternate_mode, voice_actor))
print village

print "Autobots:"
for autobot in village.get_autobots():
    print "\t{0:<15} ({1}):\t{2: <16}\t{3}".format(autobot.name,
                                                   autobot.morality,
                                                   autobot.alternate_mode,
                                                   autobot.voice_actor)

print

print "Decepticons:"
for decepticon in village.get_decepticons():
    print "\t{0:<15} ({1}):\t{2: <16}\t{3}".format(decepticon.name,
                                                   decepticon.morality,
                                                   decepticon.alternate_mode,
                                                   decepticon.voice_actor)

class Combiners(object):

    def __init__(self, name, team, voice_actor, group_name, members):
        self.name = name
        self.team = team
        self.voice_actor = voice_actor
        self.group_name = group_name
        self._members = members

    def add_members(self, member):
        self._members.append(member)

def demo1():
    devastator = Combiners("Devastator", "Decepticon", "Arthur Burghardt", "Constructicons", ["Scrapper", "Hook", "Bonecrusher", "Long Haul", "Mixmaster", "Scavenger"])
    print devastator.name
    print devastator.team
    print devastator.voice_actor
    print devastator.group_name
    print devastator._members

demo1()
