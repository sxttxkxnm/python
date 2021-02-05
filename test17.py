import os
word_dictionary = {}
def menu():
    global choice
    print('พจนานุกรม\n1. เพิ่มคำศัพท์\n2. แสดงคำศัพท์ทั้งหมด\n3. ลบคำศัพท์\n4. ออกจากโปรแกรม')
    choice=input('input choice : ')

def adddict():
    word = input("\nเพิ่มคำศัพท์ :\t")
    typeword = input('ชนิดของคำ: (n. ,v. ,adj. ,adv.) : ')
    mean = input('ความหมาย : ')
    word_dictionary[word]=typeword,mean
    print('เพิ่มคำศัพท์เรียบร้อบแล้ว')

def showdict():
    print('\n\tคำศัพท์ทั้งหมด\n{0:<11}{1:<8}{2}'.format('คำศัพท์','ประเภท','ความหมาย'))
    for key in word_dictionary:
        print("{}{:<3}{}".format(key,'',word_dictionary[key]))

def deletee():
    delete_word = input("\nพิมพ์คำศัพท์ที่ต้องการลบ : ")
    yes_no = input("ต้องการลบ {} ใช่หรือไม (y/n): ".format(delete_word))
    if yes_no=='y':
        del word_dictionary[delete_word]
        print("ลบ"+delete_word+"เรียบร้อยแล้ว")
while True:
    menu()
    if choice == '1':
        adddict()
    elif choice == '2':
        showdict()
    elif choice == '3':
        deletee()
    elif choice == '4':
        c = input("ต้องการใช้งานโปรแกรมต่อหรือไม่ y/n : ")
        if c.lower() == 'y':
            os.system('cls')
        elif c.lower() == 'n':
            os.system('cls')
            break