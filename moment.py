class Mom:
    @staticmethod
    def mom(perpl, force, direct, units):
        m = perpl * force
        if direct == "cw":
            m = m * -1
        m = str("%.2f" % m)
        return m + " " + units
