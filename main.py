import math
import time

from centroid import Centr
from vectors import Vect
from beamdeflection import BeamDeflect
from moment import Mom
from random import random
from rps import RPS


class ClearScreen:
    @staticmethod
    def clr():
        for n in range(50):
            print('\n')


print("Welcome to the Beam Deflection Calculator.")
response = ""
answer = ""
done = False
while not done:
    correct = False
    while not correct:
        print("Beam Deflection: BD")
        print("Centroid: Cent")
        print("Moment: Mom")
        print("Vector: Vect")
        print("Game: Game")
        response = input("What are you trying to find: ")
        respl = str.lower(response)
        # Beam Deflection
        if respl == "bd":
            print("Moment of Inertia: MoI")
            print("Modulus of Elasticity: MoE")
            print("Max Beam Deflection: Max")
            response = input("What are you trying to find: ")
            respl = str.lower(response)
            if respl == "moi":
                base = float(input("What is the width of the beam(in.): "))
                height = float(input("What is the height of the beam(in.): "))
                answer = str(BeamDeflect.moi(base, height))
                correct = True
            elif respl == "moe":
                havemoi = str.lower(input("Do you already have the moment of inertia(Y,N): "))
                maxd = float(input("What is the max beam defection(in.): "))
                l = float(input("What is the length of the beam(in.): "))
                f = float(input("What is the force being applied on the beam(lbs.): "))
                if havemoi[0] == "y":
                    moi = float(input("What is the moment of inertia: "))
                    answer = str(BeamDeflect.moe(moi, maxd, l, f))
                else:
                    base = float(input("What is the length of the base(in.): "))
                    height = float(input("What is the length of the height(in.): "))
                    answer = str(BeamDeflect.moei(base, height, maxd, l, f))
                correct = True
            elif respl == "max":
                havemoi = str.lower(input("Do you already have the moment of inertia(Y,N): "))
                moe = float(input("What is the modulus of elasticity: "))
                l = float(input("What is the length of the beam(in.): "))
                f = float(input("What is the force being applied on the beam(lbs.): "))
                if havemoi[0] == "y":
                    moi = float(input("What is the moment of inertia: "))
                    answer = str(BeamDeflect.max(moi, moe, l, f))
                else:
                    base = float(input("What is the length of the base(in.): "))
                    height = float(input("What is the length of the height(in.): "))
                    answer = str(BeamDeflect.maxi(base, height, moe, l, f))
                correct = True
            else:
                print("I'm sorry that command does not seem to exist please try again.")
                correct = False
                time.sleep(1)
                ClearScreen.clr()
        # Centroid
        elif respl == "cent":
            print("Rectangle/Square: Rect")
            print("Right Triangle: Tri")
            print("SemiCircle: Semi")
            print("Multiple Shapes: MultiShape")
            response = input("What are you trying to find: ")
            respl = str.lower(response)
            if respl == "multishape":
                print("How Many of each shape are you calculating?")
                rectcount = int(input("How many Rectangle/Square: "))
                tricount = int(input("How many Right Triangle: "))
                semicount = int(input("How many SemiCircle: "))
                ansx = 0
                ansy = 0
                for n in range(rectcount):
                    xcord = float(input("What is the x coordinate of the bottom left corner of the Rectangle: "))
                    ycord = float(input("What is the y coordinate of the bottom left corner of the Rectangle: "))
                    width = float(input("What is the width of the Rectangle: "))
                    height = float(input("What is the height of the Rectangle: "))
                    ansx += Centr.rectintx(width, xcord)
                    ansy += Centr.rectinty(height, ycord)
                for n in range(tricount):
                    xcord = float(input("What is the x coordinate of the right angle corner of the Triangle: "))
                    ycord = float(input("What is the y coordinate of the right angle corner of the Triangle: "))
                    base = float(
                        input("What is the length of the base of the Triangle(If it is to the left of the right "
                              "angle corner enter a negative number): "))
                    height = float(
                        input("What is the height of the Triangle(If it is below the right angle corner enter "
                              "a negative number): "))
                    ansx += Centr.triintx(base, xcord)
                    ansy += Centr.triinty(height, ycord)
                for n in range(semicount):
                    xcord = float(input("What is the x coordinate of the center of the base of the Semicircle: "))
                    ycord = float(input("What is the y coordinate of the center of the base of the Semicircle: "))
                    rot = input("What way is the Semicircle oriented(base vertical:v, base horizontal:h): ")
                    if rot == "h":
                        rad = float(
                            input("What is the radius of Semicircle(If the the base is above the rest of the circle"
                                  "enter a negative radius): "))
                    else:
                        rad = float(
                            input("What is the radius of Semicircle(If the the base is left of the rest of the circle "
                                  "enter a negative radius): "))
                    ansx += Centr.semiintx(rad, xcord, rot)
                    ansy += Centr.semiinty(rad, ycord, rot)
                retx = str("%.2f" % ansx)
                rety = str("%.2f" % ansy)
                ansewer = "the point (" + retx + ", " + rety + ")"
                correct = True
            elif respl == "rect":
                xcord = float(input("What is the x coordinate of the bottom left corner of the Rectangle: "))
                ycord = float(input("What is the y coordinate of the bottom left corner of the Rectangle: "))
                width = float(input("What is the width of the Rectangle: "))
                height = float(input("What is the height of the Rectangle: "))
                answer = Centr.rect(width, height, xcord, ycord)
                correct = True
            elif respl == "tri":
                xcord = float(input("What is the x coordinate of the right angle corner of the Triangle: "))
                ycord = float(input("What is the y coordinate of the right angle corner of the Triangle: "))
                base = float(input("What is the length of the base of the Triangle(If it is to the left of the right "
                                   "angle corner enter a negative number): "))
                height = float(input("What is the height of the Triangle(If it is below the right angle corner enter "
                                     "a negative number): "))
                answer = Centr.tri(base, height, xcord, ycord)
                correct = True
            elif respl == "semi":
                xcord = float(input("What is the x coordinate of the center of the base of the Semicircle: "))
                ycord = float(input("What is the y coordinate of the center of the base of the Semicircle: "))
                rot = input("What way is the Semicircle oriented(base vertical:v, base horizontal:h): ")
                if rot == "h":
                    rad = float(input("What is the radius of Semicircle(If the the base is above the rest of the circle"
                                      "enter a negative radius): "))
                else:
                    rad = float(
                        input("What is the radius of Semicircle(If the the base is left of the rest of the circle "
                              "enter a negative radius): "))
                answer = Centr.semi(rad, xcord, ycord, rot)
                correct = True
            else:
                print("I'm sorry that command does not seem to exist please try again.")
                correct = False
                time.sleep(1)
                ClearScreen.clr()
        # Moment
        elif respl == "mom":
            print("NewtonMeters: NM")
            print("Foot-Pounds: FP")
            units = input("What are your units: ")
            force = float(input("What is force being applied to the object: "))
            perpdist = float(input("What is the perpendicular distance of the force to the pivot: "))
            direct = str.lower(input("In what direction is the force being applied(ClockWise: CW, Counter-ClockWise: "
                                     "CCW): "))
            answer = Mom.mom(perpdist, force, direct, units)
            correct = True
        elif respl == "vect":
            print("X and Y forces: XY")
            print("Resultant of two Vectors: Res")
            response = input("What are you trying to find: ")
            respl = str.lower(response)
            if respl == "xy":
                mag = float(input("What is Magnitude of the vector: "))
                theta = float(input("What is the angle of the Vector(deg): "))
                up = str.lower(input("Is the vector going up or down: "))
                right = str.lower(input("Is the vector going left or right: "))
                axis = str.lower(input("What axis is the angle of the vector connected to: "))
                answer = Vect.xnys(theta, mag, up, right, axis)
                correct = True
            elif respl == "res":
                mag = float(input("What is Magnitude of the first vector: "))
                theta = float(input("What is the angle of the first Vector(deg): "))
                up = str.lower(input("Is the vector going up or down: "))
                right = str.lower(input("Is the vector going left or right: "))
                axis = str.lower(input("What axis is the angle of the first vector connected to: "))
                vector1 = Vect.xnyi(theta, mag, up, right, axis)
                loc = vector1.find(" ")
                fx = float(vector1[:loc])
                fy = float(vector1[(loc + 1):])
                mag = float(input("What is Magnitude of the second vector: "))
                theta = float(input("What is the angle of the second Vector(deg): "))
                up = str.lower(input("Is the vector going up or down: "))
                right = str.lower(input("Is the vector going left or right: "))
                axis = str.lower(input("What axis is the angle of the second vector connected to: "))
                vector2 = Vect.xnyi(theta, mag, up, right, axis)
                loc = vector2.find(" ")
                fx += float(vector2[:loc])
                fy += float(vector2[(loc + 1):])
                rvector = str("%.2f" % math.sqrt(fy * fy + fx * fx))
                rangle = str("%.2f" % math.atan2(fy, fx))
                correct = True
                if fx >= 0:
                    answer = "The resultant vector has a magnitude of " + rvector + ("and the angle from the positive "
                                                                                     "x-axis is ") + rangle + "."
                else:
                    answer = "The resultant vector has a magnitude of " + rvector + ("and the angle from the negative "
                                                                                     "x-axis is ") + rangle + "."
            else:
                print("I'm sorry that command does not seem to exist please try again.")
                correct = False
                time.sleep(1)
                ClearScreen.clr()
        elif respl == "game":
            # rock:1
            # paper:2
            # scissors:3
            done = False
            count = 0
            wins = 0
            ties = 0
            while not done and count < 2:
                print("Let's play some rock paper scissors.")
                choice = str.lower(input("What do you choose (rock: r, paper: p, scissors: s): "))
                mychoice = int(random() * 3) + 1
                if(mychoice == 1):
                    print("I chose rock.")
                elif (mychoice == 2):
                    print("I chose paper.")
                elif (mychoice == 3):
                    print("I chose scissors.")
                if RPS.checkwin(choice, mychoice):
                    wins += 1
                    print("Congrats you won!")
                elif RPS.checktie(choice, mychoice):
                    ties += 1
                    print("Oh, we tied.")
                else:
                    print("Oh no, you lost.")
                count += 1
                previous = choice
                RPS.addto(choice)
                aredone = str.lower(input("Are you done (yes: y, no: n): "))
                if aredone == "y":
                    done = True
            while not done:
                print("Let's play some rock paper scissors.")
                choice = str.lower(input("What do you choose (rock: r, paper: p, scissors: s): "))
                mychoice = RPS.generatechoice()
                if RPS.checkwin(choice, mychoice):
                    wins += 1
                    print("Congrats you won!")
                elif RPS.checktie(choice, mychoice):
                    ties += 1
                    print("Oh, we tied.")
                else:
                    print("Oh no, you lost.")
                count += 1
                previous = choice
                RPS.addto(choice)
                aredone = str.lower(input("Are you done (yes: y, no: n): "))
                if aredone == "y":
                    done = True
            print("You chose rock " + str(RPS.r) + " times.")
            print("You chose paper " + str(RPS.p) + " times.")
            print("You chose scissors " + str(RPS.s) + " times.")
            print("You won " + str(wins) + " times out of the " + str(count) + " rounds.")
            print("We tied " + str(ties) + " times out of the " + str(count) + " rounds.")
            print("You lost " + str(count - ties - wins) + " times out of the " + str(count) + " rounds.")
            correct = True
        else:
            print("I'm sorry that command does not seem to exist please try again.")
            correct = False
            time.sleep(1)
            ClearScreen.clr()
    if not respl == "game":
        print("The " + response + " is " + answer)
    again = str.lower(input("Would you like to do anything else(Y,N): "))
    if again[0] == "y" or again == "sure":
        done = False
        ClearScreen.clr()
    else:
        done = True
ClearScreen.clr()
print("Thank you for using this calculator, please come again.")
