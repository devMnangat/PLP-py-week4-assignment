
# File Read and Write Challenge

def main():
    print("This program reads a text file and writes it to a new text file.")

    in_file = input("Enter the name of the input file: ")
    out_file = input("Enter the name of the output file: ")

    in_file = open(in_file, "r")
    out_file = open(out_file, "w")

    for line in in_file:
        out_file.write(line)

    in_file.close()
    out_file.close()

    print("Done.")

main()


