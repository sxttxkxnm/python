import sqlite3,os
conn = sqlite3.connect(r"D:\Poom_Python\MidtermProject.db")
c = conn.cursor()
#c.execute ('''CREATE TABLE MidtermProject(id integer PRIMARY KEY AUTOINCREMENT,
#    Name varchar(50) NOT NULL,
#    Phone varchar(10) NOT NULL,
#    Court varchar(30) NOT NULL,
#    Time varhar(10) NOT NULL,
#    Borrow_Equipment varchar(30) NOT NULL,
#    Another_Service varchar(30) NOT NULL,
#    Total Price varchar(30) NOT NULL)''')
#conn.commit()
#conn.close()
#เพิ่ม แก้ไข ลบ
service = ""
save = 3 
b = ""
sa = 3
bor = 4
an = 3
price = 0
totalbat = 0
totalchicken = 0
totalplastic = 0
totalsneaker = 0
totalwater = 0
sumprice = 0
courtlist=['สนามที่ 1','สนามที่ 2','สนามที่ 3','']
servicelist=['น้ำเปล่า','สปอนเซอร์','น้ำอัดลม','']
borrowlist=['ไม้แบดมินตัน','ลูกแบดขนไก่','ลูกแบดพลาสติก','รองเท้าแบดมินตัน','']
timelist=[]
pricecourt = {
    'สนามที่ 1': 100
    ,'สนามที่ 2': 200
    ,'สนามที่ 3': 300
}
priceborrow ={
    'ไม้แบดมินตัน': 50,
    'ลูกแบดขนไก่': 20,
    'ลูกแบดพลาสติก': 40,
    'รองเท้าแบดมินตัน': 100,
}
priceservice = {
    'น้ำเปล่า': 10,
    'สปอนเซอร์': 15,
    'น้ำอัดลม': 20,
}
courtdt = {
    "C1":"สนามที่ 1",
    "C2":"สนามที่ 2",
    "C3":"สนามที่ 3"
}
borrowdt = {
    "R1":"ไม้แบดมินตัน",
    "R2":"ลูกแบดขนไก่",
    "R3":"ลูกแบดพลาสติก",
    "R4":"รองเท้าแบดมินตัน"
}
servicedt = {
    "W1":"น้ำเปล่า",
    "W2":"สปอนเซอร์",
    "W3":"น้ำอัดลม"
}

name = input('กรุณากรอกชื่อ-สกุล : ')
tel = str(input('เบอร์โทรศัพท์ : '))
print('******บันทึกข้อมูลแล้ว******')
data = (name,tel)
conn.commit()
conn.close()

def Menu():
    global choice
    print("---------------------\nโปรแกรมจองสนามแบดมินตัน\n---------------------")
    print('[1]ต้องการจองสนาม\n[2]ต้องการยืมอุปกรณ์\n[3]ต้องการใช้บริการอื่นๆ\n[4]แก้ไขรายการ\n[5]ลบรายการ\n[6]สรุปรายการ\n[7]ออกจากระบบ')
    choice = input('\nกรุณาเลือกรายการ: ')

