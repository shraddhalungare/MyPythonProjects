t = (1,2,4,5)
print(t[0])
#t[0] = 34

t1 = ( )
print(t1)
t1 = (1, )
print(t1)


# Tuples methods-----
#t = (1,2,4,5)
print(t.count(1))

t = (1,2,4,5,4,1,2,1,1)
print(t.count(1))
print(t.index(1))
print(t.index(5))



#problem2---
m1 = int(input("Enter mark for student number 1:"))
m2 = int(input("Enter mark for student number 2:"))
m3 = int(input("Enter mark for student number 3:"))
m4 = int(input("Enter mark for student number 4:"))
m5 = int(input("Enter mark for student number 5:"))
m6 = int(input("Enter mark for student number 6:"))

mylist = [m1,m2,m3,m4,m5,m6]
mylist.sort()
print(mylist)


# problem 3----
a = [2,4,56,7]
print(a[0]+a[1]+a[2]+a[3])
print(sum(a))


