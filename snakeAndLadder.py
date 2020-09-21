import turtle
t=turtle.Turtle()
t.speed(0)
t.penup()
t.setpos(-250,-250)
t.pd()
t.fd(500)
for i in range(3):
    t.left(90)
    t.fd(500)
for i in range(5):
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(500)
    t.right(90)
    t.fd(50)
    t.right(90)
    t.fd(500)
t.right(90)
t.fd(500)
for i in range(5):
    t.right(90)
    t.fd(50)
    t.right(90)
    t.fd(500)
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(500)
t.setpos(-250,-250)
for i in range(20):
        t.right(90)
        t.fd(25*(i+1))
        t.rt(90)
        t.penup()
        t.fd(20)
        z=i*5
        for j in range(10):
            t.pd()
            if((z+j+1)%2==0 and (z+j+1)%7==0 and z+j+1>11):
                t.dot(30,"red")
            if((z+j+1)%3==0 and (z+j+1)%8==0 and z+j+1>11):
                t.dot(30,"skyblue")
            if((z+j+1)%5==0 and (z+j+1)%7==0 and z+j+1>11):
                t.dot(30,"skyblue")
            t.write(j+z+1)
            t.pu()
            t.fd(50)      
        t.pu()
        t.goto(-250,-250)
for i in range(7):
    t.pu()
    t.goto(125+i,-130+i+i)
    t.pd()
    t.pencolor("red")
    t.goto(-75,-175)
t.pu()
t.goto(0,0)
for i in range(7):
    t.pu()
    t.goto(-75-i-i,172+i)
    t.pd()
    t.pencolor("red")
    t.goto(-175,-25)
t.pu()
t.goto(0,0)
for i in range(7):
    t.pu()
    t.goto(120+i+i,225+i)
    t.pd()
    t.pencolor("red")
    t.goto(25,25)
t.pu()
t.goto(0,0)
for i in range(7):
    t.pu()
    t.goto(-175+i,125+i)
    t.pd()
    t.pencolor("sky blue")
    t.goto(-75+i,-120+i)
for i in range(7):
    t.pu()
    t.goto(-195+i,125+i)
    t.pd()
    t.pencolor("sky blue")
    t.goto(-95+i,-120+i)
t.pu()
t.goto(0,0)
for i in range(5):
    t.pu()
    t.goto(-40+i,-70+i)
    t.pd()
    t.pencolor("sky blue")
    t.goto(120+i,-20+i)
for i in range(5):
    t.pu()
    t.goto(-20+i,-85+i)
    t.pd()
    t.pencolor("sky blue")
    t.goto(110+i,-40+i)
t.pu()
t.goto(0,0)
for i in range(4):
    t.pu()
    t.goto(10+i,220+i)
    t.pd()
    t.pencolor("sky blue")
    t.goto(210+i,70+i)
for i in range(4):
    t.pu()
    t.goto(33+i,225+i)
    t.pd()
    t.pencolor("sky blue")
    t.goto(220+i,80+i)
t.pu()
t.goto(-225,-225)
a=[]
aa=["green","orange","violet","blue"]
b=["1","2","3","4"]
n=int(input("enter no of players: "))
cc=[]
c=0
for i in range(n):
    a.append(turtle.Turtle("triangle",5000))
    a[i].color(aa[i])
    a[i].pu()
    a[i].goto(-275,-225)
    cc.append(0)
import random
z=random.randrange(1,6,1)
for i in range(n):
    print("press spacebar for playing ")
    print("color for player ",i," is ",aa[i])
co=[]
for i in range(10):
    w=-225+i*50
    for j in range(10):
        co1=[]
        q=-225+j*50
        co1.append(q)
        co1.append(w)
        co.append(co1)
co[27]=co[13]
co[97]=co[55]
co[83]=co[41]
co[23]=co[71]
co[34]=co[47]
co[69]=co[95]
f=0
while(max(cc)!=100):
    for i in range(n):
        ii=input()
        if(ii==' '):
            z=random.randrange(1,6,1)
            if(f==0):
                print("number on the die",z+1)
                cc[i]=cc[i]+z
                a[i].pu()
                a[i].goto(co[cc[i]][0]-1,co[cc[i]][1]-1)
            else:
                print("number on the die",z)
                cc[i]=cc[i]+z
                a[i].pu()
                a[i].goto(co[cc[i]][0]-1,co[cc[i]][1]-1)
        f=f+1      











        
