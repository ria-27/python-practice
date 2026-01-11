#list-name=[values of list]
friends=["kevin","karen","jim","jim","oscar","toby","sandra"]    #values can be strings, numbers or boolean
lucky_number=[2,45,63,12,4,89,65,73]
print(friends[-2])  #print specific values by their index
print(friends[1:])  # use: to print the value and every value after that value
print(friends[1:4]) #prints everything upto but not including 4th index---specifies range this way
friends[1]="mike"   #change value at that index
print(friends[1])

#list functions:-
#friends.extend(lucky_number)    #appends/join the lists
print(friends)
friends.append("john")          #adds new element to list---by default adds to the end of list
print(friends)
friends.insert(1,"tom")    #add new element to specific index
print(friends)
friends.remove("tom")
print(friends)
#friends.clear()     #to remove all elements from list
friends.pop()       #removes last element from list
print(friends)
print(friends.index("jim")) # to search location of specific element
print(friends.count("jim")) # to count similar elements in list
friends.sort()   #sorts in ascending order---alphabetical here
print(friends)
lucky_number.sort()
print(lucky_number)
lucky_number.reverse()  #reverses list
print(lucky_number)
friends2=friends.copy()   #copies list to another list
print(friends2)


