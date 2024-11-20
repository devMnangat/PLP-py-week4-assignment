
def errHandle():
    print("This program asks a user for a file name")

    try:
        in_file = open(input("Enter the name of the input file: "), "r")
    except FileNotFoundError:
        print("The input file does not exist.")

    for line in in_file:
        print(line)

    in_file.close()

errHandle()