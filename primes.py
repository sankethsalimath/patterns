import math
import matplotlib.pyplot as plt
#from tkinter import *
hor = []
ver = []
primes=[1]
print("Enter highest number:")
n = int(input())



def prime(givenNumber):
    # Initialize a list
    for possiblePrime in range(2, givenNumber + 1):        # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)

prime(n)

for r in primes:
    X = r*math.cos(r)
    Y = r*math.sin(r)
    hor.append(X)
    ver.append(Y)


#print(primes)
# plotting the points
plt.scatter(hor, ver,s=0.5)
# function to show the plot
plt.show()