def edit():
    oldedit = input('ต้องการแก้ไข :  ')
    newedit = input('เป็น :  ')
    conn = sqlite3.connect(r"D:\Poom_Python\MidtermProject.db")
    c = conn.cursor()
    d = conn.cursor()
    if oldedit in courtdt:#ถ้าต้องการแก้ไขสนามให้ทำเงื่อนไขนี้
        d.execute('SELECT Total,Time,Borrow_Equipment,Another_Service FROM MidtermProject  WHERE Court = ? and name = ? and Phone = ?',(courtdt[oldedit],name,tel))
        oldall = d.fetchone()
        oldtotal = oldall[0]
        time = oldall[1]
        newtotal = int(oldtotal)-(int(time)*pricecourt[courtdt[oldedit]])
        newtotal += (int(time)*(pricecourt[courtdt[newedit]]))#เวลาเก่า*ราคาสนามใหม่
        c.execute('UPDATE MidtermProject SET Court = ?,Total = ? WHERE Court = ? and name = ? and Phone = ? and Borrow_Equipment = ? and Another_Service = ?',(courtdt[newedit],newtotal,courtdt[oldedit],name,tel,oldall[2],oldall[3]))
    if oldedit in borrowdt:#ถ้าแก้ยืมให้ทำเงื่อนไขนี้
        d.execute('SELECT Total,Court,Another_Service FROM MidtermProject  WHERE Borrow_Equipment = ? and name = ? and Phone = ?',(borrowdt[oldedit],name,tel))
        oldall = d.fetchone()
        oldtotal = oldall[0]
        newtotal = int(oldtotal) - priceborrow[borrowdt[oldedit]]
        newtotal += (priceborrow[borrowdt[newedit]])
        c.execute('UPDATE MidtermProject SET Borrow_Equipment = ?,Total = ? WHERE Borrow_Equipment = ? and name = ? and Phone = ? and Court = ? and Another_Service = ?',(borrowdt[newedit],newtotal,borrowdt[oldedit],name,tel,oldall[1],oldall[2]))
    if oldedit in servicedt:#ถ้าแก้ไขเซอร์วิสอื่นๆใก้ทำเงื่อนไขนี้
        d.execute('SELECT Total,Court,Borrow_Equipment FROM MidtermProject  WHERE Another_Service = ? and name = ? and Phone = ?',(servicedt[oldedit],name,tel))
        oldall = d.fetchone()
        oldtotal = oldall[0]
        newtotal = int(oldtotal)-priceservice[servicedt[oldedit]]
        newtotal += (priceservice[servicedt[newedit]])
        c.execute('UPDATE MidtermProject SET Another_Service = ?,Total = ? WHERE Another_Service = ? and name = ? and Phone = ? and Court = ? and Borrow_Equipment = ?',(servicedt[newedit],newtotal,servicedt[oldedit],name,tel,oldall[1],oldall[2]))
    if oldedit in (timelist):#อัพเดทเวลา
        d.execute('SELECT Total,Court,Borrow_Equipment,Another_Service FROM MidtermProject  WHERE Time = ? and name = ? and Phone = ?',(oldedit,name,tel))
        oldall = d.fetchone()
        oldtotal = oldall[0]
        time = newedit#เวลาใหม่
        newtotal = int(oldtotal)-(int(oldedit)*pricecourt[oldall[1]])#ราคารวมเก่า-เวลาเก่า*ราคาสนาม
        newtotal += (int(time)*(pricecourt[oldall[1]]))#เวลาใหม่*สนาม
        c.execute('UPDATE MidtermProject SET Time = ?, Total = ? WHERE Time = ? and name = ? and Phone = ? and Court = ?and Borrow_equipment = ? and Another_Service = ?',(newedit,newtotal,oldedit,name,tel,oldall[1],oldall[2],oldall[3]))
    conn.commit()
    conn.close()

def delete():
    deletedata = input('ต้องการลบรายการ : ')
    conn = sqlite3.connect(r"D:\Poom_Python\MidtermProject.db")
    c = conn.cursor()
    d = conn.cursor()
    if deletedata in courtdt:
        d.execute('SELECT Total,Time,Borrow_Equipment,Another_Service FROM MidtermProject  WHERE Court = ? and name = ? and Phone = ?',(courtdt[deletedata],name,tel))
        oldall = d.fetchone()
        oldtotal = oldall[0]
        time = oldall[1]
        newtotal = int(oldtotal)-(int(time)*pricecourt[courtdt[deletedata]])#ราคารวมเก่า-เวลา*สนาม เพื่อเอาราคาสนามออก
        c.execute('UPDATE MidtermProject SET Court = ? ,Time = ? ,Total = ? WHERE Court = ? and name = ? and Phone = ? and Borrow_Equipment = ? and Another_Service = ?',("","",newtotal,courtdt[deletedata],name,tel,oldall[2],oldall[3]))
    if deletedata in borrowdt:
        d.execute('SELECT Total,Court,Another_Service FROM MidtermProject  WHERE Borrow_Equipment = ? and name = ? and Phone = ?',(borrowdt[deletedata],name,tel))
        oldall = d.fetchone()
        oldtotal = oldall[0]
        newtotal = int(oldtotal) - priceborrow[borrowdt[deletedata]]
        c.execute('UPDATE MidtermProject SET Borrow_Equipment = ?,Total = ? WHERE Borrow_Equipment = ? and name = ? and Phone = ? and Court = ? and Another_Service = ?',("",newtotal,borrowdt[deletedata],name,tel,oldall[1],oldall[2]))
    if deletedata in servicedt:
        d.execute('SELECT Total,Court,Borrow_Equipment FROM MidtermProject  WHERE Another_Service = ? and name = ? and Phone = ?',(servicedt[deletedata],name,tel))
        oldall = d.fetchone()
        oldtotal = oldall[0]
        newtotal = int(oldtotal)-priceservice[servicedt[deletedata]]
        c.execute('UPDATE MidtermProject SET Another_Service = ? ,Total = ? WHERE Another_Service = ? and name = ? and Phone = ? and Court = ? and Borrow_Equipment = ?',("",newtotal,servicedt[deletedata],name,tel,oldall[1],oldall[2]))
    conn.commit()
    conn.close()


