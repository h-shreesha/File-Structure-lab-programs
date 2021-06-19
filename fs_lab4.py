class student:
    def __init__(self):
        self.usn = input('Enter usn: ')
        self.name = input('Enter name: ')
        self.branch = input('Enter branch: ')
        self.sem = input('Enter sem: ')


def insert(storefile, s):
    record = s.usn+'|'+s.name+'|'+s.branch+'|'+s.sem+'#'
    storefile.write(record)
    print('...Inserted into student.txt successfully...\n\n')
    storefile.close()


def unpack(s):
    ind = s.split('|')
    return ind


def createrrn(storefile):
    buf = ''
    count = -1
    rrn = []
    while storefile:
        ch = storefile.read(1)
        if not ch:
            break
        if ch != '#':
            buf = buf+ch
        else:
            pos = storefile.tell()
            lenbuf = len(buf)
            finalpos = pos-lenbuf-1
            rrn.append(finalpos)
            count = count+1
            buf = ''
            continue
    return count, rrn


def search(storefile):
    count, rrn = createrrn(storefile)
    buf = ''
    key = int(input("Enter the RRN value to be searched\n"))
    if key > count or key <= -1:
        print("Record with RRN ", key, "doesnt exist")
    else:
        pos = rrn[key]
    storefile.seek(pos, 0)
    while True:
        ch = storefile.read(1)
        if ch != '#':
            buf = buf+ch
        else:
            d = unpack(buf)
            print("Record d are:\n"+"USN".center(15), ":", d[0], "\n"+"Name".center(15),":",d[1],"\n"+"Branch".center(15),":",d[2],"\n"+"Sem".center(15),":",d[3])
            buf = ''
            break
    storefile.close()


while True:
    choice = input('1.Insert\t2.Search\t3.Exit\nEnter your choice: ')
    if choice == '1':
        storefile = open('student.txt', 'a')
        s = student()
        insert(storefile, s)
        storefile.close()
    elif choice == '2':
        storefile = open('student.txt', 'r')
        search(storefile)
        storefile.close()
    elif choice == '3':
        break
    else:
        print('Invalid choice\n')
