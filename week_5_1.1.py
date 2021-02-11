class Nisit:
    def __init__(self,name,gender,year,faculty,province):
        self.name = name
        self.gender = gender
        self.year = year
        self.faculty = faculty
        self.province = province
    
    def showNisit(self):
        print(self.name,self.gender,self.year,self.faculty,self.province)
def input_data():
    global name,gender,year,faculty,province
    print('-------------------แนะนำตัว--------------------')
    data = input('name:gender:year:faculty:province ')
    date = data.split(':')
    name = date[0]
    gender = date[2]
    year = date[3]
    faculty = date[4]
    province = date[5]

input_data()
x=Nisit(name,gender,year,faculty,province)
x.showNisit()