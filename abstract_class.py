


from abc import ABC, abstractmethod

class AbstractDemo(ABC):
    def hello(self, var):
        print("Hello", var)

    @abstractmethod
    def greeting(self, var):
        pass

class Howdy(AbstractDemo):
    def greeting(self, var):
        print("Howdy", var)

class hiThere(AbstractDemo):
    def greeting(self, var):
        print("Hi there", var)

world = "World!"
obj = Howdy()
objec = hiThere()

obj.hello(world)
obj.greeting(world)
objec.greeting(world)
