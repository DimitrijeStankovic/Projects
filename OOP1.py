class Student:
 
    def getInfo(self, name=True,adress=True,phone=True,course=True,index_number=True): 
            if name is not True:
                print('Name: ' + name)
                if adress is not True:
                    print('Adress:    ' + adress)
                    if phone is not True:
                        print('Phone:  ' + phone)
                        if course is not True:
                            print('Course:  ' + course)
                            if index_number is not True:
                                print('Index number: '+ index_number)
                               
            else: 
                pass 

class Studenti:
    def __init__(self,name1,adress1,phone1,course1,index_number1):
        self.name1= name1
        self.adress1=adress1
        self.phone1=phone1
        self.course1=course1
        self.index_number1=index_number1            
                
    def getInfo(self):
        return('Name: ',self.name1,'Adress: ', 
        self.adress1,'Phone: ',self.phone1,'Course: ',self.course1,
        'Index_number: ',self.index_number1)


obj = Student() 
obj.getInfo('John Benson','High Park 36','(507) 833-3567','Geography','123/007')

obj=Studenti('Marko Markovic','Bulevar Avnoja 21','+381653275','Python','12/06')
print(obj.getInfo()) 

obj=Studenti('Petar Petrovic','Bulevar Revolucije 56','+375544655','Math','90/16')
print(obj.getInfo()) 

obj=Studenti('Milos Milosevic','Kraljevica Marka 45','+312637821','Static','311/13')
print(obj.getInfo()) 











