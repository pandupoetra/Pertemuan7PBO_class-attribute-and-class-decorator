class Passenger:
    TITLES=("Mr","Mrs","Ms")
    def __init__(self,title,fname,lname):
        if title not in self.TITLES:
            raise ValueError("%s is not a valid title"%title)
        self.title=title 
        self.fname=fname
        self.lname=lname
            
#pembuatan objek
p1=Passenger("Mr","Kiewlamphone","Souvanlith")
#mengakses clas atribut dari objek
print(p1.TITLES)
#mengakses clas atribut dari kelas
print(Passenger.TITLES)
#mengakses instance atribut dari objek
print(p1.title)
#mengakses instance atribut dari kelas
print(Passenger.title)