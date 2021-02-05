a=int(input("กรุณากรอกจำนวนนักเรียน :"))
point=[0,0,0,0,0,0]
score=["90-100:","80-89:","70-79:","60-69:","50-59:","0-49:"]
for x in range(0,a):
    b=int(input("คะแนน :"))
    if b<=100 and b>=90:
        point[0]+=1
    elif b<90 and b>=80:
        point[1]+=1
    elif b<80 and b>=70:
        point[2]+=1
    elif b<70 and b>=60:
        point[3]+=1
    elif b<60 and b>=50:
        point[4]+=1
    else :
        point[5]+=1
for x in range(0,6):
    print(score[x]+":"+"*"*point[x])