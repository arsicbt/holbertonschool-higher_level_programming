class Fish:

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The birds is flying")


class Bird:

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The birds lives in the sky")


class FlyingFish(Fish, Bird):

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
