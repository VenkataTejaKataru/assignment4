try:
    with open("data.txt", "w") as file:
        text = input("Enter text to write in file: ")
        file.write(text + "\n")

    with open("data.txt", "a") as file:
        more_text = input("Enter text to append: ")
        file.write(more_text + "\n")

    print("Data written successfully")

except Exception as e:
    print("Error:", e)