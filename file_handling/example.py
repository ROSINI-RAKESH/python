file_path="file_handling/example.txt"

with open(file_path, "w") as file:
    file.write("Hello World \n")
    file.write("This file written successfully")
    print("printed in text file successfully")

with open(file_path, "r") as file:
    file.read()
    
with open(file_path, "a") as file:
    file.write("\nThis append file is executing successfully")
