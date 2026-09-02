from math import sqrt
from random import randint

def clearspinners(func):
    def wrapper(spinners,spinner):
        spinners.clear()
        func(spinners,spinner)
    return wrapper


@clearspinners
def pl1(spinners,spinner):
    for i in range(1,1000):
        radius = i+1
        rot = i*137.5
        rot = rot % 360
        size = sqrt(i)*3.5
        speed = 0.2         #*sqrt(i) optikai illuziót keltő
        spinners.append(spinner(400, 400, 20, 20,   600, 400, size, size, (0, 55, 0, 255), rot, speed, radius, (1,0,0,1)))
        size *= 0.8
        spinners.append(spinner(400, 400, 20, 20,   600, 400, size, size, (0, 255, 0, 255), rot, speed, radius, (1,0,0,1)))

@clearspinners
def pl2(spinners,spinner):
    radius = 0
    omega = 0
    size = 2
    angle = 0
    for _ in range(360):
        angle += 135
        radius += 1.5
        omega += 0.01
        size *= 1.01
        spinners.append(spinner(400, 400, 20, 20,   600, 400, size, size, (0, size%255, omega%255, 255), angle, omega, radius, (1,0,0,1)))

@clearspinners
def pl3(spinners,spinner):
    spinners.append(spinner(200, 200, 20, 20,   600, 400, 8000, 8000, (0, 0, 0, 255), 0, 0, 0, (1,0,0,1))) #fekete háttér
    spinners.append(spinner(200, 200, 20, 20,   600, 400, 200, 200, (255, 255, 200, 255), 0, 0, 0, (0,1,0,1))) #nap
    spinners.append(spinner(200, 200, 20, 20,   600, 400, 4, 4, (150, 150, 190, 255), 0, 0.2, 200, (0,1,0,1))) #merkúr
    spinners.append(spinner(200, 200, 20, 20,   600, 400, 7, 7, (150, 150, 110, 255), 0, 0.13, 230, (0,1,0,1))) #vénusz
    spinners.append(spinner(200, 200, 20, 20,   600, 400, 8, 8, (10, 100, 255, 255), 0, 0.1, 290, (0,1,0,1))) #föld
    spinners.append(spinner(200, 200, 20, 20,   600, 400, 6, 6, (255, 100, 50, 255), 0, 0.07, 350, (0,1,0,1))) #mars

    for _ in range(300): #kisbolygóöv
        radius = randint(375, 550)
        angle = randint(0,360)
        omega = 2.5 / sqrt(radius) 
        size = randint(1,3)
        n = randint(100, 235)
        color = (n+randint(-20, 20), n+randint(-20, 20), n+randint(-20, 20), 255)
        spinners.append(spinner(200, 200, 20, 20,   600, 400, size, size, color, angle, omega, radius, (1,0,0,1)))

    spinners.append(spinner(200, 200, 20, 20,   600, 400, 60, 60, (200, 140, 60, 255), 0, 0.03, 600, (0,1,0,1))) #jupiter
    spinners.append(spinner(200, 200, 20, 20,   600, 400, 30, 30, (230, 190, 130, 255), 0, 0.02, 775, (0,1,0,1))) #szaturnusz
    spinners.append(spinner(200, 200, 20, 20,   600, 400, 20, 20, (100, 180, 230, 255), 0, 0.02, 1050, (0,1,0,1))) #uránusz
    spinners.append(spinner(200, 200, 20, 20,   600, 400, 19, 19, (40, 70, 140, 255), 0, 0.01, 1300, (0,1,0,1))) #neptunusz

    for _ in range(1500): #kuiper-öv
        radius = randint(1300, 2000)
        angle = randint(0,360)
        omega = 2.5 / sqrt(radius) * randint(1,5)/3
        size = randint(1,3)
        n = randint(100, 235)
        color = (n+randint(-20, 20), n+randint(-20, 20), n+randint(-20, 20), 255)
        spinners.append(spinner(200, 200, 20, 20,   600, 400, size, size, color, angle, omega, radius, (1,0,0,1)))

    for _ in range(500): #oort-felhő
        radius = randint(2000, 5000)
        angle = randint(0,360)
        omega = 2.5 / sqrt(radius)
        size = randint(1,3)
        n = randint(100, 235)
        color = (n+randint(-20, 20), n+randint(-20, 20), n+randint(-20, 20), 255)
        spinners.append(spinner(200, 200, 20, 20,   600, 400, size, size, color, angle, omega, radius, (1,0,0,1)))

    for _ in range(50): #üstökösök
        radius = randint(200, 2000)
        angle = randint(0,360)
        omega = 2.5 / sqrt(radius) * randint(2,4)/3
        size = randint(1,2)
        color = (randint(250, 255), randint(250, 255), randint(250, 255), 255)
        spinners.append(spinner(200, 200, 20, 20,   600, 400, size, size, color, angle, omega*2, radius, (1,0,0,1)))
