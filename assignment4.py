try:
    # open file using with statement
    with open("data.txt", "r") as file:
        print("Reading file line by line:\n")

        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("File not found")