def name_list() :
    namelist = [] 
    us = " "
    count = 1
    while us != "":
        us = input(f"Enter name {count}: ")
        if us != "" :
            namelist.append(us)
        count += 1
    print(namelist)

name_list()