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
myList

