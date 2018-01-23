

# comments in python start with a hashtag/pound/octothorp

print("Hello World, My Name is Dr. Ramsey")

mylist = []    # this is an empty list
mylist = [3, 4]
mylist = [ [3,4], [4,5] ]
print(mylist)

mylist = [] # the list is empty again
mylist.append(3) # add the number 3 to the end of the list
print(mylist)
mylist.append(5)
print("This is my list after the append 5: ")
print(mylist)

if 5 in mylist:
    print("my list has a 5 in it")
    
print("this is not in the if statement")


if 7 in mylist:
    print("my list has a 7 in it")
else:
    print("7 was not in my list")

for myx in mylist: # x will get the value of the "current" element in list
    print(myx)


print(range(5))

for i in range(len(mylist)):
    print( mylist[i] )


# for next time!
# install anaconda and jupyter
# read in a list of numbers from the user (input)
# average them (is converting input into an integer int)
# --- average every pair in order
