from tkinter import *
from random import *
import time
import datetime
from PIL import Image, ImageTk
from tkinter import messagebox

class Net:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id1 = canvas.create_rectangle(0,0,10,500, fill=color)
        self.canvas.move(self.id1, 493, 100)
        self.id2 = canvas.create_rectangle(0,0,65,15, fill=color)
        self.canvas.move(self.id2, 430, 100)
        self.id3 = canvas.create_rectangle(0,0,65,15, fill=color)
        self.canvas.move(self.id3, 430, 437)
        self.canvas.create_text(442, 20, text='Soccer', fill='blue',font=('Old English Text MT',30))
        self.canvas.create_text(442, 55, text='Game', fill='blue',font=('Old English Text MT',30))
        
class Ball:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id = canvas.create_oval(0,0,30,30, fill=color)
        self.canvas.move(self.id, 310, 395)
        
class Keeper:
    def __init__(self,canvas,color,ball,man):
        self.canvas=canvas
        self.ball=ball
        self.man=man
        self.y=7
        self.shu=[7,11,15,19]
        self.id = canvas.create_rectangle(0,0,20,80, fill=color)
        self.canvas.move(self.id, 390, 220)
        self.y1=0
        self.canvas.bind_all("w", self.up)
        self.canvas.bind_all("s", self.down)

    def move(self):
        self.canvas.move(self.id, 0, self.y)
        fix=self.canvas.coords(self.id)
        fix1=self.canvas.coords(self.ball.id)
        if fix1[0]==fix[0]:
            if fix[1]<=fix1[3]<=fix[3]:
                self.man.shoot2()
            if fix[3]>=fix1[1]>=fix[1]:
                self.man.shoot2()
        if fix[1]<=100:
            shuffle(self.shu)
            self.y=self.shu[0]
            self.y=abs(self.y)
        if fix[3]>=437:
            shuffle(self.shu)
            self.y=self.shu[0]
            self.y=-abs(self.y)

    def move_double(self):
        self.canvas.move(self.id,0 , self.y1)
        fix=self.canvas.coords(self.id)
        fix1=self.canvas.coords(self.ball.id)
        if fix1[0]==fix[0]:     
            if fix[1]<=fix1[3]<=fix[3]:
                self.man.shoot2()
            if fix[3]>=fix1[1]>=fix[1]:                
                self.man.shoot2()
        if fix[1]<=140:
            self.y1=0
        if fix[3]>=430:
            self.y1=0

    def up(self,event):
        fix=self.canvas.coords(self.id)
        if fix[1]>140:
            self.y1=-15

    def down(self,event):
        fix=self.canvas.coords(self.id)
        if fix[3]<430:
            self.y1=15

