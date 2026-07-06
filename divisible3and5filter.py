# Write a lambda function using filter() which accept a list of numbers and returns a list of numbers divisible by both 3 and 5.
Division = lambda no1 : (no1 % 3 == 0) and (no1 % 5 == 0)

def main():

    Num = int(input("Enter how many elements : "))
    print("Elements are : ", Num)

    Result = []
    for i in range(Num):
        Element = int(input("Enter element : "))
        Result.append(Element)

    print("List is : ", Result)

    FData = list(filter(Division, Result))

    print("Number which are divisible by 3 and 5 are : ", FData)


if __name__ == "__main__":
    main()