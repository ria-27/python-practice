for letter in "Hello World!":     #for every letter in it, I want to do something
    print(letter)        #prints out a different letter in every iteration
#--> define a variable and that variable changes with each iteration of the loop

friends=["jim", "karen", "tim"]
for friend in friends:
    print(friend)
for index in range(len(friends)):
    print(friends[index])     # prints out friends[0],[1],[2]

for index in range(3,10):   #not including 10
    print(index)

for index in range(5):
    if index==0:
        print("first iteration")
    else:
        print("not first")