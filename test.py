from random import randint as r
import time,math

g = 9.8

def contime(t): 
    res = g*(t**2)/2
    return res

def thee(n):
    num = (1+1/n)**n
    return num
if __name__ ==  "__main__":
    elect = input("Elect: ")
    if elect == "1":
        print(contime(float(input("HIGH: "))))
    else:
        print(thee(float(input("conte: "))))
