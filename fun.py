 
       


# problem 01-->





# problem ---> 02

def farh(Cel):
    return(Cel * (9/5)) + 32
C = 45
f = farh(C)

print("Fahrenheit Tempreture is" + str(f))


# problem --> 03

print("Hello")
print("How")
print("are")
print("you")

print("Hello", end = " ")
print("How", end = " ")
print("are", end = " ")
print("you", end = " ")


# problem --> 04

n = 6
for i in range (n):
    print("*" * (n-i))



# problem --> 05

def remove_and_split(string,word):
    newstr = string.replace(word," ")
    return newstr.strip( )
this :"  Harry is a good  "
n = remove_and_split(this,Harry)
print(n)


