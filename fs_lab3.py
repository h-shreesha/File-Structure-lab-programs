class student:
    def __init__(self):
        self.usn = input('Enter usn: ')
        self.name = input('Enter name: ')
        self.branch = input('Enter branch: ')
        self.sem = input('Enter sem: ')


def pack(fp, s):
    record = s.usn+'|'+s.name+'|'+s.branch+'|'+s.sem+'\n'
    fp.write(record)


def unpack(fp):
    print('USN'.center(20)+'NAME'.center(20) +
          'BRANCH'.center(20)+'SEM\n'+'-'*65)
    for record in fp:
        for i in record.split('|')[:-1]:
            print(i.center(20), end='')
        print(record.split('|')[-1], end='')
    print('-'*65+'\n')


def modify(fp):
    usn = input('Enter usn to modify: ')
    if usn not in fp.read():
        print(usn+" not found\n")
        return
    fp.seek(0, 0)
    data = ""
    for record in fp:
        if usn in record:
            print('Enter new details of', usn)
            s = student()
            data += s.usn+'|'+s.name+'|'+s.branch+'|'+s.sem+'\n'
        else:
            data += record
    fp.close()
    fp = open('students.txt', 'w')
    fp.write(data)
    fp.close()
    print('')


def search(fp):
    usn = input('Enter usn to search: ')
    if usn not in fp.read():
        print(usn+" not found\n")
        return
    fp.seek(0, 0)
    print('USN'.center(20)+'NAME'.center(20) +
          'BRANCH'.center(20)+'SEM\n'+'-'*65)
    for record in fp:
        if usn in record:
            for i in record.split('|')[:-1]:
                print(i.center(20), end='')
            print(record.split('|')[-1], end='')
    print('-'*65+'\n')


while True:
    choice = input(
        'Choices are,\n1.PACK\t\t2.UNPACK\t3.MODIFY\t4.SEARCH\t5.STOP\nEnter yo ur choice: ')
    try:
        if choice == '1':
            fp = open('students.txt', 'a')
            s = student()
            pack(fp, s)
            fp.close()
        elif choice == '2':
            fp = open('students.txt', 'r')
            unpack(fp)
            fp.close()
        elif choice == '3':
            fp = open('students.txt', 'r')
            modify(fp)
        elif choice == '4':
            fp = open('students.txt', 'r')
            search(fp)
            fp.close()
        elif choice == '5':
            break
        else:
            print('Invalid choice\n')
    except FileNotFoundError:
        print('File not found\n')
