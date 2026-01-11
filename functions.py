# functions=collections of code that perform particular task
def print_hi(name,age):
    print("hello, "+name +". you are "+str(age))
print_hi("mike",18)    # write the parameter, not its name

#return_statement
def cube(num):
    return num*num*num    #cannot put more lines after this--the return statement breaks the function
result=cube(5)
print("the cube is "+str(result))
