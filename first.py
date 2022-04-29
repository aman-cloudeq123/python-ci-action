inpt="00011111110000000000011110001111"
Onemax=0
count=1
Zeromax= 0
for i in  range(len(inpt)-1):
    if inpt[i]==inpt[i+1]:
        count=count+1
        if  inpt[i+1]== "0":

            if(count>Zeromax):
                Zeromax=count
        else:
            if(count>Onemax):
                Onemax=count
    else:
        count=1

if(Zeromax<Onemax):
    for i in range(Onemax):
        print("1" , end="")

else:
  
    for i in range(Zeromax):
        print("0" , end="")        
