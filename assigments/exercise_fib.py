#defining the function
def liverabbits(months,k):
    F1 = 1
    F2 = 1                          #F1 and F2 is the number of rabbit pairs in the first two months
    for i in range(months-2):       #for loop that runs from the third month onward
        F3 = F1*k+F2                #F3 is the number of rabbit pairs in the current month being calculated.
        F1 = F2
        F2 = F3
    return F3


if __name__ == "__main__":
    months = int(input("Number of months: "))
    k = int(input("New rabbits generated: "))
    
    total_rabbits = liverabbits(months, k)
    print(total_rabbits)



