# Write a lambda function using filter() which accept a list of numbers and returns count of even numbers

CountEven = lambda no1 : no1 % 2 == 0

def main():

    Num = int(input("Enter how many elements : "))
    print("No of elements are : ", Num)

    Result = []

    for i in range(Num):

        Element = int(input("Enter element : "))
        Result.append(Element)

    print("Lis is : ", Result)

    FData = list(filter(CountEven, Result))
    print("Even num is : ", FData)
    
    print("Count of even number is : ", len(FData))




if __name__ == "__main__":
    main()