class Man:
    def __init__(self,canvas,color,ball,win,defend,p1):
        self.win=win
        self.canvas=canvas
        self.ball=ball
        self.defend=defend
        self.id1 = canvas.create_oval(0,0,40,40, fill=color)
        self.id2 = canvas.create_rectangle(0,0,15,45, fill=color)
        self.id3 = canvas.create_polygon(10,10, 20,10, 25,70,15,70, fill=color)
        self.id4 = canvas.create_polygon(10,10, 20,10, 25,70,15,70, fill=color)
        self.id5 = canvas.create_rectangle(0,0,43,10, fill=color)
        self.pc1=self.canvas.create_image(20,15,image=p1)
        self.canvas.move(self.id1, 270, 280)
        self.canvas.move(self.id2, 283, 321)
        self.canvas.move(self.id3, 270, 357)
        self.canvas.move(self.id4, 286, 357)
        self.canvas.move(self.id5, 298, 333)
        self.canvas.move(self.pc1, 270, 264)
        self.x = 0
        self.y=0
        self.bx=10
        self.go=False
        self.goal=0
        self.total=0
        self.total_1=0
        self.goal_1=0
        self.c=1
        self.play=1
        self.record=[]

    def manMove(self):
        self.canvas.bind_all('<KeyPress-Right>', self.moveRight)    
        self.canvas.bind_all('<KeyPress-Left>', self.moveLeft)
        self.canvas.bind_all('<KeyPress-Up>', self.moveup)
        self.canvas.bind_all('<KeyPress-Down>', self.movedown)
        self.canvas.bind_all('<space>', self.shoot)

    def moveLeft(self, event):
        manPos = self.canvas.coords(self.id1)
        if manPos[0] <= 0:                   
            self.x = 0
        else:
            self.x = -10
        self.canvas.move(self.id1, self.x, 0)
        self.canvas.move(self.id2, self.x, 0)
        self.canvas.move(self.pc1, self.x, 0)
        if self.c%2:
            if self.c==1:
                self.canvas.delete(self.id3)
                self.id3 = canvas.create_polygon(10,10, 20,10, 25,55,15,55, fill='black')
                fix=self.canvas.coords(self.id2)
                self.canvas.move(self.id3,fix[0]-15 , fix[1]+33)
                self.canvas.move(self.id4, self.x, 0)
            else:
                self.canvas.delete(self.id3)
                self.canvas.delete(self.id4)
                self.id3= canvas.create_polygon(10,10, 20,10, 25,55,15,55, fill='black')
                fix=self.canvas.coords(self.id2)
                self.canvas.move(self.id3,fix[0]-15 , fix[1]+33)
                self.id4 = canvas.create_polygon(10,10, 20,10, 25,70,15,70, fill='black')
                self.canvas.move(self.id4,fix[2]-15 , fix[1]+33)
        else:
            self.canvas.delete(self.id3)
            self.canvas.delete(self.id4)
            self.id3 = canvas.create_polygon(10,10, 20,10, 25,70,15,70, fill='black')
            fix=self.canvas.coords(self.id2)
            self.canvas.move(self.id3,fix[0]-15 , fix[1]+33)
            self.id4 = canvas.create_polygon(10,10, 20,10, 25,55,15,55, fill='black')
            self.canvas.move(self.id4,fix[2]-15 , fix[1]+33)
        self.canvas.move(self.id5, self.x, 0)
        self.canvas.move(self.ball.id,self.x, 0)
        self.c+=1

    def moveRight(self, event):
        manPos = self.canvas.coords(self.ball.id)
        if manPos[2] >= 370:                   
            self.x = 0
        else:
            self.x = 10
        self.canvas.move(self.id1, self.x, 0)
        self.canvas.move(self.id2, self.x, 0)
        self.canvas.move(self.pc1, self.x, 0)
        if self.c%2:
            if self.c==1:
                self.canvas.delete(self.id3)
                self.id3 = canvas.create_polygon(10,10, 20,10, 25,55,15,55, fill='black')
                fix=self.canvas.coords(self.id2)
                self.canvas.move(self.id3,fix[0]-15 , fix[1]+33)
                self.canvas.move(self.id4, self.x, 0)
            else:
                self.canvas.delete(self.id3)
                self.canvas.delete(self.id4)
                self.id3= canvas.create_polygon(10,10, 20,10, 25,55,15,55, fill='black')
                fix=self.canvas.coords(self.id2)
                self.canvas.move(self.id3,fix[0]-15 , fix[1]+33)
                self.id4 = canvas.create_polygon(10,10, 20,10, 25,70,15,70, fill='black')
                self.canvas.move(self.id4,fix[2]-15 , fix[1]+33)
        else:
            self.canvas.delete(self.id3)
            self.canvas.delete(self.id4)
            self.id3 = canvas.create_polygon(10,10, 20,10, 25,70,15,70, fill='black')
            fix=self.canvas.coords(self.id2)
            self.canvas.move(self.id3,fix[0]-15 , fix[1]+33)
            self.id4 = canvas.create_polygon(10,10, 20,10, 25,55,15,55, fill='black')
            self.canvas.move(self.id4,fix[2]-15 , fix[1]+33)
        self.canvas.move(self.id5, self.x, 0)
        self.canvas.move(self.ball.id,self.x, 0)
        self.c+=1

    def moveup(self, event):
            manPos = self.canvas.coords(self.id1)
            if manPos[1] <= 10:                   
                self.y = 0
            else:
                self.y = -10
            self.canvas.move(self.id1, 0, self.y)
            self.canvas.move(self.id2, 0, self.y)
            self.canvas.move(self.pc1, 0, self.y)
            if self.c%2:
                if self.c==1:
                    self.canvas.delete(self.id3)
                    self.id3 = canvas.create_polygon(10,10, 20,10, 25,55,15,55, fill='black')
                    fix=self.canvas.coords(self.id2)
                    self.canvas.move(self.id3,fix[0]-15 , fix[1]+33)
                    self.canvas.move(self.id4, 0, self.y)
                else:
                    self.canvas.delete(self.id3)
                    self.canvas.delete(self.id4)
                    self.id3= canvas.create_polygon(10,10, 20,10, 25,55,15,55, fill='black')
                    fix=self.canvas.coords(self.id2)
                    self.canvas.move(self.id3,fix[0]-15 , fix[1]+33)
                    self.id4 = canvas.create_polygon(10,10, 20,10, 25,70,15,70, fill='black')
                    self.canvas.move(self.id4,fix[2]-15 , fix[1]+33)
            else:
                self.canvas.delete(self.id3)
                self.canvas.delete(self.id4)
                self.id3 = canvas.create_polygon(10,10, 20,10, 25,70,15,70, fill='black')
                fix=self.canvas.coords(self.id2)
                self.canvas.move(self.id3,fix[0]-15 , fix[1]+33)
                self.id4 = canvas.create_polygon(10,10, 20,10, 25,55,15,55, fill='black')
                self.canvas.move(self.id4,fix[2]-15 , fix[1]+33)
            self.canvas.move(self.id5, 0, self.y)
            self.canvas.move(self.ball.id,0, self.y)
            self.c+=1

    def movedown(self, event):
            manPos = self.canvas.coords(self.ball.id)
            if manPos[3]+10 >= 440:                   
                self.y = 0
            else:
                self.y = 10
            self.canvas.move(self.id1, 0, self.y)
            self.canvas.move(self.id2, 0, self.y)
            self.canvas.move(self.pc1, 0, self.y)
            if self.c%2:
                if self.c==1:
                    self.canvas.delete(self.id3)
                    self.id3 = canvas.create_polygon(10,10, 20,10, 25,55,15,55, fill='black')
                    fix=self.canvas.coords(self.id2)
                    self.canvas.move(self.id3,fix[0]-15 , fix[1]+33)
                    self.canvas.move(self.id4, 0, self.y)
                else:
                    self.canvas.delete(self.id3)
                    self.canvas.delete(self.id4)
                    self.id3= canvas.create_polygon(10,10, 20,10, 25,55,15,55, fill='black')
                    fix=self.canvas.coords(self.id2)
                    self.canvas.move(self.id3,fix[0]-15 , fix[1]+33)
                    self.id4 = canvas.create_polygon(10,10, 20,10, 25,70,15,70, fill='black')
                    self.canvas.move(self.id4,fix[2]-15 , fix[1]+33)
            else:
                self.canvas.delete(self.id3)
                self.canvas.delete(self.id4)
                self.id3 = canvas.create_polygon(10,10, 20,10, 25,70,15,70, fill='black')
                fix=self.canvas.coords(self.id2)
                self.canvas.move(self.id3,fix[0]-15 , fix[1]+33)
                self.id4 = canvas.create_polygon(10,10, 20,10, 25,55,15,55, fill='black')
                self.canvas.move(self.id4,fix[2]-15 , fix[1]+33)
            self.canvas.move(self.id5, 0, self.y)
            self.canvas.move(self.ball.id,0, self.y)
            self.c+=1

    def shoot(self,event):
        self.total+=1
        self.total_1+=1
        if self.defend.change:
            Label(win2,text='Total: '+str(self.total)).place(x=80,y=0)
        else:
            Label(win2,text='                          ').place(x=80,y=0)
            Label(win2,text='Total: 0').place(x=80,y=0)
        self.go=True
        fix=self.canvas.coords(self.id2)
        self.canvas.delete(self.id4)
        self.id4 = canvas.create_rectangle(0,0,55,10, fill='black')
        self.canvas.move(self.id4,fix[0]+16 , fix[1]+33)

    def shoot1(self,win):
        self.canvas.move(self.ball.id,self.bx , 0)
        fix=self.canvas.coords(self.ball.id)
        fix1=self.canvas.coords(self.id4)
        fix2=self.canvas.coords(self.id2)
        if fix[2]>=493:
            self.goal+=1
            if self.defend.change:
                self.goal_1=0
                self.total_1=0
                Label(win2,text='                            ').place(x=70,y=140)
                Label(win2,text='Attacker: 0').place(x=70,y=140)
                Label(win2,text='Goal: '+str(self.goal)).place(x=80,y=20)
                Label(win2,text='                           ').place(x=70,y=160)
                Label(win2,text='Defender: 0').place(x=70,y=160)
            else:
                self.total=0
                self.goal=0
                Label(win2,text='                            ').place(x=80,y=20)
                Label(win2,text='Goal: 0').place(x=80,y=20)
                self.goal_1+=1
                Label(win2,text='                       ').place(x=70,y=140)
                Label(win2,text='Attacker: '+str(self.goal_1)).place(x=70,y=140)
            self.bx=-10
            self.canvas.delete(self.id3)
            self.canvas.delete(self.id4)
            self.id3 = canvas.create_polygon(10,10, 20,10, 25,70,15,70, fill='black')
            self.id4 = canvas.create_polygon(10,10, 20,10, 25,70,15,70, fill='black')
            self.canvas.move(self.id3,fix2[0]-15 , fix2[1]+33)
            self.canvas.move(self.id4,fix2[2]-15 , fix2[1]+33)
        if fix[0]<=fix2[2]+12:
            self.bx=0
            self.go=False
            self.bx=10

    def shoot2(self):
        if self.defend.change==0:
            self.total=0
            self.goal=0
            Label(win2,text='                              ').place(x=70,y=160)
            Label(win2,text='Defender: '+str(self.total_1-self.goal_1)).place(x=70,y=160)
        self.canvas.move(self.ball.id,self.bx , 0)
        fix2=self.canvas.coords(self.id2)
        self.bx=-10
        self.canvas.delete(self.id3)
        self.canvas.delete(self.id4)
        self.id3 = canvas.create_polygon(10,10, 20,10, 25,70,15,70, fill='black')
        self.id4 = canvas.create_polygon(10,10, 20,10, 25,70,15,70, fill='black')
        self.canvas.move(self.id3,fix2[0]-15 , fix2[1]+33)
        self.canvas.move(self.id4,fix2[2]-15 , fix2[1]+33)

    def countdown(self,cd):
        Label(win2,text='                     ').place(x=80,y=40)
        Label(win2,text='Time: '+str(cd)).place(x=80,y=40)
        if cd> 0:
            win.after(1000, self.countdown, cd-1)       
        else:
            now=datetime.datetime.now()
            self.record.append(str(now.hour)+':'+str(now.minute)+':'+str(now.second)+" Total: "+str(self.total)+',Goal: '+str(self.goal))

    def restart(self):
        self.countdown(10)
        self.goal=0
        self.total=0
        Label(win2,text='Total: 0                        ').place(x=80,y=0)
        Label(win2,text='Goal: 0                         ').place(x=80,y=20)

    def Record(self):
        t=Toplevel()
        t.geometry("300x300")
        t.title('Your Record')
        for i in range(len(self.record)):
            Label(t,text=str(self.record[i])).place(x=0,y=15*i)
    def leave(self):
        yo=messagebox.askokcancel("Leave","Do you want to leave the game?")
        if yo:
            self.play=0
            win.destroy()
            win2.destroy()
    def warn(self):
        messagebox.showwarning("Warning","You can not close this window")
        
