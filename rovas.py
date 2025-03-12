from turtle import *
import math

speed(0)
SORKÖZ = 1.1
H = 100
XMARGÓ = 50
sor = 1
TÖBBSOROS = True


def A():
    pendown()
    fd(H)
    left(135)
    fd(H/2*1.41)
    left(135)
    fd(H/2)
    left(90)
    backward(H/2)
    penup()

def Á():
    pendown()
    fd(H)
    left(135)
    fd(H/3*1.41)
    left(90)
    fd(H/3*1.41)
    left(135)
    backward(H/3)
    penup()

def I():
    pendown()
    fd(H)
    penup()
    backward(H/6)
    left(112.5)
    fd(H/3)
    right(180)
    pendown()
    fd(H/3*2)
    penup()
    backward(H/3)
    right(112.5)
    right(180)
    backward(H/6*5)
    penup()

def Í():
    pendown()
    fd(H)
    penup()
    left(112.5)
    fd(H/3)
    right(180)
    pendown()
    fd(H/3*2)
    penup()
    backward(H/3)
    right(112.5)
    right(180)
    backward(H)
    penup()  

def M():
    pendown()
    fd(H)
    left(135)
    fd(H/4*1.41)
    left(90)
    fd(H/4*1.41)
    right(90)
    fd(H/4*1.41)
    left(90)
    fd(H/4*1.41)
    left(135)
    penup() 

def P():
    pendown()
    fd(H)
    for _ in range(3):
        left(112.5)
        fd(H/2)
        backward(H/2)
        right(112.5)
        backward(H/3)
    penup()

def R():
    pendown()
    fd(H)
    left(90)
    penup()
    fd(H/2.15)
    pendown()
    left(90)
    fd(H)
    left(90)
    penup()
    fd(H/2.15)
    pendown()
    left(90)
    fd(H)
    backward(H/3)
    left(112.5)
    fd(H/2)
    backward(H/2)
    right(112.5)
    backward(H/3*2)
    penup()
def T():
    pendown()
    fd(H)
    fd(-H/3)
    left(45)
    fd(H/2.15)
    fd(-H/2.15)
    right(45)
    fd(-H/3*2)
    penup()

def szöveg(szó):
    for betü in szó:
        if betü == "a":
            A()
        elif betü == "á":
            Á()
        elif betü == "i":
            I()
        elif betü == "í":
            Í()
        elif betü == "m":
            M()
        elif betü == "p":
            P()
        elif betü == "r":
            R()
        elif betü == "t":
            T()
        left(90)
        fd(H)
        right(90)
        if xcor() <= 0-screensize()[0] + XMARGÓ and TÖBBSOROS:
            global sor
            goto(screensize()[0],screensize()[1]-H*sor*SORKÖZ)
            sor += 1

def rovás(mondat):
    penup()
    if TÖBBSOROS:
        goto(screensize()[0],screensize()[1])
    for szó in mondat:
        szöveg(szó)
        penup()
        

def main():
    left(90)
    mondat = ["pár tapír papírt mart itt"]
    rovás(mondat)
    exitonclick()

if __name__ == "__main__":
    main()