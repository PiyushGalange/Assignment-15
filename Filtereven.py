#Write a lambda function using filter() which accepts a list of numbers and returns a list of even number

Even = lambda No : No % 2 == 0

def main():

    Numbers = []

    Num = int(input("Enter how many elements you want in list : "))

    print("I want" ,Num, "Elements in the list")

    for i in range(Num):
        Element = int(input("Enter the Element : "))
        Numbers.append(Element)

    print("List of elements is :", Numbers)

    FData = list(filter(Even, Numbers))

    print("Even number is the list are : ", FData)



if __name__ == "__main__":
    main()