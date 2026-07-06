##Write a lambda function using reduce() which accepts a list of numbers and returns a addition of all elements
from functools import reduce

Addition = lambda no1, no2 : no1 + no2


def main():

    Number = []

    Num = int(input("How many elements do you want in the list : "))

    print("i want", Num ,"Element in my list")

    for i in range(Num):
        Element = int(input("Enter element for list : "))
        Number.append(Element)

    print("List is :", Number)

    RData = reduce(Addition, Number)

    print("Addition of number is : ", RData)



if __name__ == "__main__":
    main()