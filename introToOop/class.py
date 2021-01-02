# classes
class Parrot:

    # default values
    # encapsulation
    #   mPublicVar
    #   _mProtectedVar
    #   __mPrivateVar

    __mSpecies: str
    __mColour: str
    __mAge: int

    # constructors

    def __init__(self, species: str, colour: str, age: int):
        self.__mSpecies = species
        self.__mColour = colour
        self.__mAge = age

    # accessor methods
    def Get_Species(self):
        return self.__mSpecies

    def Set_Species(self, species: str):
        self.__mSpecies = species


# objects
#   oObject

oParrot: Parrot = Parrot("macaw", "blue", 10)
oParrotTwo: Parrot = Parrot("parakeet", "red", 10)
#macaw
print(oParrot.Get_Species())
#parakeet
print(oParrotTwo.Get_Species())
#error
#print(oParrot.__mSpecies)

oParrot.Set_Species('parakeet')
#parakeet
print(oParrot.Get_Species())