class Defend:
    def __init__(self,canvas):
        self.canvas=canvas
        self.change=1
        self.num=1

    def mode(self,event):
        if self.num%2:
            Label(win2,text='                        ').place(x=60,y=100)
            Label(win2,text='Two Player').place(x=60,y=100)
            self.change=0
        else:
            Label(win2,text='                        ').place(x=60,y=100)
            Label(win2,text='Single Player').place(x=60,y=100)
            self.change=1
        self.num+=1

winW = 500
winH = 450                                      
step = 20                                        
speed = 0.01

win= Tk()                     
win.wm_attributes('-topmost', 1)                 
canvas = Canvas(win, width=winW, height=winH)
canvas.create_rectangle(0,0,500,450 ,fill='lightgreen')
canvas.pack()
win.update()

img1 = Image.open("190712_0001.jpg")
p1= ImageTk.PhotoImage(img1)

win2=Tk()
win2.geometry('190x260')
Label(win2,text='Total: 0').place(x=80,y=0)
Label(win2,text='Goal: 0').place(x=80,y=20)
Label(win2,text='Attacker: 0').place(x=70,y=140)
Label(win2,text='Defender: 0').place(x=70,y=160)
Label(win2,text='****************************************').place(x=0,y=180)
Label(win2,text='Please type \"tab\" to ').place(x=45,y=200)
Label(win2,text='change the mode').place(x=45,y=220)

defend=Defend(canvas)
net=Net(canvas,'black')
ball=Ball(canvas,'orange')
man=Man(canvas,'black',ball,win2,defend,p1)
keeper=Keeper(canvas,'blue',ball,man)
Button(win2,text='Start',command=man.restart).place(x=0,y=40)
Button(win2,text='Record',command=man.Record).place(x=0,y=70)
Button(win2,text='Leave',command=man.leave).place(x=0,y=100)
Label(win2,text='Single Player').place(x=60,y=100)
canvas.bind_all("<Tab>", defend.mode)

win.protocol("WM_DELETE_WINDOW", man.warn)
win2.protocol("WM_DELETE_WINDOW", man.warn)

while man.play:
    if defend.change:
        man.manMove()
        keeper.move()
        if man.go:
            man.shoot1(win2)
        win.update()
        time.sleep(speed)
    else:
        man.manMove()
        keeper.move_double()
        if man.go:
            man.shoot1(win2)
        win.update()
        time.sleep(speed)        
        
