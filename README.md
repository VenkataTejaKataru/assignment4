Description:
This assignment demonstrates file handling in Python using with open() and error handling.
It contains two tasks.
Task 1:
The program reads a file line by line using with open() and a for loop. If the file does not exist, the program handles the error using try–except.
Task 2:
The program accepts user input, writes the input to a file, and then appends additional user input to the same file. Finally, the program reads and displays the file content.
Task 1: Read File Line by Line
Program
try:
    with open("data.txt", "r") as file:
        print("Reading file line by line:\n")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found")
Output:
Reading file line by line:

Hello Python
This is a file handling example
Learning Python is easy
welcome to python
Task 2: Write and Append Using User Input
Program
try:
    with open("data.txt", "w") as file:
        text = input("Enter text to write in file: ")
        file.write(text + "\n")
    with open("data.txt", "a") as file:
        more_text = input("Enter text to append: ")
        file.write(more_text + "\n")
    with open("data.txt", "r") as file:
        print("\nFile content is:\n")
        for line in file:
            print(line.strip())
except Exception as e:
    print("An error occurred:", e)
Output:
Enter text to write in file: Hello Python
Enter text to append: Welcome to Python
File content is:
Hello Python
Welcome to Python
