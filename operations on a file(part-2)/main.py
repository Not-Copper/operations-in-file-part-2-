with open("a.txt","w")as file:
    file.write("Hi I am Saadiq , I am 11 years old")
file.close()
with open("a.txt","r")as file:
    data=file.readlines()
    print("Words in this file are........")
    for line in data:
        word=line.split(",")
        print(word)
file.close()