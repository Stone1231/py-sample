class Dog():
    """Represent a dog."""
    @classmethod
    def fromdict(cls, datadict):
        obj = cls("", 0, 0)
        obj.__dict__ = datadict
        return obj

    def __init__(self, name, heigh, weight):
        """Initialize dog object."""
        self.name = name
        self.heigh = heigh
        self.weight = weight
        self.persion = Persion('stone')

    def sit(self):
        """Simulate sitting."""
        print(self.persion.name + "'s " + self.name + " is sitting.")

    def eat(self):
        """Simulate sitting."""
        print(self.persion.name + "'s " + self.name + " is eating.")


class Persion():
    def __init__(self, name="happy"):
        self.name = name

class Master():
    def __init__(self, name):
        self.name = name
        self.dogs: {}