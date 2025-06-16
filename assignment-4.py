# Task1

try:
    file = open('simple.txt', 'r')
    reading_file = file.read()
    print(reading_file)
    file.close()
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")





#Task2
with open("output.txt", "w") as file:
    user_input = input("Enter text to write to the file: ")
    file.write(user_input + "\n")
    print("Data successfully written to output.txt.")


with open("output.txt", "a") as file:
    additional_text = input("Enter additional text to append: ")
    file.write(additional_text + "\n")
    print("Data successfully appended.")


with open("output.txt", "r") as file:
    print("\nFinal content of output.txt:")
    for line in file:
        print(line, end="")



