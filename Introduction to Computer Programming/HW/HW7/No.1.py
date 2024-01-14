class Clock:
    def __init__(self, hour, minute, second):
        self.set_time(hour, minute, second)

    def set_time(self, hour, minute, second):
        if self.valid_hour(hour) and self.valid_minute(minute) and self.valid_second(second):
            self.hour = hour
            self.minute = minute
            self.second = second
        else:
            print("Invalid time values provided.")

    def valid_hour(self, hour):
        return 0 <= hour < 24

    def valid_minute(self, minute):
        return 0 <= minute < 60

    def valid_second(self, second):
        return 0 <= second < 60
    
    def get_time(self):
        if self.hour > 12:
            return f"{self.hour - 12:02}:{self.minute:02}:{self.second:02} PM."
        elif self.hour == 12:
            return f"{self.hour:02}:{self.minute:02}:{self.second:02} PM."
        elif self.hour == 0:
            return f"{self.hour + 12:02}:{self.minute:02}:{self.second:02} AM."
        else:
            return f"{self.hour:02}:{self.minute:02}:{self.second:02} AM."

    def tick(self):
        self.second += 1
        if self.second >= 60:
            self.minute += 1
            self.second -= 60
            if self.minute >= 60:
                self.hour += 1
                self.minute -= 60
            if self.hour >= 24:
                self.hour -= 24


my_clock = Clock(10, 30, 45)
print(my_clock.get_time()) 

my_clock.set_time(20, 15, 30)
print(my_clock.get_time()) 

my_clock.tick()
print(my_clock.get_time())  
