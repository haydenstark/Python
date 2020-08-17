

class Birds:
    wings = 2
    legs = 2
    beak = True
    color = ' '
    flight = ' '
    def intro(self):
        print("There are many species of birds")
    def flight(self):
        print("Some can fly, others can't")

class Pigeon(Birds):
    color = 'Commonly grey and black'
    flight = 'Can fly'
    def intro(self):
        print("Pigeons are common and can be found attacking bread crumbs in major cities in America")
    def flight(self):
        print("Pigeons can fly")

class Penguin(Birds):
    color = 'Black and White, baby penguins are mainly grey"
    flight = 'Can not fly'
    def intro(self):
        print("Penguins are home to Antartica and colder climates")
    def flight(self):
        print("Penguins can not fly, but are very good swimmers")

if __name__ == "__main__":
    birds = Birds()
    pigeon = Pigeon()
    penguin = Penguin()

    birds.intro()
    birds.flight()

    pigeon.intro()
    pigeon.flight()

    penguin.intro()
    penguin.flight()
