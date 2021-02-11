#Author: ALJ (AMDG) 2/11/21

with open("my_file.txt", "w") as file1:
#^auto closes
    file1.write("ALJ, 2/11/21\n")
    file1.write("Hello world!\n")
    file1.write("I have been playing sports\n")

#file1 = open("my_file.txt", "w")
#file1.close()