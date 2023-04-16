myDict = {
    "Fast" : "In a Quick Manner",
    "Harry" : "A coder",
    "Marks" : [1,2,5],
    "anotherdict" : {'harry':'player'},
    1:2
}

print(myDict.keys())
print(type(myDict.keys()))
print(myDict.values())
print (myDict.items())
print(myDict)

updateDict = {
    "Lovish" : "Friend"
}
myDict.update(updateDict)
print(myDict)
print(myDict.get("Lovish"))
print(myDict["Lovish"])

print(myDict.get("Lovish2"))
#print(myDict["Lovish2"])


# Sets---->
#a = {1,3,4,5,1}
#print(a)

#print(type(a))

#a = { }
#print(type(a))

b = set( )
print(type(b))

b.add(4)
b.add(5)
b.add(5)
print(b)

#b.add([4,5,6])
b.add((4,5,6))

# print the length of set---------
print(len(b))

b.remove(5)
print(b)

# pop----
print(b.pop())
print(b)


# problem -->1
#myDict = {
    #"Pankha" : "Fan",
    #"Dabba" : "Box",
    #"Vastu" : "Item"
#}

#print("Option are", myDict.keys( ))
#a = input("enter the Hindi word\n")
#print("The meaning of your word is:", myDict[a])

# To avoid error--->
#print("The meaning of your word is:", myDict.get(a))



#problem 2--->

#num1 = int(input("Enter number 1\n"))
# = int(input("Enter number 2\n"))
#num3 = int(input("Enter number 3\n"))
#num4 = int(input("Enter number 4\n"))
#num5 = int(input("Enter number 5\n"))
#num6 = int(input("Enter number 6\n"))
#num7 = int(input("Enter number 7\n"))
#num8 = int(input("Enter number 8\n"))

#s = {num1,num2,num3,num4,num5,num6,num7,num8}
#print(s)

#problem 3--->
#s = {18,"18",18.1}
#print(s)


#problrm 4 -------->
#s = {20,20.0,"20"}
#print(s)
#print(len(s))

#problem 5 --->
#s = { }
#print(type(s))

# problrm 6 --->
favLang = { }
a = input("Enter your favorite language Shubham\n")
b = input("Enter your favorite language Ankit\n")
c = input("Enter your favorite language Sonali\n")
d = input("Enter your favorite language Harshita\n")
favLang['Shubham'] = a
favLang['Ankit'] = b
favLang['Shubham'] = c
favLang['Harshita'] = d
print(favLang)
