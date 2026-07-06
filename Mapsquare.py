# Write a lambda function using Map() which accept a list of numbers and return a list of squares of each number

Square = lambda No : No * No

def main():

    Numbers = []

    Num = int(input("How many elements you want in the list : "))

    print("i want" ,Num, "elements in my list")

    for i in range(Num):
        Element = int(input("Enter the element : "))    
        Numbers.append(Element)

    print("Here is your list ", Numbers)


    MData = list(map(Square, Numbers))

    print("Square of the elements present in the list are : ", MData)


if __name__ == "__main__":
    main()