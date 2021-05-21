print("Shreesha\n 4MT18IS053")

n = int(input("Enter the no of names: "))
names = []
for i in range(n):
    ip = input("Enter the name: ")
    names.append(ip)
print("Names in reverse order:")
for n in names:
    print(n[::-1])

print('*'*100)

file = input("Enter the file containing names:")
try:
    namefile = open(file,"r")
    storefile = input("Enter the file name to be stored in reverse order:")
    output = open(storefile,"w")
    for name in namefile:
        output.write(name[::-1])
    namefile.close()
    output.close()
    print("Reversed names are stored in "+storefile+" successfully")
except:
    print("File "+namefile+"not found")