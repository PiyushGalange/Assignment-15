#Write a lambda function using filter() which accepts a list of numbers and returns a list of ODD number

Odd = lambda no : no % 2 != 0

def main():

    Number = []

    Num = int(input("Enter how many elements : "))

    print("i want", Num ,"Elements in my list")

    for i in range(Num):
        Element = int(input("Enter the element : "))
        Number.append(Element)

    print("List is ", Number)

    FData = list(filter(Odd, Number))

    print("Odd elements are : ",FData)



if __name__ == "__main__":
    main()