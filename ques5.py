text=input("enter text you want write in file\n")
with open('text.txt','w') as file:
    file.writelines(text)
