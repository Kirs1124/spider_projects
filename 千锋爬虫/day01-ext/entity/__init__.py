class Student:
    def __init__(self, sno, sname, ssex, sbirthday, sdept, speciality):
        self.sno = sno
        self.sname = sname
        self.ssex = ssex
        self.sbirthday = sbirthday
        self.sdept = sdept
        self.speciality = speciality

    def __str__(self):
        return "%s %s %s %s %s %s" % (self.sno, self.sname, self.ssex, self.sbirthday, self.sdept, self.speciality)

    def __repr__(self):
        return self.__str__()