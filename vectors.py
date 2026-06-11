import math


class Vect:
    @staticmethod
    def xnys(angle, mag, up, right, axis):
        angle = math.radians(angle)
        if axis == "x":
            fy = (mag * math.sin(angle))
            fx = (mag * math.cos(angle))
        else:
            fx = (mag * math.sin(angle))
            fy = (mag * math.cos(angle))
        if up == "down":
            fy = fy * -1
        if right == "left":
            fx = fx * -1
        fxs = str("%.2f" % fx)
        fys = str("%.2f" % fy)
        return "x = " + fxs + ", y = " + fys + "."

    @staticmethod
    def xnyi(angle, mag, up, right,axis):
        angle = math.radians(angle)
        if axis == "x":
            fy = (mag * math.sin(angle))
            fx = (mag * math.cos(angle))
        else:
            fx = (mag * math.sin(angle))
            fy = (mag * math.cos(angle))
        if not up:
            fy = fy * -1
        if not right:
            fx = fx * -1
        return str(fx) + " " + str(fy)
