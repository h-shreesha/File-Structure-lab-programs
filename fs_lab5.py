import time
import os


class student:
    def __init__(self):
        self.name = input('Enter name: ')
        self.usn = input('Enter usn: ')
        self.branch = input('Enter branch: ')
        self.sem = input('Enter sem: ')


def insert(storefile, s):
    record = s.name+'|'+s.usn+'|'+s.branch+'|'+s.sem+'\n'
    pos = storefile.tell()
    storefile.write(record)
    indexfile = open("index.txt", 'a')
    indfile = str(pos)+'|'+s.usn+'\n'
    indexfile.write(indfile)
    print('...Inserted into student.txt successfully...\n\n')
    indexfile.close()


def unpack(s):
    ind = s.split('|')
    return ind


def search(storefile):
    key = int(input("Enter the USN  to be searched: "))
    indexfile = open("index.txt", 'r')

    for i in indexfile:
        x = i.split('|')
        if "*" in x[0]:
            continue
        if key == int(x[1]):
            storefile.seek(int(x[0]), 0)
            record = unpack(storefile.readline())
            print("\nRecord details are:\n"+"Name".center(15), ":", record[0], "\n"+"USN".center(
                15), ":", record[1], "\n"+"Branch".center(15), ":", record[2], "\n"+"Sem".center(15), ":", record[3]+"\n")
            indexfile.close()
            return
    print("Not found")


def delete(storefile):
    keyc = int(input("Enter the USN  to be deleted: "))
    indexfile = open("index.txt", "r+")
    if str(keyc) not in indexfile.read():
        print("Not found")
        return
    indexfile.seek(0, 0)
    pos = 0
    for i in indexfile:
        x = i.split('|')
        if "*" in x[1]:
            continue
        if keyc == int(x[1]):
            indexfile.seek(pos, 0)
            indexfile.write('*')
            storefile.seek(int(x[0]), 0)
            storefile.write("*")
            print(keyc, " Deleted successfully")
            indexfile.close()
            return
        pos += len(i)


while True:
    choice = input(
        '\n1.Insert\t2.Search\t3.Delete\t4.Exit\nEnter your choice: ')
    if choice == '1':
        storefile = open('student.txt', 'a')
        n = int(input("Enter the number of students to insert:"))
        for i in range(n):
            s = student()
            insert(storefile, s)
        storefile.close()
    elif choice == '2':
        storefile = open('student.txt', 'r')
        search(storefile)
        storefile.close()
    elif choice == '3':
        storefile = open('student.txt', 'r+')
        delete(storefile)
        storefile.close()
    elif choice == '4':
        print("...Exited...")
        break
    else:
        print('Invalid choice\n')
