class Clock:
    def __init__(self, hh, mm, ss):
        self.hh = hh
        self.mm = mm
        self.ss = ss
    
    def run(self):
        self.ss += 1
        if self.ss == 60:
            self.ss = 0
            self.mm += 1
            if self.mm == 60:
                self.mm = 0
                self.hh += 1
                if self.hh == 24:
                    self.hh = 0
        print(f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}")

    def setTime(self, h, m, s):
        self.hh = int(h)
        self.mm = int(m)
        self.ss = int(s)

class AlarmClock(Clock):
    def __init__(self, hh, mm, ss):
        super().__init__(hh, mm, ss)
        self.alarm_hh = int(hh)
        self.alarm_mm = int(mm)
        self.alarm_ss = int(ss)
        self.alarm_on = False 

    def setAlarmTime(self, h, m, s):
        self.alarm_hh = int(h)
        self.alarm_mm = int(m)
        self.alarm_ss = int(s)

    def alarm_on(self): 
        self.alarm_on = True

    def alarm_off(self):  
        self.alarm_on = False

    def run(self):
        while True:
            self.ss += 1
            if self.ss == 60:
                self.ss = 0
                self.mm += 1
                if self.mm == 60:
                    self.mm = 0
                    self.hh += 1
                    if self.hh == 24:
                        self.hh = 0
            print(f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}")

            if (
                self.hh == self.alarm_hh
                and self.mm == self.alarm_mm
                and self.ss == self.alarm_ss
                and self.alarm_on
            ):
                print("ALARM")
                break 

def main():
    clock = Clock(0, 0, 0)
    alarm = AlarmClock(0, 0, 0)
    while True:
        print("1. Set time")
        print("2. Set alarm time")
        print("3. Turn on alarm")
        print("4. Turn off alarm")
        print("5. Run clock")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            h = input("Enter hour: ")
            m = input("Enter minute: ")
            s = input("Enter second: ")
            clock.setTime(h, m, s)
        elif choice == 2:
            h = input("Enter hour: ")
            m = input("Enter minute: ")
            s = input("Enter second: ")
            alarm.setAlarmTime(h, m, s)
        elif choice == 3:
            alarm.alarm_on()
        elif choice == 4:
            alarm.alarm_off()
        elif choice == 5:
            alarm.run()
        elif choice == 6:
            break

main()