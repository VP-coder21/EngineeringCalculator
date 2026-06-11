# Online Python - IDE, Editor, Compiler, Interpreter

class BeamDeflect:
    @staticmethod
    def moi(b, h):
        ret = (b * (h ** 3)) / 12
        return "%.2f" % ret

    @staticmethod
    def moiint(b, h):
        ret = (b * (h ** 3)) / 12
        return ret

    @staticmethod
    def moei(b, h, maxd, l, f):
        ret = (f * l ** 3) / (48 * maxd * BeamDeflect.moiint(b, h))
        return "%.2f" % ret

    @staticmethod
    def moe(moi, maxd, l, f):
        ret = (f * l ** 3) / (48 * maxd * moi)
        return "%.2f" % ret

    @staticmethod
    def max(moe, moi, l, f):
        ret = (f * l ** 3) / (48 * moe * moi)
        return "%.2f" % ret

    @staticmethod
    def maxi(b, h, moe, l, f):
        ret = (f * l ** 3) / (48 * moe * BeamDeflect.moiint(b, h))
        return "%.2f" % ret
