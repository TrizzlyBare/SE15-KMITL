#Write a recursive function to solve subset problem, the target sum is 0, if there is non in the set print("No solution"), if there is one print("Solution: ", subset)


def printAllSubsetsRec(arr, n, v, sum):
    if n == 0 and sum == 0:
        for value in v:
            print(value, end=" ")
        print()
        return
    if n == 0:
        return
    
    v1 = [] + v
    v1.append(arr[n - 1])
    printAllSubsetsRec(arr, n - 1, v1, sum - arr[n - 1])
    printAllSubsetsRec(arr, n - 1, v, sum)

def printAllSubsets(arr, n, sum):
    v = []
    printAllSubsetsRec(arr, n, v, sum)

arr = [-7, -3, -2, 5, 7]
sum = 0
n = len(arr)
printAllSubsets(arr, n, sum)