while True:
    Menu()
    if choice == '1': #จองสนาม
        print("\nจองสนามแบดมินตัน\n----------------------------")
        print('[C1]สนามที่ 1 100 บาท\n[C2]สนามที่ 2 200 บาท\n[C3]สนามที่ 3 300 บาท')
        S = input("\nกรุณาเลือกสนาม: ")
        t = int(input('ต้องการจองสนามนานเท่าไหร่ (ชั่วโมง) : '))
        
        if S == 'C1':
            sa = 0
            price = (t * 100)
            print(str(price) + ' บาท')
            sumprice += price
        if S == 'C2':
            sa = 1
            price = (t * 200)
            print(str(price) + ' บาท')
            sumprice += price
        if S == 'C3':
            sa = 2
            price = (t * 300)
            print(str(price) + ' บาท')
            sumprice += price 


    elif choice == '2': #ยืมอุปกรณ์
        print("\nยืมอุปกรณ์\n----------------------------")
        print('[R1]ไม้แบดมินตัน  50 บาท\n[R2]ลูกแบดขนไก่ 20 บาท\n[R3]ลูกแบดพลาสติก 40 บาท\n[R4]รองเท้าแบดมินตัน 100 บาท')
        b = input("\nกรุณาเลือกบริการ: ")
        if b == 'R1':
            bor = 0
            x = int(input('จำนวนไม้แบดที่ต้องการ :  '))
            totalbat = 50 * x
            print(str(totalbat) + ' บาท')
            sumprice += totalbat
        if b == 'R2':
            bor = 1
            x = int(input('จำนวนลูกแบดขนไก่ที่ต้องการ :'))
            totalchicken = 20 * x
            print(str(totalchicken) + ' บาท')
            sumprice += totalchicken
        if b == 'R3':
            bor = 2
            x = int(input('จำนวนลูกแบดพลาสติกที่ต้องการ :'))
            totalplastic = 40 * x
            print(str(totalplastic) + ' บาท')
            sumprice += totalplastic
        if b == 'R4':
            bor = 3
            x = int(input('จำนวนรองเท้าแบดมินตันที่ต้องการ :'))
            totalsneaker = 100 * x
            print(str(totalsneaker) + ' บาท')
            sumprice += totalsneaker


    elif choice == '3': #บริการอื่นๆ
        print("\nบริการอื่นๆ\n----------------------------")
        print('[W1]น้ำเปล่า 10 บาท\n[W2]สปอนเซอร์ 15 บาท\n[W3]น้ำอัดลม 20 บาท')
        service = input("\nกรุณาเลือกบริการ: ")
        if service == 'W1':
            an = 0
            x = int(input('จำนวนน้ำเปล่าที่ต้องการ :'))
            totalwater = 10 * x
            print(str(totalwater) + ' บาท')
            sumprice += totalwater
        if service == 'W2':
            an = 1
            x = int(input('จำนวนสปอนเซอร์ที่ต้องการ :'))
            totalwater = 15 * x
            print(str(totalwater) + ' บาท')
            sumprice += totalwater
        if service == 'W3':
            an = 2
            x = int(input('จำนวนน้ำอัดลมที่ต้องการ :'))
            totalwater = 20 * x
            print(str(totalwater) + ' บาท')
            sumprice += totalwater
        save = 0 

    elif choice == '4':#แก้ไขรายการ
        print("                                                           แก้ไขราการ                                                                       ")
        conn = sqlite3.connect(r"D:\Poom_Python\MidtermProject.db")
        c = conn.cursor()
        print('\n--------------------------------------------------------  สนามแบดมินตัน  --------------------------------------------------------------------')
        print("ชื่อผู้จอง               สนามที่จอง                 เวลาที่จอง                     อุปกรณ์                    บริการอื่นๆ                      คิดเป็นเงิน")
        print("-------------------------------------------------------------------------------------------------------------------------------------------")
        d = conn.cursor()
        d.execute('SELECT name,Court,Time,Borrow_Equipment,Another_Service,Total FROM MidtermProject WHERE name = ? and Phone = ?',(name,tel))
        totalnum = d.fetchall()
        e = conn.cursor()
        e.execute('SELECT * FROM MidtermProject WHERE name = ? and Phone = ?',(name,tel))
        all = e.fetchall()
        for i in range(0,len(all)):#โชว์ข้อมูลที่จอง 
            num = totalnum[i]#num เก็บข้อมูลบรรทัด 203
            print("{0: <20}{1: <30}{2: <30}{3: <30}{4: <30}{5: <30}".format(num[0],num[1],num[2],num[3],num[4],num[5]))
            if num[2]!="":#num[2]เก็บเวลา 
                timelist.append(str(num[2]))#เอาเวลามาเก็บ
        edit()
        while True:
            a = input('ต้องการแก้ไขต่อหรือไม่ y/n : ')
            if a == 'y':
                edit()
            if a == 'n':
                break
        conn.close()
        
    elif choice == '5':#ลบรายการ
        conn = sqlite3.connect(r"D:\Poom_Python\MidtermProject.db")
        c = conn.cursor()
        print("                                                            ลบราการ                                                                       ")
        print('\n--------------------------------------------------------  สนามแบดมินตัน  --------------------------------------------------------------------')
        print("ชื่อผู้จอง               สนามที่จอง                 เวลาที่จอง                     อุปกรณ์                    บริการอื่นๆ                      คิดเป็นเงิน")
        print("-------------------------------------------------------------------------------------------------------------------------------------------")
        d = conn.cursor()
        d.execute('SELECT name,Court,Time,Borrow_Equipment,Another_Service,Total FROM MidtermProject WHERE name = ? and Phone = ?',(name,tel))
        totalnum = d.fetchall()
        e = conn.cursor()
        e.execute('SELECT * FROM MidtermProject WHERE name = ? and Phone = ?',(name,tel))
        all = e.fetchall()
        for i in range(0,len(all)):
            num = totalnum[i]
            print("{0: <20}{1: <30}{2: <28}{3: <28}{4: <28}{5: <28}".format(num[0],num[1],num[2],num[3],num[4],num[5]))
        delete()#เรียกใช้delete
        while True:
            a = input('ต้องการลบต่อหรือไม่ y/n : ')
            if a == 'y':
                delete()
            if a == 'n':
                break
        e = conn.cursor()
        e.execute('SELECT Total,Court,Time,Borrow_Equipment,Another_Service FROM MidtermProject  WHERE name = ? and Phone = ?',(name,tel))
        del_data = e.fetchall()[0]
        if del_data[0] == 0 and del_data[1] == '' and  del_data[2] == ''and del_data[3] == '' and  del_data[4] == '':#เช็คว่าไม่ได้จอง
            f = conn.cursor()
            f.execute('DELETE FROM MidtermProject WHERE name = ? and Phone = ? and Court = ? and Borrow_Equipment = ? and Time = ? and Another_Service = ? and Total = ?',(name,tel,del_data[1],del_data[3],del_data[2],del_data[4],del_data[0]))#ลบบรรทัดออก
        conn.commit()
        conn.close()

    elif choice == '6': #สรุป
        conn = sqlite3.connect(r"D:\Poom_Python\MidtermProject.db")
        c = conn.cursor()#สร้างตัวแปรสำหรับ execute
        data = (name,tel,courtlist[sa],t,borrowlist[bor],servicelist[an],sumprice)
        if S != '' or t != '' or b != '' or service !='' or sumprice != 0:
            c.execute ('INSERT INTO MidtermProject(name,Phone,Court,Time,Borrow_Equipment,Another_Service,Total) VALUES(?,?,?,?,?,?,?)',data)
        conn.commit()
        save = 1 
        print("                                                           สรุปรายการ                                                                       ")
        print('\n--------------------------------------------------------  สนามแบดมินตัน  -------------------------------------------------------------------')
        print("ชื่อผู้จอง              สนามที่จอง                 เวลาที่จอง                          อุปกรณ์                    บริการอื่นๆ                  คิดเป็นเงิน")
        print("-------------------------------------------------------------------------------------------------------------------------------------------")
        d = conn.cursor()
        d.execute('SELECT name,Court,Time,Borrow_Equipment,Another_Service,Total FROM MidtermProject WHERE name = ? and Phone = ?',(name,tel))
        totalnum = d.fetchall()
        e = conn.cursor()
        e.execute('SELECT * FROM MidtermProject WHERE name = ? and Phone = ?',(name,tel))
        all = e.fetchall()
        for i in range(0,len(all)):
            num = totalnum[i]
            print("{0: <20}{1: <30}{2: <30}{3: <30}{4: <30}{5: <30}".format(num[0],num[1],num[2],num[3],num[4],num[5]))
        f = conn.cursor()
        f.execute('SELECT SUM(Total) FROM MidtermProject WHERE name = ? and Phone = ?',(name,tel))
        allprice = f.fetchall()[0][0]
        print('\n{0: <108}{1: <24}{2}'.format("ราคารวม "," ",allprice))#ปริ้นราคารวมทั้งหมด เก็บใน allprice
        S= ''
        t=''
        b=''
        service = ''
        sumprice = 0
        sa = 3
        bor = 4
        an = 3
        conn.close()

    elif choice == '7': #ออกจากโปรแกรม
        
        c=input('ต้องการออกจากโปรแกรมหรือไม่ y/n : ')
        if c =='y':
            os.system('cls')
            print('ปิดโปรแกรมเรียบร้อย')
            break
        elif c =='n':
            os.system('cls')
