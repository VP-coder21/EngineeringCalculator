from random import random

class RPS:
    # rock:1
    # paper:2
    # scissors:3
    rs = 0
    rr = 0
    rp = 0
    sr = 0
    ss = 0
    sp = 0
    ps = 0
    pp = 0
    pr = 0
    r = 0
    p = 0
    s = 0
    previous = "none"

    @staticmethod
    def checkwin(c, mc):
        win = False
        if c == "r" and mc == 3:
            win = True
        elif c == "p" and mc == 1:
            win = True
        elif c == "s" and mc == 2:
            win = True
        return win

    @staticmethod
    def checktie(c, mc):
        tie = False
        if c == "r" and mc == 1:
            tie = True
        elif c == "p" and mc == 2:
            tie = True
        elif c == "s" and mc == 3:
            tie = True
        return tie

    @staticmethod
    def generatechoice():
        if(not RPS.previous == "none"):
            if(RPS.previous == "p"):
                if(RPS.ps > RPS.pp and RPS.ps > RPS.pr):
                    return 1
                elif(RPS.ps == RPS.pp and RPS.pp == RPS.pr):
                    return int(random() * 3) + 1
                elif(RPS.pp > RPS.ps and RPS.pp >RPS.pr):
                    return 3
                elif (RPS.pr > RPS.ps and RPS.pr > RPS.pp):
                    return 2
                elif (RPS.pr == RPS.ps):
                    return int(random() * 2) + 1
                elif (RPS.pr == RPS.pp):
                    return int(random() * 2) + 2
                elif (RPS.pp == RPS.ps):
                    rand = int(random() * 2)
                    if(rand == 0):
                        return 1
                    else:
                        return 3
            elif (RPS.previous == "r"):
                if (RPS.rs > RPS.rp and RPS.rs > RPS.rr):
                    return 1
                elif (RPS.rs == RPS.rp and RPS.rp == RPS.rr):
                    return int(random() * 3) + 1
                elif (RPS.rp > RPS.rs and RPS.rp > RPS.rr):
                    return 3
                elif (RPS.rr > RPS.rs and RPS.rr > RPS.rp):
                    return 2
                elif (RPS.rr == RPS.rs):
                    return int(random() * 2) + 1
                elif (RPS.rr == RPS.rp):
                    return int(random() * 2) + 2
                elif (RPS.rp == RPS.rs):
                    rand = int(random() * 2)
                    if (rand == 0):
                        return 1
                    else:
                        return 3
            elif (RPS.previous == "s"):
                if (RPS.ss > RPS.sp and RPS.ss > RPS.sr):
                    return 1
                elif (RPS.ss == RPS.sp and RPS.sp == RPS.sr):
                    return int(random() * 3) + 1
                elif (RPS.sp > RPS.ss and RPS.sp > RPS.sr):
                    return 3
                elif (RPS.sr > RPS.ss and RPS.sr > RPS.sp):
                    return 2
                elif (RPS.sr == RPS.ss):
                    return int(random() * 2) + 1
                elif (RPS.sr == RPS.sp):
                    return int(random() * 2) + 2
                elif (RPS.sp == RPS.ss):
                    rand = int(random() * 2)
                    if (rand == 0):
                        return 1
                    else:
                        return 3

    @staticmethod
    def addto(c):
        if c == "r":
            RPS.r+=1
        elif c == "s":
            RPS.s+=1
        elif c == "p":
            RPS.p += 1
        if not RPS.previous == "none":
            if(c == "p"):
                if(RPS.previous == "p"):
                    RPS.pp+=1
                elif RPS.previous == "s":
                    RPS.ps+=1
                else:
                    RPS.pr+=1
            elif (c == "r"):
                if (RPS.previous == "p"):
                    RPS.rp += 1
                elif RPS.previous == "s":
                    RPS.rs += 1
                else:
                    RPS.rr += 1
            else:
                if (RPS.previous == "p"):
                    RPS.sp += 1
                elif RPS.previous == "s":
                    RPS.ss += 1
                else:
                    RPS.sr += 1
        RPS.previous = c