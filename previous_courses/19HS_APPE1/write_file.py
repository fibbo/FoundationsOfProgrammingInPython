file = open("my_file.txt", "a")
file.write("First line of the write operation ")
file.write("This is a line with a new line character at the end\n")
file.write("This is another line, on a new line below the previous one.\n")
file.close()
