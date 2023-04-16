



# Problem 02 -->
#num = int(input("Enter the number: "))
 #prime = True 
#for i in range (2,num):
    #if(num % i == 0):
        #prime = False
       # break
#if prime:
    #print("This number is prime")
#else:
   # print("This number is not prime")


#Problem 03-->
#n ! = 1 x 2 x 3 x ........ x n
#5 ! = 1 x 2 x 3 x 4 x 5

num = int(input("Enter the number: "))
for i in range (1,num+1):
    factorial = 1
    factorial = factorial*1
    #print(f"The factorial of this number is{factorial}")


# Problem 03 -->
n = 3
for i in range(3):
    print(" " * (n-i-1))
    print("*" * (n*i+1))
    print(" " * (n-i-1))
print(" " * (n-i-1),end = " ")
print("*" * (2*i+1),end = " ")
