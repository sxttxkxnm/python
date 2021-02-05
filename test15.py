import os
choice=0
thing=[0,0,0,0,0]
pick=0
def menu():
    global choice
    print('\tMenu\n1. แสดงรายการสินค้า\n2. หยิบสินค้าใส่ตะกร้า\n3. แสดงรายการและจำนวนสินค้าที่หยิบ\n4. หยิบสินค้าออกจากตะกร้า\n5. ปิดโปรแกรม')
    choice = input('เลือกทำรายการ: ')

def showmenu():
    print('\t\nรายการสินค้า\n1. ขนม 20 บาท\n2. น้ำเปล่า 8 บาท\n3. น้ำอัดลม 17 บาท\n4. ยาดม 25 บาท\n5. กล้วย 8 บาท\n')

def pickmenu():
    global pick
    print('\t\nรายการสินค้า\n1. ขนม\n2. น้ำเปล่า\n3. น้ำอัดลม\n4. ยาดม\n5. กล้วย')
    pick=int(input('เลือกหยิบสินค้าหมายเลข: '))
    if pick==1:
        thing[0] += 1
    elif pick==2:
        thing[1] += 1
    elif pick==3:
        thing[2] += 1
    elif pick==4:
        thing[3] += 1
    elif pick==5:
        thing[4] += 1

def showyourpick():
    score=['ขนม','น้ำเปล่า','น้ำอัดลม','ยาดม','กล้วย']
    price=[20,8,17,25,8]
    print('{0:-<13}{1:-<13}{2:-<13}{3}'.format('สินค้า','ราคา','จำนวน','ราคารวม'))
    for i in range(0,5):
        print('{0:-<13}{1:-<13}{2:-<13}{3}'.format(score[i],price[i],thing[i],thing[i]*price[i]))

def deletyourpick():
    print('\t\nรายการสินค้า\n1. ขนม\n2. น้ำเปล่า\n3. น้ำอัดลม\n4. ยาดม\n5. กล้วย')
    depick=int(input('เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์-1 เพื่อออก : '))
    if depick==1:
        thing[0]-=1
    elif depick==2:
        thing[1]-=1
    elif depick==3:
        thing[2]-=1
    elif depick==4:
        thing[3]-=1
    elif depick==5:
        thing[4]-=1

while True:
    menu()
    if choice=='1':
        showmenu()
    elif choice=='2':
        pickmenu()
    elif choice=='3':
        showyourpick()
    elif choice=='4':
        deletyourpick()
    elif choice=='5':
        c=input('ต้องการออกจากโปรแกรมหรือไม่ y/n : ')
        if c.lower=='y':
            screen_clear()
        elif c.lower=='n':
            screen_clear()
            break