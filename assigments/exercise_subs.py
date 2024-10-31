#defining the functon
def locations(s, t):
    lenght_t = len(t)
    location = ""  
    for i in range(len(s) - lenght_t + 1):      #for loop that iterates through the string s from the start to len(s) - lenght_t + 1.
        if s[i:i + lenght_t] == t:       
            location += str(i + 1) + " "        #If a match is found, the position i + 1 is appended, followe by a space
    return location


s = "GATATATGCATATACTT"
t = "ATAT"
print(locations(s, t)) 
