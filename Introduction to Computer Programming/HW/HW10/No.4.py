def print_table(table):
    max_lengths = [0] * len(table[0])

    for row in table:
        for i, item in enumerate(row):
            max_lengths[i] = max(max_lengths[i], len(str(item)))

    for row in table:
        for i, item in enumerate(row):
            print(str(item).ljust(max_lengths[i]), end=" ")
        print()

print_table([["X","Y"], [0,0], [10,10], [200,200]])

print_table( [
    ["ID","Name","Surname"], 
    ["001","Guido","van Rossum"], 
    ["002","Donald","Knuth"], 
    ["003","Gordon","Moore"] ] )