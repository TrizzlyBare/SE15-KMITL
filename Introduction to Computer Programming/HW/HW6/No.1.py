t = input("Please enter the time in 24-hour format (hh:mm): ")

def time_change(time):
    hr, min = time.split(':')
    if int(hr) < 24 and int(hr) >= 0:
        if int(min) < 60 and int(min) >= 0:
            if int(hr) > 12:
                return str(int(hr) - 12) + ':' + min + ' PM'
            elif int(hr) == 0:
                return str(int(hr) + 12) + ':' + min + ' AM'
            elif int(hr) == 12:
                return str(int(hr)) + ':' + min + ' PM'
            else:
                return str(int(hr)) + ':' + min + ' AM'
        else:
            return 'Invalid input of minutes'
    else: 
        return 'Invalid input of hours'
    
print(time_change(t))