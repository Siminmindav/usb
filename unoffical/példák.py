from math import sqrt, sin, cos
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
        speed = 0.2         
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

@clearspinners
def pl4(spinners,spinner):
    spinners.append(spinner(200, 100, 20, 20,   200, 100, 100, 100, (0,0,0,255), 0, 1, 10, (1,0,0,1)))
    spinners.append(spinner(400, 100, 20, 20,   400, 100, 100, 100, (0,0,0,255), 0, 1, 10, (1,0,0,1)))
    spinners.append(spinner(100, 300, 20, 20,   100, 300, 100, 100, (0,0,0,255), 0, 1, 10, (1,0,0,1)))
    spinners.append(spinner(500, 300, 20, 20,   500, 300, 100, 100, (0,0,0,255), 0, 1, 10, (1,0,0,1)))
    spinners.append(spinner(200, 400, 20, 20,   200, 400, 100, 100, (0,0,0,255), 0, 1, 10, (1,0,0,1)))
    spinners.append(spinner(300, 400, 20, 20,   300, 400, 100, 100, (0,0,0,255), 0, 1, 10, (1,0,0,1)))
    spinners.append(spinner(400, 400, 20, 20,   400, 400, 100, 100, (0,0,0,255), 0, 1, 10, (1,0,0,1)))

#AI made
@clearspinners
def pl5(spinners, spinner):
    # Wave Interference / Moire pattern
    for x in range(0, 8000, 40):
        for y in range(0, 8000, 40):
            # Calculate distance from two focal points
            dist1 = sqrt((x - 200)**2 + (y - 300)**2)
            dist2 = sqrt((x - 600)**2 + (y - 300)**2)
            
            # Interference math
            wave = (dist1 + dist2) * 0.05
            
            # Color based on the wave phase
            r = int(127 + 127 * sin(wave))
            g = int(127 + 127 * cos(wave))
            b = 150
            color = (r, g, b, 255)
            
            spinners.append(spinner(x, y, 40, 40, x, y, 40, 40, color, 0, 0.02, 0, (1,0,0,1)))

#AI made
@clearspinners
def pl6(spinners, spinner):

    # Accretion disk
    for i in range(10000):

        radius = randint(80, 7000)
        angle = randint(0, 360)

        # Faster near center
        omega = 300 / max(radius, 20)

        size = randint(1, 3)

        brightness = randint(120, 255)

        color = (
            brightness,
            int(brightness * 0.7),
            int(brightness * 0.3),
            255
        )

        spinners.append(
            spinner(
                400, 400,
                20, 20,
                600, 400,
                size, size,
                color,
                angle,
                omega,
                radius,
                (1,0,0,1)
            )
        )


#AI made
@clearspinners
def pl7(spinners, spinner):
    for i in range(2000):
        radius = sqrt(i) * 8

        # Several spiral arms
        arm = i % 5
        angle = radius * 0.8 + arm * 72

        # Slight randomness
        angle += randint(-15, 15)

        omega = 1.5 / sqrt(max(radius, 1))
        size = randint(1, 4)

        brightness = randint(150, 255)

        color = (
            brightness,
            brightness,
            randint(180, 255),
            255
        )

        spinners.append(
            spinner(
                400, 400,
                20, 20,
                600, 400,
                size, size,
                color,
                angle,
                omega,
                radius,
                (1,0,0,1)
            )
        )

@clearspinners    
def pl8(spinners, spinner):
    max = 2000
    for x in range(0, max, 10):
        for y in range(0, max, 10):
            i = 255*255*255/(max*max)*(x*max+y)
            color = (i%(255*255*255)//(255*255), i%(255*255)//255, i%255,255)
            spinners.append(spinner(x,y,20, 20,x, y,40, 40,color,0,0,0,(1,0,0,1)))

@clearspinners    
def pl9(spinners, spinner):
    max = 2000
    for x in range(0, max, 20):
        for y in range(0, max, 20):
            color = (int((x//20*x//20 + y//20*y//20) % 13 * 255/12),0,0,255)
            spinners.append(spinner(x,y,10, 10,x, y,20, 20,color,0,0,0,(1,0,0,1)))

@clearspinners    
def pl10(spinners, spinner):
    max = 2000
    for x in range(0, max, 20):
        for y in range(0, max, 20):
            if int(sin(x/100)*100) + 150 >= y % 300 and int(sin(x/100)*100) + 100 <= y % 300:
                color = (255,int(y % 300/300*255),0,255)
            else:
                color = (0, 0, int(50 - abs(((y-150) % 300 / 300)-0.5) * 50), 255) #AAAAAAAAAAAAAAAAAAA im braindead 
            spinners.append(spinner(x,y,10, 10,x, y,20, 20,color,0,0,0,(1,0,0,1)))

@clearspinners    
def pl1(spinners, spinner):
    max = 2000
    for x in range(0, max, 20):
        for y in range(0, max, 20):
            spinners.append(spinner(x,y,10, 10,x, y,20, 20,(0,0,0,1),0,0,100,(1,0,0,1), clockmax = 256,
            functions=[
                lambda s: setattr(s, 'color', spinner.color(((s.clock+20) % 255), ((s.clock+40) % 255), ((s.clock + s.clock) % 255), 255)),
                lambda s: setattr(s, 'omega', (s.x+s.y)/1000)
                ]
            ))

