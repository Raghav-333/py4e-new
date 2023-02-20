'''class PartyAnimal:
    x = 0
    
    def func(self):
        self.x = self.x + 1
        print("So Far" , self.x)

an = PartyAnimal()

an.func()
an.func()
an.func()'''









'''class PartyAnimal:
    x = 0

    def __init__(self):
        print("I an constructed")
    
    def func(self):
        self.x = self.x + 1
        print("an contains" , self.x)
    
    def __del__(self):
        print("I an destructed")

an = PartyAnimal()

an.func()
an.func()
an = 42
print("an contains" , an)'''












'''class PartyAnimal:
    x = 0
    name = ""

    def __init__(self , z):
        self.name = z
        #print(self.name)
    
    def party(self):
        self.x = self.x + 1
        print(self.name , "count" , self.x)

s = PartyAnimal("sally")
s.party()
s.party()

j = PartyAnimal("jin")
j.party()'''










class PartyAnimal:
    x = 0
    name = ""

    def __init__(self , z):
        print("I am constructed")
        self.name = z

    def party(self):
        self.x = self.x + 1
        print(self.name , "count: " , self.x)

class FootballFan(PartyAnimal):
    point = 0
    def touchdown(self):
        self.party()
        self.point = self.point + 7
        print(self.name , "points: " , self.point)

an = FootballFan("sally")
an.touchdown()