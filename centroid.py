import math


class Centr:
    @staticmethod
    def rect(w, h, x, y):
        cenx = (w / 2) + x
        ceny = (h / 2) + y
        retx = str("%.2f" % cenx)
        rety = str("%.2f" % ceny)
        return "the point (" + retx + ", " + rety + ")"

    @staticmethod
    def rectintx(w, x):
        cenx = (w / 2) + x
        return cenx

    @staticmethod
    def rectinty(h, y):
        ceny = (h / 2) + y
        return ceny

    @staticmethod
    def tri(b, h, x, y):
        cenx = (b / 3) + x
        ceny = (h / 3) + y
        retx = str("%.2f" % cenx)
        rety = str("%.2f" % ceny)
        return "the point (" + retx + ", " + rety + ")"

    @staticmethod
    def triintx(b, x):
        cenx = (b / 3) + x
        return cenx

    @staticmethod
    def triinty(h, y):
        ceny = (h / 3) + y
        return ceny

    @staticmethod
    def semi(r, x, y, rot):
        if (rot == "h"):
            cenx = x
            ceny = (4 * r / 3 * math.pi) + y
        else:
            cenx = (4 * r / 3 * math.pi) + x
            ceny = y
        retx = str("%.2f" % cenx)
        rety = str("%.2f" % ceny)
        return "the point (" + retx + ", " + rety + ")"

    @staticmethod
    def semiintx(r, x, rot):
        if (rot == "h"):
            cenx = x
        else:
            cenx = (4 * r / 3 * math.pi) + x
        return cenx

    @staticmethod
    def semiinty(r, y, rot):
        if (rot == "h"):
            ceny = (4 * r / 3 * math.pi) + y
        else:
            ceny = y
        return ceny
