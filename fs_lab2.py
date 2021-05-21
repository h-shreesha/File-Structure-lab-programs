class student:
    def __init__(self):
        self.name = input('Enter Name: ')
        self.usn = input('Enter USN: ')
        self.branch = input('Enter Branch: ') 

def pack(storefile,s):
    record = s.name.center(20)+'|'+s.usn.center(17)+'|'+s.branch.center(7)+'\n'
    storefile.write(record)
    print('Packed into student.txt successfully\n')

def unpack(storefile):
    print('NAME'.center(20)+'USN'.center(17)+'BRANCH'.center(10)+'\n'+'-'*70)
    for record in storefile:
            print(record)
    print('-'*70+'\n')

def modify(storefile):
    name = input('Enter name to modify: ')
    if name not in storefile.read():
        print(name+" not found\n")
        return
    storefile.seek(0,0)
    pos=-48
    for record in storefile.readlines():
        pos += 48
        if name == record[:20].strip():
            storefile.seek(pos,0)
            print('Enter new details of',name)
            s = student()
            pack(storefile,s)
            pos+=48
    print('')  

def search(storefile):
    name = input('Enter name to search: ')
    if name not in storefile.read():
        print(name+" not found\n")
        return
    storefile.seek(0,0)
    name = name.center(20)
    print('NAME'.center(20)+'USN'.center(17)+'BRANCH'.center(7)+'\n'+'-'*50)
    for record in storefile:
        if name == record[:20]:
                print(record)
    print('-'*50+'\n')      

while True:
    choice = input('1.Pack\t2.Unpack\t3.Modify\t4.Search\t5.Exit\nEnter your choice: ')
    if choice == '1':
        storefile = open('student.txt','a')
        s = student()
        pack(storefile,s)
        storefile.close()
    elif choice == '2':
        storefile = open('student.txt','r')
        unpack(storefile)
        storefile.close()
    elif choice == '3':
        storefile = open('student.txt','r+')
        modify(storefile)
        storefile.close()
    elif choice == '4':
        storefile = open('student.txt','r')
        search(storefile)
        storefile.close()
    elif choice == '5':
        break
    else:
        print('Invalid choice\n')
 


