s=[["1","2","3"],["4","5","6"],["7","8","9"]]
def display(s):
    print()
    for i in range(3):
        print("                                 ",end="")
        print(s[i][0],s[i][1],s[i][2],sep=" | ")
        if(i!=2):
            print("                                ---------")
z=0
c=0
display(s)
vals=[]
while(1):
    if s[0][0]==s[0][1]==s[0][2] and s[0][0]!="-":                          #"1,2,3"
        print(s[0][0],"is winner")
        break
    elif s[0][0]==s[1][0]==s[2][0] and s[0][0]!="-":                        #"1,4,7"
        print(s[0][0],"is winner")
        break
    elif s[0][0]==s[1][1]==s[2][2] and s[0][0]!="-":                        #"diagonal"
        print(s[0][0],"is winner")
        break
    elif s[1][0]==s[1][2]==s[1][1] and s[1][0]!="-":                        #"4,5,6"
        print(s[1][0],"is winner")
        break
    elif s[2][0]==s[2][1]==s[2][2] and s[2][0]!="-":                        #"7,8,9"
        print(s[2][0],"is winner")
        break
    elif s[0][2]==s[1][1]==s[2][0] and s[2][0]!="-":                        #"diagonal"
        print(s[0][2],"is winner")
        break
    elif s[0][1]==s[1][1]==s[2][1] and s[1][1]!="-":                        #"2,5,8"
        print(s[0][1],"is winner")
        break
    elif s[0][2]==s[1][2]==s[2][2] and s[2][0]!="-":                        #"3,6,9"
        print(s[0][2],"is winner")
        break
    if(len(vals)==9):
        print("match drawn")                        # if no place is left ie list contains 1-9
        break
        
    while(1):                #check for entering unique values
        v=int(input("enter position:"))                   
        if(v in vals):
            print("RESERVED choose other")                  
        else:
            vals.append(v)
            break
    
    if(z%2==0):             #swapping players
        q="X"
    else:
        q="O"
    z=z+1
    if(v<4):                        #placing X,O in given positions
        s[0][v-1]=q
    elif(v<7):
        s[1][v-1-3]=q
    else:
        s[2][v-1-6]=q
    display(s)
