#methods vs functions
my_name="ece"
print(my_name.upper())
help(my_name.upper())
#functions
def hello_pyhton():
    print("hello")
    print("pyhton")
hello_pyhton()
#input
#args(arguments), kwargs(key word arguments)
def args_sum(*args):
    return(args)
print(args_sum(10,20,30,40,40,60))
def kwargs_example(**kwargs):
    print(kwargs)
    print("function is working")
print(kwargs_example(apple=100,banana=150,melon=200))
print(kwargs_example())
#PRACTİCAL_FUNCTİONS
def divideNumber(number):
    return number/2
myList=[3,5,7,10,20,30]
myResultList=[]
for num in myList:
    myResultList.append(divideNumber(num))
print(myResultList)
#map
help(map)
print(list(map(divideNumber,myList)))
def controlString(string):
    return "Ece" in string
print(controlString("Ece Ulker"))
print(controlString("Ulker"))
myStringList=["Atil","Ece","Ece Ulker","Atlas"]
print(list(map(controlString,myStringList)))
#filter
print(list(filter(controlString,myStringList)))
#print(list(filter("l",myStringList))) wrong code
#lambda
multiplyLambda=lambda num:num*3
print(type(multiplyLambda))
numList=[10,20,30,40,50]
print(list(map(lambda num:num/4,numList)))




