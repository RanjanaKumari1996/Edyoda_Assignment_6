class Dog:
    def __init__(self,name,age,coat_color):
        self.name=name
        self.age=age
        self.coat_color=coat_color
    
    def description(self):
        print("Name of the Dog is: ", self.name)
        print("Age of the Dog is: ", self.age)

    def get_info(self):
        return self.coat_color


class JackRussellTerrier(Dog):

    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def Jackproperties(self):

        print("The Jack Russell terrier is a happy, energetic dog with a strong desire to work")
    
    def Jacklength(self):

        print("Length of The Jack Russell terrier dog is: SHORT")



class Bulldog(Dog):
    
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def Bullproperties(self):

        print("The English bulldog has a sweet, gentle disposition. Dependable and predictable, the bulldog is a wonderful family pet and loving to most children. People-oriented as a breed, they actively solicit human attention")
    
    def Bulllength(self):
        
        print("Length of The Bull dog is: SHORT")
    

name=input("Enter Dog name: ")
age=int(input("Enter Dog age: "))
color=input("Enter colour of dog: ")

Dog_obj=Dog(name,age,color)
Dog_obj.description()

print(Dog_obj.get_info())



Jack_obj=JackRussellTerrier(name,age,color)
Jack_obj.Jackproperties()
Jack_obj.Jacklength()
Jack_obj.description()
print(Jack_obj.get_info())


Bulldog_obj=Bulldog(name,age,color)
Bulldog_obj.Bullproperties()
Bulldog_obj.Bulllength()
Bulldog_obj.description()
print(Bulldog_obj.get_info())
