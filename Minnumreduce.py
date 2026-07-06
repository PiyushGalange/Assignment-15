# Write a lambda function using reduce() which accept a list of numbers and return the Minimum elements
from functools import reduce

Minimum = lambda no1, no2 : no1 if no1 < no2 else no2

def main():

    Num = int(input("How many elements : "))
    print(Num, "Elements")

    Result = []

    for i in range(Num):
        Element = int(input("Enter element : "))
        Result.append(Element)
        

    print("List is : ",Result)

    RData = reduce(Minimum, Result)

    print("Minimum number is : ", RData)


if __name__ == "__main__":
    main()