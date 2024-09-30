#write
#read
#append


file_path=r"file_handling\example.txt"
image_path=r"file_handling\document.png"

with open(file_path, "w") as file:
    file.write("Hello World \n")
    file.write("This file written successfully")
    print("printed in text file successfully")

with open(file_path, "r") as file:
    file.read()
    
with open(file_path, "a") as file:
    file.write("\nThis append file is executing successfully")

with open(image_path, "rb") as file:
    print(file.read())
