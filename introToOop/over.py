# inheritance

class Bird:
    _mSpecies: str
    _mName: str
    _mWeight: float
    _mAge: int

    def __init__(self, species: str, name: str, weight: float, age: int):
        self._mSpecies = species
        self._mName = name
        self._mAge = age
        self._mWeight = weight

    #functions
    def Make_Sound(self) -> None:
        print("chirp")


    # accessor methods
    def Get_Species(self) -> str:
        return self._mSpecies

    def Set_Species(self, species: str) -> None:
        self._mSpecies = species

    def Get_Name(self) -> str:
        return self._mName

    def Set_Name(self, name: str) -> None:
        self._mName = name

    def Get_Age(self) -> int:
        return self._mAge

    def Set_Age(self, age: int) -> None:
        if (age < 0):
            self._mAge = 0
        else:
            self._mAge = age

    def Get_Weight(self) -> float:
        return self._mWeight

    def Set_Weight(self, weight: float) -> None:
        self._mWeight = weight

# classes
class Parrot(Bird):

    __mColour: str

    # constructors

    def __init__(self, species: str, name: str, weight: float, age: int, colour: str):
        Bird.__init__(self, species, name, weight, age)
        self.__mColour = colour

    #functions
    # override
    def Make_Sound(self) -> None:
        print("Talk")

    # def Make_Sound(self, lang: str) -> None: 
    #     if (lang == 'it'):
    #         print('Ciao')
    #     elif(lang == 'fr'):
    #         print('I surrender')
    #     else: 
    #         print('Talk')
    
    #this is how overloading would work if python supported it

    # accessor methods
    def Get_Colour(self) -> str:
        return self.__mColour

    def Set_Species(self, colour: str) -> None:
        self.__mColour = colour

class Robin(Bird):

    __mBeakLength: int

    # constructors

    def __init__(self, species: str, name: str, weight: float, age: int, beakLength: int):
        Bird.__init__(self, species, name, weight, age)
        self.__mBeakLength = beakLength


    # override
    def Make_Sound(self) -> None:
        print("sup bro")

    def Fly_About(self) -> None:
        print("weeeee")

    # accessor methods
    def Get_BeakLength(self) -> int:
        return self.__mBeakLength

    def Set_BeakLength(self, beakLength: int) -> None:
        self.__mBeakLength = beakLength

    
oParrot: Parrot = Parrot("macaw", "dudu", 1, 15, "blue")
oRobin: Robin = Robin("robin", "jojo", 0.5, 1, 15)
#polymorphism
oParrot.Make_Sound()
oRobin.Make_Sound()
print(oParrot.Get_Age())
oParrot.Set_Age(-3)
print(oParrot.Get_Age())

