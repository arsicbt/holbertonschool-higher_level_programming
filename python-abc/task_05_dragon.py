class SwimMixin:

    def swim(self):
        print("The creature swims!")

class FlyMixing:

    def fly(self):
        print("The creature flies!")
    

class Dragon(SwimMixin, FlyMixing):
    def sound(self):
        print("GREEEEEEEEEEEEEEEEEEEEEH!")
