with open("my_text.txt", "r") as f:
    for line in f:
        line = line.strip()
        print(line)
