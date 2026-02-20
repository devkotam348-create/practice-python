###Overload greater than (>) operator in Time class which has instance obhect variables hour, min , sec.

class Time:
    def __init__(self, hour, min, sec):
        self.hour = hour
        self.min = min
        self.sec = sec

    def __gt__(self,others):
        if self.hour > others.hour:
            return True
        elif self.hour < others.hour:
            return False
        elif self.min > others.min:
            return True
        elif self.min < others.min:
            return False
        elif self.sec > others.sec:
            return True
        else:
            return False
    
e = Time(10,22,30)
d = Time(10,33,40)

print(e > d)
        