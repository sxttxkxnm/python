import os
choice = 0
filename = ''

def menu():
    global choice
    print('Menu\n1.Open Calculator\n2.Open Notepad\n3.Exit')
    choice = input('Select Menu : ')

def opennotepad():
    filename= 'C:\\Windows\\SysWOW64\\notepad.exe'
    print('Memoradum writing %s'%filename)
    os.system(filename)

def opencalculator():
    filename= 'C:\\Windows\\SysWOW64\\calc.exe'
    print('Calculate Number %s'%filename)
    os.system(filename)

while True:
    menu()
    if choice == '1':
        opencalculator()
    elif choice == '2':
        opennotepad()
    else:
        break