eceName = "Ece"
eceAge = 80
eceGender = "Female"
atlasName = "Atlas"
atlasAge = 10
atlasGender = "Male"
''' 
class Person():
    name= ""
    age= 0
    gender=""

    # method, initializer
    def __init__(self,name,age,gender):
        self.name= name
        self.age= age
        self.gender= gender

ece= Person("Ece",30,"Female")
print(type(ece))
print(ece)
print(ece.name)
'''


class Person():
    # property
    # name=""
    # age=0
    # gender=""
    job="Developer"

    # initializer method
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # method
    def printName(self):
        print(self.name)


ece = Person("Ece", 30, "Female")
print(type(ece))
print(ece)
print(ece.name)
print(ece.printName())
#why none?
print(ece.job)

