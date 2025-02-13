with open("c.txt") as fp:
    data1=fp.read()
with open("d.txt") as fp:
    data2=fp.read()
data1 +="\n"
data1 += data2
print("Merging 2 files....")
with open ("e.txt","w") as fp:
    fp.write(data1)