# Write a lambda function using reduce() which accept a list of numbers and returns a product of all elements
from functools import reduce

Product = lambda no1, no2 : no1 * no2


def main():

    Num = int(input("Enter how many elements : "))
    print("No of elements are : ", Num)

    Result = []

    for i in range(Num):
        Element = int(input("Enter element : "))
        Result.append(Element)

    print("list of number is : ", Result)

    RData = reduce(Product, Result)

    print("Product of all element is : ", RData)



if __name__ == "__main__":
    main()