
#Problem 01 ---------->


#Problem 02 -->

def game( ):
    return 446

score = game( )
with open("hiscore.txt") as f:
    hiscorestr = f.read( )

if hiscorestr:
    with open("hiscore.txt","w") as f:
        f.write(str(score)) 
elif int(hiscorestr) < score or hiscorestr:
    with open("hiscore.txt","w") as f:
        f.write(strscore)
    if hiscorestr:
        with open("hiscore.txt","w") as f:
            f.write(strscore)




#problem 03 ----->
for i in range(2,21):
    for j in range(1,11):
        with open(f"table/multiplication_table_of_{i}",'w') as f:
            f.write(f"{i}x{j}={i*j}\n")
            break
            


