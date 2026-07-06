# write a lambda function using filter() which accept a list of string and return a list of string having length greater than 5

Max_length = lambda word1 : len(word1) > 5

def main():

    string = int(input("How many words do you want to enter in string : "))
    print("i want to enter", string, "words")

    Words = []

    for i in range(string):
        word = input("Enter word : ")
        Words.append(word)

    print("String is : ", Words)

    FData = list(filter(Max_length, Words))
    print("Max length word is : ", FData) 



if __name__ == "__main__":
    main()