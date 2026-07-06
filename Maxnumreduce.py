# Write a lambda function using reduce() which accept a list of numbers and return the maximum elements

from functools import reduce

Maximum = lambda no1, no2 : no1 if(no1 > no2) else no2

def main():

    Num = int(input("Enter how many elements you wants to enter : "))
    print("No of Elements are :", Num)

    Result = []

    for i in range(Num):
        Element = int(input("Enter element : "))
        Result.append(Element)

    print("Your list is  : ", Result)


    RData = reduce(Maximum, Result)
    print("Maximun number is : ", RData)


if __name__ == "__main__":
    main()