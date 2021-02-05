print("ป้อนชื่ออาหารสุดโปรดของคุณหรือ exit เพื่อออกจากโปรแกรม")
food=[]
b=0
while(True):
    b=b+1
    print("อาหารสุดโปรดอันดับที่",b,end=" ")
    x=input(":")
    food.append(x)
    if x == "exit":
        break   
print("อาหารของคุณมีดังนี้:",end="") 
for x in range(1,b):
    print(x,'.',food[x-1],end="")