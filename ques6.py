text=input("enter the name of file with txt extension\n")
file=open(text,'r')
info=file.readline()
print(info)
file.close()