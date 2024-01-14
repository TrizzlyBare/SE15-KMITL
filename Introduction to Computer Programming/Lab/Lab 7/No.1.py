class Time:
    def __init__(self, hour = 0, min = 0, sec = 0 ):
        self.hour = hour
        self.min = min
        self.sec = sec

    def print(self):
        print(f"{self.hour:02}:{self.minute:02}:{self.second:02} Hrs.")

time1 = Time(9, 30 , 0)
time1.print()