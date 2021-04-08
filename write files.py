from random import randint
from csv import reader
N = int(input("Enter Number Of Coutries: "))
List = []
for I in range(N):
    X = input(str(I + 1) + ".")
    R = randint(100, 1000)
    List.append(str(I + 1) + ". " + X + " " + str(R))
A = open('data.txt','w')
for Val in List:
    A.write(Val + "\n")
A.close()
B = open('data.txt','r')
print(B.read())