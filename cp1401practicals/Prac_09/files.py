"""Files"""


# 4. Read a String from a File
def question_4():
    in_file = open("name.txt", "r")
    text = in_file.read().strip()
    print(f"Greetings {text}!")
    in_file.close()


# 5. Greater-Than Counter
def question_5():
    filename = input("Filename: ")
    in_file = open("recentrain.txt", "r")
    threshold = 13.9
    count = 0
    total = 0
    for line in in_file:
        number = float(line)
        if number > threshold:
            count += 1
        total += 1
    percentage = (count/total) * 100
    print(f"Threshold: {threshold}\nProcessing...")
    print(f"{count} out of {total} ({percentage:.1f}%) values in {filename} are greater than {threshold}.")


# 6. File Filter
def question_6():
    filename = str(input("Filename: "))
    print(filename)
    in_file = open("letter.txt", "r")
    out_file = open("output.txt", "w")
    for i in in_file:
        if "it" in i:
            print(i, file=out_file)
    out_file.close()
    in_file.close()





# question_4()
# question_5()
question_6()
