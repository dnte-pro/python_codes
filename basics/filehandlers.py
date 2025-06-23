print("Here is my file handler code")
f1 = open("files/diary.txt", "r")
print(f1.read())

print("Now I will write to the file")
f2= open("files/diary2.txt", "w")
f2.write("Writing in my diary file.\n")
f2.write("Writing in my diary file!")
f2.close()