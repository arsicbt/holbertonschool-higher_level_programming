class SwimMixin:

    def swim(self):
        print("The creature swims!")


class FlyMixing:

    def fly(self):
        print("The creature flies!")
    

class Dragon(SwimMixin, FlyMixing):

    def roar(self):
        print("The dragon roars!")

    def sound(self):
        print("GREEEEEEEEEEEEEEEEEEEEEH!")
