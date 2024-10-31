#defining the function which takes the parameters k,m,n 
def prob(k, m, n):
    i = m * m + 4 * n * n + 4 * m * n - 4 * n - m         #calculates the number of ways to randomly select two individuals from the population such that their offspring will not have a dominant allele
    j = 4 * (k + m + n) * (k + m + n - 1)                 #calculates the total number of ways to select any two individuals from the population.
    rst = 1 - float(i) / j                                #probability of selecting a pair that produces at least one dominant allele:
    return rst

k, m, n = map(int, input("k, m, n: ").split())
print(prob(k, m, n))